"""Preserve the approved slide design, simplify product views, and print a readable traced 4/3/2 table."""
from pathlib import Path
import json
import shutil
import sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/final_release_v1/slide';OUT.mkdir(parents=True,exist_ok=True)
for name in ['logo_teliport.png','logo_tata.png']:
 (OUT/'assets').mkdir(exist_ok=True);shutil.copy(ROOT/'reports/slide_v4/assets'/name,OUT/'assets'/name)
summary=json.loads((ROOT/'reports/design_study_v2/run1/summary.json').read_text())
release_path=ROOT/'reports/final_release_v1/verification.json'
release=json.loads(release_path.read_text()) if release_path.exists() else {}
rows=[]
for count in [4,3,2]:
 d=next(x for x in summary['designs'] if x['count']==count and x['option']=='baseline');w=d['worst_required']
 rows.append(f"<tr class=\"{'pick' if count==2 else ''}\"><td>{count} cells</td><td>{d['required_passed']}/{d['required_cases']}</td><td>{w['highest_cell_current_A']:.2f} A</td><td>{w['highest_temperature_C']:.1f} °C</td><td>{d['cell_mass_g']:.0f} g</td><td>₹{d['cell_cost_inr']:,.0f}</td></tr>")
repeat='Rechecked on the final engine.' if release.get('study_complete') else 'Frozen study; final rerun pending.'
html='''<!doctype html><html><head><meta charset="utf-8"><title>VOLT-FORGE final slide</title>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet"><style>
*{box-sizing:border-box;margin:0;padding:0}html,body{width:1920px;height:1080px;background:#fff;font-family:Manrope,Arial,sans-serif;color:#10202F;overflow:hidden;-webkit-font-smoothing:antialiased}
.slide{position:relative;width:1920px;height:1080px}.logo-left{position:absolute;left:6px;top:0;height:104px}.logo-right{position:absolute;right:6px;top:0;height:100px}
header{position:absolute;left:0;right:0;top:12px;text-align:center}h1{font-size:52px;font-weight:800;letter-spacing:-1.4px;line-height:1.08}h1 em{font-style:normal;color:#0091CC}header p{font-size:23px;font-weight:500;color:#566575;margin-top:4px}
.col{position:absolute;top:118px;width:376px;height:872px;display:flex;flex-direction:column;justify-content:space-between}.left{left:36px}.right{right:36px}
.c h2,.proto h2{font-size:16px;font-weight:800;color:#0091CC;letter-spacing:.3px;text-transform:uppercase}.c h3{font-size:27px;font-weight:800;letter-spacing:-.5px;line-height:1.18;margin-top:5px;text-wrap:balance}.c p{font-size:20px;font-weight:500;line-height:1.42;color:#3F4E5D;margin-top:7px}.c p b{font-weight:800;color:#10202F}
.proto{position:absolute;left:436px;top:118px;width:1048px;height:872px}.proto h2{text-align:center}.proto h2 span{color:#566575;font-weight:600;text-transform:none;margin-left:10px}.proto a,.applink a{color:#0B6FA8;font-weight:800;text-decoration:none}
.shot{position:absolute;left:0;width:1048px;border:2px solid #D3DFE8;border-radius:12px;overflow:hidden;background:#fff;display:flex;justify-content:center}.shot img{display:block;max-width:100%;height:100%;object-fit:contain}.one{top:30px;height:270px}.two{top:349px;height:168px}
.caption{position:absolute;left:0;right:0;text-align:center;font-size:18px;font-weight:500;line-height:1.3;color:#3F4E5D}.caption b{font-weight:800;color:#10202F}.capone{top:310px}.captwo{top:526px}
.study{position:absolute;top:559px;left:0;width:1048px;border-collapse:collapse;font-size:21px;text-align:center;font-variant-numeric:tabular-nums}.study th{background:#0B6FA8;color:white;font-size:18px;font-weight:800;line-height:1.2;height:49px}.study td{height:42px;border-bottom:1px solid #D3DFE8;font-weight:600}.study th:first-child,.study td:first-child{text-align:left;padding-left:15px}.study .pick{background:#E3F2FA}.study .pick td{font-weight:800}.tablenote{position:absolute;top:741px;font-size:16px;color:#566575;line-height:1.3;text-align:center;width:100%}
.proofs{position:absolute;top:785px;left:0;right:0;display:grid;grid-template-columns:repeat(3,1fr);gap:25px}.proofs div{font-size:17px;font-weight:500;line-height:1.35;color:#3F4E5D}.proofs b{font-weight:800;color:#10202F}.applink{position:absolute;top:865px;text-align:center;width:100%;font-size:17px;color:#566575}
.market{display:flex;align-items:center;gap:14px;margin-top:9px}.market svg{flex:none}.market ul{list-style:none}.market li{font-size:16px;color:#3F4E5D;line-height:1.25;margin-bottom:9px}.market b{font-size:21px;font-weight:800;color:#10202F}.price{font-size:32px;color:#0B6FA8;font-weight:800;margin-top:10px}
footer{position:absolute;left:36px;right:36px;bottom:16px;height:52px;border-radius:26px;background:#0B6FA8;color:white;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:600}
</style></head><body><div class="slide">
<img class="logo-left" src="assets/logo_teliport.png"><img class="logo-right" src="assets/logo_tata.png">
<header><h1>Test a battery <em>before you build it</em></h1><p>VOLT-FORGE connects your battery design decisions to what they physically change</p></header>
<section class="col left">
<div class="c"><h2>Problem understanding</h2><h3>One change affects the whole battery</h3><p>A Pi 5 gateway needs a <b>10-minute backup</b>. Fewer cells cost less, but each works harder. Wiring, cell variation and cooling change the answer together. We model one small cell group; ageing and packaging come later.</p></div>
<div class="c"><h2>Desirability</h2><h3>Make the trade-off visible</h3><p>A student can change a circuit and explain what happens. An engineer can compare candidates before a bench test. Build, test, inspect the exact values and export the evidence, <b>in one workspace</b>.</p></div>
<div class="c"><h2>Technical feasibility</h2><h3>How few cells can do this job?</h3><p><b>Two cells passed 33/33</b> required simulations, including weak-cell cases; one cell was refused. The browser solves current and cell heating together. The table shows the trade-off against 3 and 4 cells. Board limits still need checking.</p></div>
</section>
<section class="proto"><h2>Prototype &amp; evidence<span>Test it out: <a id="site-link" href="https://volt-forge-app.vercel.app">volt-forge-app.vercel.app</a></span></h2>
<div class="shot one"><img src="assets/circuit.png"></div><p class="caption capone"><b>Build it.</b> Edit the actual circuit, its cells and the assumptions the solver uses.</p>
<div class="shot two"><img src="assets/compare.png"></div><p class="caption captwo"><b>Compare it.</b> Same job, fewer cells: lower cell cost and mass, less electrical margin.</p>
<table class="study"><thead><tr><th>Parallel design</th><th>Required<br>cases</th><th>Worst cell<br>current</th><th>Worst cell<br>temperature</th><th>Cell mass</th><th>Cell cost</th></tr></thead><tbody>__ROWS__</tbody></table>
<p class="tablenote">Frozen study: same-end outputs; mismatch, thermal and converter sensitivities. Case counts vary by cell positions.<br>Temperatures are simulated. Cost and mass cover cells only.</p>
<div class="proofs"><div><b>4,006 simulated cases.</b><br>13 design variants. __REPEAT__</div><div><b>54 published experiments.</b><br>194 files checksum-verified; 2 module records compared.</div><div><b>15/15 numerical checks.</b><br>Electrical and heat calculations checked against PyBaMM.</div></div>
<p class="applink">Assumptions, finance and sources: <a id="appendix-link" href="https://volt-forge-app.vercel.app/appendix">volt-forge-app.vercel.app/appendix</a></p>
</section>
<section class="col right">
<div class="c"><h2>Engineering quality</h2><h3>Know what the evidence supports</h3><p>Numerical checks passed. <b>All 12 comparisons with published measurements missed</b> voltage and temperature bands. Predictive accuracy remains unestablished. Monitoring and virtual cutoffs support investigation; physical board protection is unverified.</p></div>
<div class="c"><h2>Innovation</h2><h3>Change it, then challenge it</h3><p><b>Find the smallest design</b> tests each size at normal conditions. Pressure tests show where it stops working. Every saved result keeps its inputs, model and software versions for repeatable comparisons.</p></div>
<div class="c"><h2>Business viability</h2><h3>Start with teaching labs</h3><div class="market"><svg width="110" height="110" viewBox="0 0 176 176"><circle cx="88" cy="88" r="88" fill="#D5ECF8"/><circle cx="88" cy="118" r="58" fill="#59B9E6"/><circle cx="88" cy="146" r="30" fill="#0B6FA8"/></svg><ul><li><b>41.3 lakh</b> engineering students</li><li><b>15.6 lakh</b> in three target disciplines (AISHE 2021–22)</li><li><b>130 labs</b> at 5% assumed reach</li></ul></div><p>Students free. Labs <b>₹50,000/year</b>; teams <b>₹5 lakh/year</b>. Proposed prices and adoption are untested.</p></div>
</section>
<footer>25 W supply-rating scenario · 10 min · 23 °C · 70% charge · assumed 90% converter and 3.3 V floor · 8.42 A proxy</footer>
</div></body></html>'''
html=html.replace('__ROWS__',''.join(rows)).replace('__REPEAT__',repeat)
(OUT/'slide.html').write_text(html)
print(OUT/'slide.html')
