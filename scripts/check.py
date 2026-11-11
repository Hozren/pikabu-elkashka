"""Validate the intentionally CSS-only extension using Python's standard library."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / 'extension'
DOMAINS = ['https://pikabu.ru/*', 'https://www.pikabu.ru/*']


def check():
    manifest = json.loads((EXT / 'manifest.json').read_text(encoding='utf-8'))
    assert manifest['manifest_version'] == 3, 'Expected Manifest V3'
    assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']), 'Expected numeric x.y.z version'
    assert all(int(n) <= 65535 for n in manifest['version'].split('.')), 'Version component too large'
    for key in ('permissions', 'host_permissions', 'optional_permissions', 'background', 'update_url'):
        assert not manifest.get(key), f'Unexpected capability: {key}'
    scripts = manifest['content_scripts']
    assert len(scripts) == 1 and scripts[0]['matches'] == DOMAINS
    assert scripts[0]['css'] == ['replacements.css'] and not scripts[0].get('js')
    assert scripts[0]['run_at'] == 'document_start'
    assert manifest['web_accessible_resources'] == [{'resources': ['assets/*.svg'], 'matches': DOMAINS}]
    assert not list(EXT.rglob('*.js')), 'Runtime JavaScript is outside this scope'
    css = (EXT / 'replacements.css').read_text(encoding='utf-8')
    referenced = re.findall(r'url\("chrome-extension://__MSG_@@extension_id__/(assets/[a-z_]+\.svg)"\)', css)
    expected = {f'assets/{name}_{size}.svg' for name in ('poop', 'clown', 'cock') for size in ('m', 's')}
    assert set(referenced) == expected and len(referenced) == 6, 'Expected six packaged assets'
    assert len(re.findall(r'url\(', css)) == 6 and '@import' not in css, 'Unexpected CSS resource'
    for old in ('christmastree', 'skull', 'dove'):
        for size in ('m', 's'):
            assert f'svg.icon--ui-kit__{old}_{size}' in css
    for rel in expected:
        root = ET.parse(EXT / rel).getroot()
        assert root.tag == '{http://www.w3.org/2000/svg}svg' and root.get('viewBox')
        for el in root.iter():
            assert el.tag.split('}')[-1] not in ('script', 'foreignObject', 'image', 'use', 'style')
            for key, val in el.attrib.items():
                assert not key.lower().startswith('on'), 'Event handlers forbidden'
                assert not key.endswith('href'), 'External references forbidden'
                assert not re.search(r'https?:|javascript:', val, re.I), 'Active/external SVG resource'
    for rel in manifest.get('icons', {}).values():
        assert (EXT / rel).is_file(), f'Missing icon: {rel}'
    print('OK: manifest, domain scope, CSS and six local SVG assets')
    return manifest


if __name__ == '__main__':
    check()
