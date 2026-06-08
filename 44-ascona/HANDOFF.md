# Handoff — Ascona 2026 talk build

For a fresh agent continuing this work. Read this, then `OUTLINE.md`, then skim `talk.html`.

## What this is

Preparing Navish Wadhwa's talk for **Ascona 2026, "Mechanobiology of Infection"** — **25 min talk + 5 min Q&A**. Single topic: **Seiga Yanagisawa's experimental evolution project** on flagellar motility. Audience: biophysics / microbial mechanobiology.

**Central thesis:** bacteria evolve better migration through structured environments by tuning the flagellum as a *mechanical system*, not by swimming faster. Two separable routes — (1) flagellar **number**, (2) filament **shape switching**. Headline surprise: a single flagellin mutation (A438V) makes cells *slower in liquid* but *better in agar*.

## The three files (all in `44-ascona/`)

- **`OUTLINE.md`** — the agreed, fully-reviewed slide-by-slide plan. **Source of truth.** 19 main slides (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11a, 11b, 11c, 12–19) + supplements S1–S3. Each entry has header, content bullets, and an **Assets** line. Has a **"Figure status"** section mapping every panel to a real file: already-rendered / needs-rendering / not-in-repo. Has **"Open framing notes"** with the scientific constraints below.
- **`talk.html`** — a complete reference draft of the deck (user approved it: "pretty good"). Clean reveal.js markup with `.placeholder` boxes for pending figures. **Use as the design/markup reference** when building each slide. Not the deliverable.
- **`index.html`** — the **canonical deck under construction**. Everything ultimately goes here. This is what gets presented. Built by transforming the old copied multi-part talk into the new single-topic deck, one slide at a time.

## Working cadence (important)

- **One slide at a time.** The user reviews/approves each change before moving on. Do not bulk-rewrite `index.html`.
- The user **edits files directly** and leaves **inline comments** (often prefixed `--` or `---`). When they do: **respond to every comment in chat first, get approval, then apply** — don't silently edit.
- **Verify against the project folder before asserting any data exists.** The user repeatedly (and correctly) pushed back on claims about what data/plots exist. Check, don't assume.
- Plain, literal language; claim-first (see global `~/.claude/CLAUDE.md`). Never fabricate citations or data.

## Progress so far (in `index.html`)

Done (new content):
- Title (abstract title; byline just "Navish Wadhwa")
- **Seiga credit slide** ("This work was led by Seiga Yanagisawa") — photo placeholder, needs `figures/people/seiga.jpg`
- "Bacteria don't live in buffer" (infection line intentionally omitted — NW says it verbally)
- "In liquid, bacteria swim by rotating helical flagella" + fragment question "What tunes motility in viscous, structured environments?"
- "Reversing flagellar rotation changes swimming direction" (run-tumble) — **kept**

Deleted: old physics primer (Reynolds/scallop/two-strategies), the e-coli "Flagella power" slide, the "nanoscale rotary motor" slide, a stray "Flagellar number and geometry" divider, a duplicate buffer slide. Renamed all "Directed evolution" → "Experimental evolution".

## What's left in `index.html` (current slide list, by line as of handoff)

The body below run-tumble is still the **old Part II content** (headers renamed) plus old Part III + a motor appendix that must go. Reconcile against `OUTLINE.md`:

- "Experimental evolution selects…" → OUTLINE slide 4 ✓ (but rebuild from Seiga's better images)
- "Experimental evolution rapidly enhances…" (dee-20) → OUTLINE slide 5: needs the staged build (halo-vs-round, hypermutator overlay, frozen-stock). dee-20 stays as the **visual lead-in**.
- "Swimming speed … does not predict motility" → OUTLINE slide 8 (the puzzle): swap in `swim-speed-ficoll-summary.pdf` heatmap.
- "Selection drives morphological changes" → slide 9 ✓
- **"Mutant A has more flagella"** → slide 10: **rename "Mutant A" → "*mutL* 20B"**
- "More flagella improve motility" (×2 slides) → slides 11a/11b: add flagella-vs-IPTG premise panel, IPTG×Ficoll optimum + swim-speed, Sourjik ack, confirm strain number. Add **11c transition divider**.
- "Selection drives higher flagellar curvature" → slide 12 ✓
- "A single flagellin mutation increases curvature and motility" → slide 13; then **add the inversion (slide 14)**: WT-vs-A438V halo (1.7×→3.4×) + slower-at-every-viscosity.
- **Insert polymorphism primer (slide 15, `wt-twist.png`) here**, after the inversion, before the switch.
- "Mutant filaments undergo dramatic shape changes" → becomes the switch (slide 16, `mutant-twist.png` + a rotating gif).
- "A structural switch within the flagellar filament" (×3) → consolidate to slide 17 (β-hairpin design rules + Curly-locked V148L necessity). Move N441S → **S1**, V148I → **S2**.
- **"Part II summary"** → DELETE (no Route 2 summary; folds into slide 18).
- **Part III surface motility / swashing (all ~15 slides) → DELETE** (off-abstract).
- "What I told you today" → replace with new two-route **summary (slide 18)**.
- "Acknowledgements" → slide 19: highlight Seiga, **add Victor Sourjik (Ptac strain)**, trim to relevant people.
- **Motor appendix (bidirectional rotation, stator remodeling, electrorotation, torque model) + leftover surfactant/swashing slides → DELETE.**
- **Add supplements S1 (N441S), S2 (V148I), S3 (run-tumble kinematics)** per OUTLINE.

## Scientific constraints (do not re-introduce these errors)

- **"Experimental evolution," never "directed evolution"** (the latter = protein engineering to this audience). Note: image *paths* are `figures/directed-evolution/…` — leave those.
- **N441S** is a near-twin of A438V that *also* performs the rotation-dependent switch but gives **no** phenotype; the only known difference is slightly different twist (Δτ ≈ 3.7 vs 4.7 µm⁻¹). It is **NOT** a "curvature-without-switching" control. Kept **out of the main story** → supplement S1.
- **C11A has slightly *fewer* flagella than WT** (not "indistinguishable"). Keep *mutL* 20B (number route) and C11A (shape route) distinct.
- Name mutants: **mutL 20B, A438V, V148L** — not "Mutant A/B".
- **Infection framing** lives on slide 2 and the close only — not on the slide-3 question.
- **Strain number ambiguity:** project uses both **VS1638** and **VS1683** for the Ptac::flhDC strain. Confirm with NW before labeling slides.
- **Curly-locked / N87K ref:** *E. coli* ATCC10798, **Kinosita et al., Sci. Rep. 2020**, DOI 10.1038/s41598-020-72429-1 (cited in the project manuscript as `Kinosita2020SciRep`).
- **IPTG optimum honesty:** peak shift is clean 0%→5% Ficoll; at 10% it's a plateau + magnitude collapse (38→28→12 cm²). Phrase as "optimum drops with viscosity, and at high viscosity the benefit collapses."
- WT filaments **already** switch (Normal during runs ↔ Semi-coiled/Curly during tumbles); A438V is an *evolved exaggeration of a switch cells already use* — use this framing on the primer (slide 15).

## External dependencies (not in repo — will block those slides)

- **WGS figure** (slide 7): no processed table/figure or raw sequencing in the project folder — only manuscript prose. Awaiting NW's postdoc; else cut.
- **Frozen-stock heritability** panel (slide 5, panel 3): Seiga has it; not yet in repo.
- **Slide 4 high-quality selection images:** locate Seiga's source.
- **Seiga photo** for the credit slide: drop at `figures/people/seiga.jpg`.

## Figures: render status (project = `C:\Users\nwadhwa3\ASU Dropbox\Navish Wadhwa\ASU\Projects\2026-Yanagisawa-Flagellar`)

Already rendered as PDFs (need PDF→PNG + wire into deck): `halo-area-vs-selection-round.pdf` (slide 5), `growth-curves/growth-curves-and-rates.pdf` (slide 6), `swim-speed-ficoll-summary.pdf` (slide 8), `halo-area-vs-iptg_vs1683.pdf` + heatmap/peak-halo (slide 11b), `manuscript/figures/supp/run-tumble-vs1638-*.pdf` (S3).

Need rendering from curated CSVs: flagella-vs-IPTG (slide 11a; script `2026-05-06 Number of flagella per cell - VS1638 …`), slide-14 WT-vs-A438V halo (re-render `halo-area_flic-mutants` excluding N441S) + swim (`2025-03-26_fliC_WT_vs_A438V_vs_N441S`), VS1683 swim-vs-IPTG (`2026-02-16_VS1683_swim_speed`), S1 N441S, S2 β-hairpin (`2025-09-19_fliC_beta_hairpin_mutants_swimming`).

Figure-script conventions (from project `SESSION_HANDOFF.md`): project-relative paths via `Path(__file__).parents[1]`; `pdf.fonttype=42`, `ps.fonttype=42`, `font.family='Arial'`, 7pt; outputs to `outputs/figure-panels/`. Color palette: gray `#333333` = WT/control; orange `#D55E00` = elevated-phenotype (A438V); blue `#0072B2` = neutral comparator; sequential blues for Ficoll. n=3: use min–max bands or mean±SD, no SEM, no significance stars.

## Technical notes

- reveal.js deck; relative paths `../reveal.js` and `../figures` (both `talk.html` and `index.html` sit in `44-ascona/`, so paths resolve identically).
- `.placeholder` CSS is already in `index.html`'s `<style>` block; use `class="placeholder"` boxes for pending figures (pattern in `talk.html`).
- **`index.html` has inconsistent legacy indentation and real trailing whitespace.** When deleting/replacing old blocks, **re-read the exact lines first** to capture whitespace, or expect Edit match failures and retry.

## Open decisions awaiting NW

- **Run-tumble ordering:** it currently sits *between* the pivot question and the experiment, softening the pivot. Offered to move it before the swim/question slide or drop the question off the swim slide. Unresolved.
- Whether the WGS slide (7) stays as placeholder or is cut.
- Strain number VS1638 vs VS1683.
