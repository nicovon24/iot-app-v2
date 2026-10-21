"""Embed simplified Natural Earth country boundaries into the standalone HTML.

Usage: py -3 designs/map-data/build_world.py PATH_TO_NE_50M_ADMIN0_GEOJSON
Natural Earth admin-0 countries, public domain. Coordinates are simplified
for display; country names, unique IDs, multipart geometry and holes remain.
"""
import json
import pathlib
import re
import sys


def rdp(points, tolerance=0.09):
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
target = pathlib.Path(__file__).resolve().parents[1] / 'IoTArg.html'
features = json.loads(source.read_text(encoding='utf-8'))['features']
countries, ids = [], set()
for feature in features:
    props, geometry = feature['properties'], feature['geometry']
    candidate = props.get('ISO_A2')
    if not candidate or candidate == '-99':
        candidate = props.get('ISO_A2_EH')
    if not candidate or candidate == '-99' or candidate in ids:
        candidate = props['ADM0_A3']
    assert candidate not in ids, candidate
    ids.add(candidate)
    polygons = [geometry['coordinates']] if geometry['type'] == 'Polygon' else geometry['coordinates']
    simplified = []
    for polygon in polygons:
        rings = []
        for ring in polygon:
            points = [[round(x, 4), round(y, 4)] for x, y in ring]
            reduced = rdp(points[:-1])
            if len(reduced) >= 3:
                rings.append(reduced + [reduced[0]])
        if rings:
            simplified.append(rings)
    countries.append({'id': candidate, 'name': props.get('NAME_ES') or props['NAME'], 'polygons': simplified})

assert {'AR', 'CL', 'US', 'MX'}.issubset(ids)
payload = json.dumps(countries, ensure_ascii=False, separators=(',', ':'))
html = target.read_text(encoding='utf-8')
start, end = '<!-- WORLD_BEGIN -->', '<!-- WORLD_END -->'
assert html.count(start) == html.count(end) == 1
html = html[:html.index(start) + len(start)] + '\n<script>const WORLD_COUNTRIES=' + payload + ';</script>\n' + html[html.index(end):]
html, replacements = re.subn(r'^const GEO=.*;$', 'const GEO=WORLD_COUNTRIES;', html, count=1, flags=re.MULTILINE)
assert replacements == 1 or 'const GEO=WORLD_COUNTRIES;' in html
target.write_text(html, encoding='utf-8', newline='\n')
print(f'Embedded {len(countries)} countries, {len(payload)} bytes, into {target}')
