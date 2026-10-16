"""Check local links in the fork's root guides, without installing the site."""
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

root=Path(__file__).resolve().parents[2]
tracked=set(subprocess.check_output(['git','ls-files'],cwd=root,text=True).splitlines())
for name in ['README.md','FORK_NOTES.md']:
    path=root/name
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',path.read_text()):
        url=urlsplit(target)
        if url.scheme or target.startswith('#'):continue
        destination=(path.parent/unquote(url.path)).resolve()
        relative=destination.relative_to(root).as_posix() if destination.is_relative_to(root) else None
        present=relative is not None and (destination.exists() or relative in tracked or any(p.startswith(relative.rstrip('/')+'/') for p in tracked))
        if not present:
            raise SystemExit(f'{name}: missing local link {target}')
print('Fork guide links verified.')
