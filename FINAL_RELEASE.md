# VOLT-FORGE | Round 1 final release

Team StratWise: Shubhra Arora, Jai Kaushik, Sanya Bansal. 1 November 2026.

The final release combines Jai’s V4 corrections at `05adc81` with a Groq-backed public copilot, a rebuilt evidence appendix and two submission designs. The electrical and thermal engine source is unchanged from Jai’s final branch.

- [Live prototype](https://volt-forge-app.vercel.app): demo video, then the real Python engine in the visitor’s browser.
- [Original visual style, final PDF](reports/final_release_v1/VOLT-FORGE_Final_Submission.pdf).
- [Alternative design, final PDF](reports/final_release_v1/VOLT-FORGE_Alternative_Submission.pdf).
- [Analytical appendix workbook](reports/final_release_v1/VOLT-FORGE_Final_Appendix.xlsx).
- [Verification receipt](reports/final_release_v1/verification.json), [browser check](reports/final_release_v1/browser_check.json), [AI checks](reports/final_release_v1/ai_check.json).

## What is verified

The final engine reran all 4,006 frozen cases: zero differing stored fields and zero numerical change across 27,832 compared values. There are 42 refusals and 3,964 calculated cases. All 649 protected configuration/evidence files remain byte-identical. No reserved outcome was decoded.

515 Python tests pass, with 8 known skips; 74 JavaScript tests pass. The public browser completed the Pi example, produced three SVG report charts, exported a ZIP whose 1,201 samples replayed using its bundled source/models, downloaded an editable JSON backup, and reopened that backup as a new design. A real AI edit changed ambient temperature from 23 to 30 C only after review. The old saved test retained 23 C and was marked historical.

Software hashes are platform-dependent because the existing fingerprint uses native path separators. The identical source bytes produce `28c7e5b925453a6a402f056fd636c7c40aac5c5e059199f8be7aec3cfa09c07d` with slash keys on macOS and Jai’s `2437f14ea7f583a9d406ed365b9b920d6aa8a035f6b0f49332dab2b7f553a0d2` with backslash keys. Both digests were reconstructed; historical records were not rewritten.

## What the design result means

Two LG M50T cells are the smallest qualifying parallel arrangement among those tested for the declared 25 W supply-rating scenario, 10 minutes, 23 C and 70% starting charge. The study approximates the load with 8.418 A constant current, calculated from assumed 90% conversion and a 3.3 V floor. It does not measure actual Pi consumption or simulate a converter’s true constant-power response.

The slide holds same-end output routing fixed for its 4/3/2 comparison. The study separately favours opposite-end outputs for the two-cell candidate. Their rows must not be mixed. Temperatures are simulated; costs/masses in the table cover cells only. Two cells have no spare. Board compatibility, physical isolation, charge sharing, sensing and protection need separate physical evidence.

Historical PyBaMM checks passed 15/15 synthetic electrical/heat cases. All 12 comparisons with published measurements missed both voltage and temperature bands: eight measured discharges plus four sensitivity reruns. Current sharing also missed its frozen criterion. These facts cannot be replaced by selected good-looking slices or an energy-balance check. Predictive accuracy remains unestablished.

## Public AI

Groq hosts `openai/gpt-oss-120b`. `GROQ_API_KEY` exists only in Vercel Production. No credential is embedded in the app, workbook or handoff.

A small, curated retrieval layer selects up to three source-labelled engineering passages and sends them with bounded saved-result/current-design context. This is retrieval over project evidence, not a newly trained model. JSON schema limits action types and stable component IDs; the existing Python proposal validator and explicit review govern edits. New drafts can open automatically, as in the existing product contract. The solver never depends on AI availability.

Real-provider checks covered explanation, limitations, ambient edit, new-draft construction and refusal to fabricate results. One browser construction response initially used an invalid cell target and was rejected by the product; target IDs and construction instructions were then tightened. Bounded tests do not establish general reasoning correctness. Free-provider quotas, outages and mistakes remain possible; manual simulation stays usable. Per-instance rate limiting is best-effort, not a distributed abuse-control service.

## Appendix logic

The six exhibits answer six challenges to the slide: controlled design trade-off; sizing derivation and rejected options; parameter/data pedigree; numerical versus measured accuracy; sensitivities and reversal conditions; commercial drivers, costs and adoption sensitivity. Sources sit beside the analysis. Commercial calculations use live formulas with expandable calculation detail. All formulas were recalculated and checked for errors.

Students are free. ₹50,000/year per lab and ₹5 lakh/year per team (up to five seats) are untested planning prices. At 130 labs the scenario earns ₹65 lakh/year. The legacy full-product estimate is ₹35.38 crore; its stage-one allocation is ₹10.97 crore. At the stated five-year gross-recovery assumption, 31 additional team customers are needed after lab revenue, before post-build running/support/sales costs. This is arithmetic, not evidence of commercial feasibility. Do not imply that the present prototype cost those amounts.

## Submission actions

1. Review the two PDF designs and select exactly one. Both retain the official team cover, contain one content slide, and are below 10 MB.
2. Replace the old linked Google workbook with the final Desktop XLSX. Preserve the existing spreadsheet ID by importing into that spreadsheet and choosing Replace spreadsheet. Confirm public view access in a signed-out window. This import remains user-owned.
3. Check the prototype and appendix links once in a signed-out browser, then submit the selected PDF through the portal before 1 November 2026, 23:59 IST. No portal submission was performed by the agent.

Hardware work, customer trials and price validation remain future work. They have not been represented as completed or imposed as additional Round 1 submission requirements.
