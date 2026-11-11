"""Build a reproducible installable ZIP. No network and no external dependencies."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import hashlib
from check import check, ROOT, EXT


def build():
    manifest = check()
    dest = ROOT / 'dist'
    dest.mkdir(exist_ok=True)
    archive = dest / f'yolkashka-chrome-{manifest["version"]}.zip'
    # Explicit allowlist: never package research, credentials or arbitrary extension files.
    files = ['manifest.json', 'replacements.css', 'README.txt']
    files += sorted(p.relative_to(EXT).as_posix() for p in (EXT / 'assets').glob('*.svg'))
    files += sorted(set(manifest.get('icons', {}).values()))
    with ZipFile(archive, 'w', ZIP_DEFLATED) as z:
        for name in sorted(set(files)):
            path = Path(name)
            if path.is_absolute() or '..' in path.parts:
                raise ValueError(f'Invalid archive path: {name}')
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, (EXT / name).read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix('.zip.sha256').write_text(f'{digest}  {archive.name}\n', encoding='ascii')
    print(f'Built {archive.name}: {archive.stat().st_size} bytes; SHA256 {digest}')


if __name__ == '__main__':
    build()
