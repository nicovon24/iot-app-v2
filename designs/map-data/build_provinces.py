"""Embed simplified GeoRef province boundaries into the standalone demo HTML.

Usage: py -3 designs/map-data/build_provinces.py PATH_TO_PROVINCIAS_GEOJSON
Source: https://apis.datos.gob.ar/georef/api/provincias.geojson
GeoRef / IGN, CC BY 4.0. Coordinates are simplified for display; IDs and
polygon/hole structure are retained. Antarctic coordinates remain in source.
"""
import json
import pathlib
import sys


def rdp(points, tolerance=0.06):
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
provinces = []
for feature in features:
    geometry = feature['geometry']
    polygons = [geometry['coordinates']] if geometry['type'] == 'Polygon' else geometry['coordinates']
    simplified = []
    for polygon in polygons:
        rings = []
        for ring in polygon:
            # GeoRef rings are closed. Simplify the open chain and close it again.
            points = [[round(x, 4), round(y, 4)] for x, y in ring]
            reduced = rdp(points[:-1])
            if len(reduced) >= 3:
                rings.append(reduced + [reduced[0]])
        if rings:
            simplified.append(rings)
    provinces.append({'id': feature['properties']['id'], 'name': feature['properties']['nombre'], 'polygons': simplified})

payload = json.dumps(provinces, ensure_ascii=False, separators=(',', ':'))
html = target.read_text(encoding='utf-8')
start, end = '<!-- PROVINCES_BEGIN -->', '<!-- PROVINCES_END -->'
assert html.count(start) == html.count(end) == 1
html = html[:html.index(start) + len(start)] + '\n<script>const PROVINCES=' + payload + ';</script>\n' + html[html.index(end):]
target.write_text(html, encoding='utf-8', newline='\n')
print(f'Embedded {len(provinces)} provinces, {len(payload)} bytes, into {target}')
