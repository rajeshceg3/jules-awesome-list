#!/usr/bin/env python3
from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[4]
out=ROOT/'artifacts/verification';out.mkdir(parents=True,exist_ok=True)
proof={'scope':'Documentation navigation and prompt formatting on local tracked source, no external link availability or prompt effectiveness claim','passed':False}
try:
 readme=(ROOT/'README.md').read_text();contrib=(ROOT/'contributing.md').read_text()
 headings=re.findall(r'^## (.+)$',readme,re.M)
 def slug(text):return re.sub(r'[^\w\- ]','',text.lower()).replace(' ','-')
 anchors={slug(x) for x in headings};links=re.findall(r'\]\(#([^)]*)\)',readme)
 missing=[x for x in links if x not in anchors]
 local=['assets/jules-readme.png','contributing.md','pull_request_template.md']
 assert all((ROOT/x).is_file() for x in local),'Missing linked document/image'
 assert not missing,'Broken table of contents: '+str(missing)
 assert 'YOUR_REPO' not in readme,'Unresolved repository placeholder'
 prompts=re.findall(r'^- `([^`]+)`',readme,re.M)
 assert len(prompts)>=30 and all(x.startswith('// ') for x in prompts),'Prompt formatting regression'
 assert 'README.md' in contrib and '## How to Contribute' in contrib,'Contribution route missing'
 proof.update(headings=headings,tableOfContentsTargets=links,promptCount=len(prompts),localTargets=local,readmeSha256=hashlib.sha256(readme.encode()).hexdigest(),passed=True)
except Exception as error:proof['failure']=str(error)
finally:
 (out/'documents.json').write_text(json.dumps(proof,indent=2)+'\n');assert (out/'documents.json').exists();print(json.dumps(proof,indent=2))
if not proof['passed']:raise SystemExit(1)
