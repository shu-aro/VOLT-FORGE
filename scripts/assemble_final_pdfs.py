"""Pair the unchanged official team cover with each newly rendered content page."""
from pathlib import Path
import json
from pypdf import PdfReader, PdfWriter
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'reports/final_release_v1';SLIDE=OUT/'slide'
cover=SLIDE/'cover.pdf'
# Use the retained official cover from the last released two-page PDF.
reader=PdfReader(cover);first=reader.pages[0]
assert all(x in first.extract_text() for x in ['StratWise','Shubhra','Jai','Sanya'])
checks={}
for variant,name in [('main','VOLT-FORGE_Final_Submission.pdf'),('alternative','VOLT-FORGE_Alternative_Submission.pdf')]:
 content=PdfReader(SLIDE/f'{variant}-content.pdf');assert len(content.pages)==1
 page=content.pages[0];page.scale_to(float(first.mediabox.width),float(first.mediabox.height))
 writer=PdfWriter();writer.add_page(first);writer.add_page(page)
 writer.add_metadata({'/Title':'VOLT-FORGE | Team StratWise | Teliport S4 Case Study 2','/Author':'Shubhra Arora, Jai Kaushik, Sanya Bansal','/Subject':'Round 1 submission; simulation prototype and supporting evidence'})
 target=OUT/name
 with target.open('wb') as f:writer.write(f)
 final=PdfReader(target);text=final.pages[1].extract_text();assert '33/33' in text and '12' in text and '5' in text
 links=[]
 for ref in final.pages[1].get('/Annots',[]):
  a=ref.get_object();uri=a.get('/A',{}).get('/URI');rect=[float(x) for x in a.get('/Rect',[])];links.append(dict(uri=uri,rect=rect))
  assert len(rect)==4 and min(rect)>=0 and rect[2]<=float(first.mediabox.width)+1 and rect[3]<=float(first.mediabox.height)+1
 assert any(x['uri'].rstrip('/')=='https://volt-forge-app.vercel.app' for x in links)
 assert any(x['uri']=='https://volt-forge-app.vercel.app/appendix' for x in links)
 assert target.stat().st_size<10_000_000
 checks[name]=dict(pages=len(final.pages),bytes=target.stat().st_size,links=links,page_size=[float(first.mediabox.width),float(first.mediabox.height)],searchable_content=True)
(OUT/'pdf_check.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2))
