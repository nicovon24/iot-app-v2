"""Embed simplified Natural Earth admin-1 boundaries for worldwide browsing.

Usage: py -3 designs/map-data/build_admin1.py PATH_TO_NE_10M_ADMIN1_GEOJSON PATH_TO_NE_50M_ADMIN0_GEOJSON
Natural Earth 10m admin-1, public domain. GeoRef overrides Argentina in the
HTML. The builder preserves IDs, multipart polygons, holes, and country keys.
"""
import json
import pathlib
import sys


def rdp(points, tolerance=0.10):
    if len(points) < 4:
        return points
    a, b = points[0], points[-1]
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = dx * dx + dy * dy
    maximum, index = -1, 0
    for i, p in enumerate(points[1:-1], 1):
        t = max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / length)) if length else 0
        distance = (p[0] - a[0] - t * dx) ** 2 + (p[1] - a[1] - t * dy) ** 2
        if distance > maximum:
            maximum, index = distance, i
    if maximum <= tolerance * tolerance:
        return [a, b]
    return rdp(points[: index + 1], tolerance)[:-1] + rdp(points[index:], tolerance)


source = pathlib.Path(sys.argv[1])
world_source = pathlib.Path(sys.argv[2])
target = pathlib.Path(__file__).resolve().parents[1] / 'IoTArg.html'
features = json.loads(source.read_text(encoding='utf-8'))['features']
world_features = json.loads(world_source.read_text(encoding='utf-8'))['features']
a3_to_id = {}
for feature in world_features:
    props = feature['properties']
    candidate = props.get('ISO_A2')
    if not candidate or candidate == '-99':
        candidate = props.get('ISO_A2_EH')
    if not candidate or candidate == '-99':
        candidate = props['ADM0_A3']
    a3_to_id[props['ADM0_A3']] = candidate

by_country, ids, skipped = {}, set(), []
for feature in features:
    props, geometry = feature['properties'], feature['geometry']
    country = props.get('iso_a2')
    if not country or country == '-99' or country not in {'AR', *a3_to_id.values()}:
        country = a3_to_id.get(props.get('adm0_a3'))
    if not country:
        skipped.append(props.get('adm1_code'))
        continue
    if country == 'AR':
        continue  # GeoRef has the Argentina geometry and IDs used by the demo.
    candidate = props.get('iso_3166_2')
    if not candidate or candidate == '-99' or (country, candidate) in ids:
        candidate = props.get('adm1_code')
    if not candidate or (country, candidate) in ids:
        skipped.append(props.get('adm1_code'))
        continue
    ids.add((country, candidate))
    name = props.get('name_es') or props.get('name') or candidate
    if '\ufffd' in name:
        name = props.get('name') or props.get('name_local') or candidate
    if '\ufffd' in name:
        name = candidate
    polygons = [geometry['coordinates']] if geometry['type'] == 'Polygon' else geometry['coordinates']
    simplified = []
    for polygon in polygons:
        rings = []
        for ring in polygon:
            points = [[round(x, 4), round(y, 4)] for x, y in ring]
            reduced = rdp(points[:-1])
            if len(reduced) < 3:
                reduced = rdp(points[:-1], 0.005)
            if len(reduced) < 3:
                reduced = points[:-1]
            if len(reduced) >= 3:
                rings.append(reduced + [reduced[0]])
        if rings:
            simplified.append(rings)
    if simplified:
        by_country.setdefault(country, []).append({'id': candidate, 'name': name, 'polygons': simplified})

assert {'CL', 'US', 'MX'}.issubset(by_country)
payload = json.dumps(by_country, ensure_ascii=False, separators=(',', ':'))
asset = target.parent / 'map-data' / 'world-admin1.js'
asset.write_text('const WORLD_ADMIN1=' + payload + ';\n', encoding='utf-8', newline='\n')
html = target.read_text(encoding='utf-8')
start, end = '<!-- ADMIN1_BEGIN -->', '<!-- ADMIN1_END -->'
assert html.count(start) == html.count(end) == 1
html = html[:html.index(start) + len(start)] + '\n<script src="map-data/world-admin1.js"></script>\n' + html[html.index(end):]
target.write_text(html, encoding='utf-8', newline='\n')
print(f'Built {sum(map(len, by_country.values()))} admin1 features, {len(by_country)} countries, {len(payload)} bytes in {asset}, skipped={len(skipped)}')
