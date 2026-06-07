# Ascona Talk Outline — Experimental Evolution of Flagellar Motility

**Talk:** Ascona 2026, "Mechanobiology of Infection"
**Length:** 25 min talk + 5 min Q&A
**Scope:** Single topic — Seiga Yanagisawa's experimental evolution project
**Audience:** Biophysics / microbial mechanobiology
**Mutant naming (NW decision, 2026-06-07):** The deck keeps the generic display names **Mutant A = *mutL* 20B** (number route) and **Mutant B = *mutL* C11A** (shape route). Do NOT rename these to their real line designations — the figures are already labeled "Mutant A"/"Mutant B", and NW has chosen to present them this way. Flagellin point mutants (A438V, N441S, V148L) keep their residue names. (This reverses the earlier "use real designations" instruction.)

**Submitted abstract title:** *Experimental evolution reveals distinct flagellar strategies for enhanced motility in complex environments*

**Central thesis:** Bacteria evolve better migration through structured environments by tuning the flagellar apparatus as a *mechanical system* — not by simply swimming faster. Two separable routes: (1) flagellar **number**, (2) flagellar filament **shape switching**. The headline surprise: a single flagellin mutation makes cells *slower in liquid* but *better in agar*.

---

## Part 0 — Setup and infection frame

### Slide 1 — Title
- **Header:** Experimental evolution reveals distinct flagellar strategies for enhanced motility in complex environments
- Seiga Yanagisawa named prominently; Wadhwa lab, ASU
- Subtitle/framing tie to conference theme: pathogens navigating structured host environments
- **Assets:** reuse title-slide layout from draft; update title text

### Slide 2 — Bacteria navigate structured environments
- **Header/message:** Bacteria don't live in buffer — their world is viscous, crowded, and structured
- Host tissue / mucus / gut, plus soil, pond, pipes
- **Infection frame (state explicitly here):** "For a pathogen, these structured environments are the host — mucus, tissue, the gut it must move through to establish infection." This is where the infection theme lives (reprised at the close, slide 18).
- **Assets:** reuse soil/pond/gut/pipe images

### Slide 3 — Flagella power motility — but how is it tuned?
- **Header/message:** Bacteria swim by rotating helical flagella — but how do they tune motility in structured environments?
- **Spoken framing (NW):** "We understand how bacteria move through liquid; we understand much less about how they move through viscous, structured environments like host tissue. What factors are important for tuning motility in such environments?"
- Quick visual: flagellar bundle rotates → propulsion (keep physics minimal; this audience knows low-Re)
- Plant the central question that the talk answers
- **Assets:** reuse fluo-bundle.gif + swimming schematic

---

## Part 1 — The experiment, the controls, and the puzzle

### Slide 4 — Experimental evolution selects for soft-agar motility
- **Header/message:** Experimental evolution selects for enhanced motility in soft agar
- Serial soft-agar selection: inoculate → halo expands → pick the leading edge → transfer
- Parallel WT and Δ*mutL* (hypermutator) backgrounds
- **Note:** header "Experimental evolution" (not "Directed evolution")
- **Assets:** REBUILD from Seiga's higher-quality selection images (NW to point to source; or I search the project). Current dee-1…5 build is a placeholder.

### Slide 5 — Motility is rapidly and heritably enhanced
- **Header/message:** Motility rapidly improves over selection rounds, in both backgrounds, and is heritable
- **Open with the dee-20 plate collage** as a visual demonstration of experimental evolution in action (20 rounds of expanding halos) — then show the quantitative data
- **Then build as a 3-step animation:**
  1. Halo radius vs selection round for all WT selection lines (monotonic increase)
  2. Overlay the Δ*mutL* hypermutator lines — gain more, and faster
  3. Heritability: frozen-stock re-inoculation retains enlarged halos
- **Assets:**
  - Visual lead-in: dee-20 plate collage
  - Panels 1–2: `halo-area-vs-selection-round.pdf` (+ traces-only, mean±SD variants) already rendered from `motility-halo-area_directed-evolution.csv` (120 rows, both backgrounds) — ready to render as a staged build
  - Panel 3 (frozen-stock): **data not yet in project folder** — Seiga has it; needs to be added before rendering

### Slide 6 — Control: it's not just faster growth  *(NEW)*
- **Header/message:** Evolved lines don't grow faster in liquid — the bigger halos aren't a growth-rate artifact
- Preempts the Fisher–Kolmogorov objection (halo speed ~ √(growth × motility))
- Liquid TB growth curves: hypermutator-derived lines match or grow *slower* than ancestor; motility gains came with a fitness cost in liquid
- Honest scope: rules out a uniform shift in intrinsic growth rate (not in-agar growth-coupled physics)
- **Assets:** `outputs/figure-panels/growth-curves/growth-curves-and-rates.pdf` already rendered — copy into deck

### Slide 7 — Genetic basis: selection targets the flagellar system  *(PLACEHOLDER)*
- **Header/message:** Whole-genome sequencing shows selection repeatedly and independently hits the flagellar system
- Two routes visible in the genetics: *flhDC* promoter mutations (→ number route); *fliC* point mutations A438V / N441S (→ shape route); plus chemotaxis genes
- Bridges evolution → mechanism; motivates dissecting each route
- **Assets / status:** **No WGS figure, table, or raw sequencing data exists in the project folder** — only prose in the manuscript. Cannot build a real panel today. Options: (a) placeholder until postdoc supplies a processed mutation table; (b) a simple text/schematic listing the two routes (*flhDC* promoter + *fliC*). If neither lands in time, **cut** — plasmid complementation carries the causal claim.

### Slide 8 — The puzzle: liquid speed ≠ structured-environment motility
- **Header/message:** Swimming speed in liquid does not predict motility in structured environments
- Some evolved lines swim *slower* than the ancestor in liquid yet make *larger* halos (notably *mutL* C11A); others (20B) swim faster — so speed and halo size don't track
- This is the hook the rest of the talk resolves — twice (number, then shape)
- **Assets:** upgrade to `swim-speed-ficoll-summary.pdf` — a heatmap of mean speed (normalized to WT ancestor) for WT ancestor + *mutL* C11A + *mutL* 20A/20B/20C across the **full 0–35% Ficoll series**, with three representative single-cell distributions (WT, 20B, C11A) at 10% Ficoll. 20B reads warm (faster), C11A reads cool (slower) — yet both make bigger halos: that contrast *is* the puzzle. Stronger than the current 0%-only two-line slide. Optionally trim to WT/20B/C11A; keeping 20A/20C shows reproducibility. (Already rendered.)

---

## Part 2 — Route 1: flagellar number

### Slide 9 — Selection drives morphological change
- **Header/message:** Selection changes flagellar morphology
- TEM shows evolved cells differ in flagellar number and filament shape — bridges into the two routes
- **Assets:** reuse em.png

### Slide 10 — Mutant A has more flagella
- **Header/message:** Mutant A (*mutL* 20B) carries ~2× as many flagella as the ancestor
- TEM counts (two-Poisson mixture fits); Mutant A ≈ 2× WT (figure shows means 6.0 vs 3.2)
- **Caution:** keep Mutant A / *mutL* 20B (number route) distinct from Mutant B / *mutL* C11A (shape route); do not claim C11A is "indistinguishable from WT" — project data show C11A actually has slightly *fewer* flagella
- **Naming:** display as "Mutant A" per NW (see naming note at top); figures already labeled "Mutant A". No caption needed — header carries it.
- **Status:** built in index.html; slide complete.
- **Assets:** reuse wt-mutantA-em + flagella-counts

### Slide 11a — More flagella improve migration
- **Header/message:** Increasing flagellar number is sufficient to improve soft-agar motility
- Inducible *Ptac::flhDC*: IPTG titrates flagellar number, ~1–18 per cell
- **Premise panel (ADD):** flagella per cell vs [IPTG] — shows IPTG actually tunes flagellar number, which licenses the inducible-strain argument. Put this *before* the halo result: "IPTG tunes flagellar number → more flagella give bigger halos."
- More flagella → faster runs and straighter swimming (smaller post-tumble reorientation angle), bigger halos — **state the kinematics in words**; run-and-tumble panel held as backup (S3). Promote S3 to an inset only if making the explicit "inducible strain reproduces the 20B evolved kinematic signature" argument.
- **Acknowledge Victor Sourjik** for the *Ptac::flhDC* strain (here and on the acknowledgements slide)
- **Strain-number flag:** the project uses both **VS1638** and **VS1683** for this strain (e.g. flagella/run-tumble scripts say VS1638; halo/swim folders say VS1683). Confirm which is correct before labeling slides.
- **Assets:** IPTG-sketch + halo-vs-IPTG; ADD flagella-vs-IPTG (script `2026-05-06 Number of flagella per cell - VS1638 strain ...`, needs rendering)

### Slide 11b — But the optimum is viscosity-dependent — and it's not a speed effect  *(NEW figures)*
- **Header/message:** The optimal flagellar number depends on viscosity, and the high-viscosity cost is not a swimming-speed effect
- Halo across IPTG × Ficoll: peak halo shifts to *lower* induction as viscosity rises; at high viscosity the benefit collapses
- Swim speed across IPTG × Ficoll: speed *saturates* (plateaus) with induction — so the halo decline at high IPTG cannot be a speed effect → a structured-environment-specific cost of too many flagella
- **Makes Route 1 a second instance of the central thesis** (liquid speed ≠ structured motility)
- **Honesty caveat (from project session notes):** "optimum shifts lower with viscosity" is statistically clean 0%→5% Ficoll; at 10% it is a plateau + magnitude collapse (38→28→12 cm²), not a clean peak shift. Phrase as "optimum drops with viscosity, and at high viscosity the benefit collapses."
- **Assets:** halo — `halo-area-vs-iptg_vs1683.pdf` (+ `_heatmap`, `_peak-halo`) already rendered from `motility-halo-area_vs1683.csv`; swim speed — data exists (`2026-02-16_VS1683_swim_speed`), needs rendering

### Slide 11c — Transition divider  *(NEW, lightweight)*
- **Header/message:** More flagella help, with a viscosity-tuned optimum — but that's only one of two routes
- One line; signposts the move from the number route to the shape route. Not a full content slide.

---

## Part 3 — Route 2: filament shape switching

### Slide 12 — Selection drives higher filament curvature
- **Header/message:** A second route: selection drives higher filament curvature
- TEM: evolved (C11A-type) filaments are more curved than WT (κ ≈ 2.0–2.5 vs ≈ 1.1 µm⁻¹)
- This line does *not* have more flagella — a different mechanical solution
- **Assets:** reuse wt-mutantB

### Slide 13 — A single FliC mutation is sufficient
- **Header/message:** A single flagellin point mutation, A438V, raises curvature and enlarges halos
- Plasmid complementation in Δ*fliC*: A438V reproduces the curved-filament phenotype and the larger halos; WT *fliC* does not
- Isolates one residue as causal (clean, independent of evolved genetic background)
- **Assets:** reuse wt-mutantB-plasmid build

### Slide 14 — The inversion
- **Header/message:** A438V cells swim *slower* in liquid yet migrate *better* in agar — and the advantage grows with viscosity
- Halo: A438V ≈ 1.7× WT at 0% Ficoll, ≈ 3.4× WT at 10% Ficoll (advantage grows with viscosity)
- Swim speed: A438V slower than WT *fliC* at every viscosity
- The central surprise of the talk, stated plainly
- **Keep N441S out of the main story** — show WT vs A438V only
- **Assets:** halo — re-render WT-vs-A438V only from `halo-area_flic-mutants` data (the rendered PDF currently includes N441S); swim speed — render WT vs A438V from `2025-03-26_fliC_WT_vs_A438V_vs_N441S` (0–35% Ficoll series), N441S excluded

### Slide 15 — Primer: the polymorphic landscape
- **Header/message:** Flagellar filaments are polymorphic — and shape switching is already part of normal motility
- The twist (τ) landscape: L-straight, f1, Normal, Coiled (left-handed) | Semi-coiled, Curly I, Curly II … R-straight (right-handed)
- WT *fliC* sits at Normal
- **Key framing:** polymorphic transitions aren't exotic — WT filaments already switch from Normal (CCW run) to Semi-coiled/Curly I (CW tumble) to unbundle. So A438V is an **evolved exaggeration of a switch cells already use**, not a new trick.
- **Placed here deliberately** (after the inversion) so it arrives as the answer-key to the puzzle and sets up the mechanism
- **Assets:** reuse wt-twist.png (the existing slide-31 sketch works as the primer)

### Slide 16 — The switch
- **Header/message:** A438V is a rotation-driven shape switch
- mutant-twist: A438V sits at Semi-coiled at rest → jumps to Normal/f1 during rotation → snaps back when rotation stops/reverses
- **Assets:** reuse mutant-twist.png + one resting/rotating gif for the visceral effect
- (Dropped the proximal→distal propagation detail — not visible in the videos)

### Slide 17 — A programmable switch: design rules at the β-hairpin
- **Header/message:** Mutations at the flagellin β-hairpin interface predictably tune the filament's shape and switching
- Residue size at the C-D1 α-helix / β-hairpin interface predictably shifts the waveform: enlarging V148, I156, or A438 walks the filament rightward Normal → Semi-coiled → Curly I → Curly II (R-/L-FliC ratio 2/11 → 4/11 → 5/11 → 6/11)
- **Curly-locked (necessity):** V148L / I156L can't switch → non-motile in soft agar, with reverse / momentarily-forward swimming — matching the naturally Curly-locked *E. coli* K-12 ATCC10798 (*fliC* N87K), **Kinosita et al., *Sci. Rep.* 2020** (DOI 10.1038/s41598-020-72429-1). → Switching is necessary for productive motility.
- Elevation: from "a lucky mutation" to "we understand the design rules and can program the switch"
- **Assets:** reuse fliC-structure + mutant structure panel (A438V, I156V-A438V, V148A-A438V, V148I, V148L) + V148L gif
- *(N441S and the V148I example moved to supplements — see S1, S2)*

---

## Part 4 — Close

### Slide 18 — Summary
- **Header/message:** Evolution tunes the flagellum as a load-responsive mechanical system, not by maximizing speed
- One-line Route 2 recap at top (since there is no separate Route 2 summary slide): a flagellin switch (A438V) trades liquid speed for structured-environment migration; switching is necessary and finely tuned
- Two separable mechanical routes:
  - **Number:** more flagella → faster runs / smaller reorientation; optimum is viscosity-dependent
  - **Shape:** a flagellin switch (A438V) that trades liquid speed for structured-environment migration
- Liquid swimming speed is not the determining factor for motility in complex environments
- Implication for infection: how pathogens may tune flagellar function to move through host tissue
- **Assets:** reuse em-conclusions (or a built two-route summary)

### Slide 19 — Acknowledgements
- **Header/message:** Acknowledgements
- Seiga Yanagisawa front and center; Wadhwa lab; collaborators; **Victor Sourjik (Ptac strain)**; funding
- **Assets:** reuse acknowledgements slide

---

## Supplemental / Q&A slides (backup)

### S1 — N441S: a near-twin that doesn't help (specificity / open question)
- **Header/message:** A near-identical switch (N441S) does not improve motility — the benefit depends on the precise twist, not on switching per se
- N441S also raises curvature and performs the same rotation-dependent switch as A438V, yet gives *no* halo advantage and is *not* slower in liquid
- Only difference found so far: slightly different twist values in both conformations (Δτ ≈ 3.7 vs 4.7 µm⁻¹)
- Note: N441 is not part of the V148/I156/A438 steric-packing series — it arose separately in evolution
- Which feature of A438V's switch is productive is still open
- **Assets:** WT/A438V/N441S halo (`halo-area_flic-mutants.pdf`) + swim-speed (`2025-03-26` folder)

### S2 — Waveform and speed don't predict structured motility (V148I example)
- **Header/message:** Resting waveform and liquid speed alone do not predict soft-agar motility
- V148I: Semi-coiled filament, *normal* liquid swim speed, yet *significantly reduced* soft-agar motility
- Contrast the double mutants: V148A-A438V reverts to Normal waveform but still swims slowly (like A438V); I156V-A438V reverts to Normal and swims at WT speed
- Reinforces that liquid speed and structured-environment motility are governed by distinct principles
- **Assets:** β-hairpin mutant motility + swim-speed panels (manuscript Supplemental Fig.; render from `2025-09-19_fliC_beta_hairpin_mutants_swimming`)

### S3 — Inducible strain reproduces the evolved kinematic signature (run-and-tumble)
- **Header/message:** More flagella give faster runs and smaller post-tumble reorientation — the same kinematic shift seen in *mutL* 20B
- *Ptac::flhDC* across IPTG: run-phase speed ↑, reorientation angle ↓, with no change in tumble frequency or run/tumble durations — isolating the effect as flagellar number, not genetic background
- Backup for slide 11a; promote to an inset there if making the recapitulation argument explicitly
- **Assets:** `manuscript/figures/supp/run-tumble-vs1638-1.pdf`, `-2.pdf` (already rendered)

---

## Cuts from the source deck
- Part I rotary-motor remodeling section (PNAS stator work) — cut; optional single backup slide
- Part III surface motility / swashing (Panich et al.) — cut entirely (off-abstract)
- Reynolds number / scallop theorem / two-strategies physics primer — cut or compress to a single line on slide 3

## Figure status (from Seiga's project `2026-Yanagisawa-Flagellar`)
**Already rendered — copy into deck:**
- Halo radius vs selection round (slide 5, panels 1–2) — `halo-area-vs-selection-round.pdf`
- Growth curves (slide 6) — `growth-curves/growth-curves-and-rates.pdf`
- Evolved-line swim speed across Ficoll (slide 8) — `swim-speed-ficoll-summary.pdf`
- IPTG × Ficoll halo (slide 11b) — `halo-area-vs-iptg_vs1683.pdf` (+ heatmap, peak-halo)
- Run-and-tumble, *Ptac* across IPTG (S3) — `manuscript/figures/supp/run-tumble-vs1638-1.pdf`, `-2.pdf`

**Data exists — needs rendering:**
- Flagella per cell vs [IPTG] (slide 11a premise panel) — script `2026-05-06 Number of flagella per cell - VS1638 strain ...`
- Slide 14 halo — WT vs A438V only (re-render from `halo-area_flic-mutants`, excluding N441S)
- Slide 14 swim speed — WT vs A438V from `2025-03-26_fliC_WT_vs_A438V_vs_N441S`
- VS1683 swim-speed vs IPTG × Ficoll (slide 11b) — `2026-02-16_VS1683_swim_speed`
- N441S supplement (S1) — WT/A438V/N441S halo + swim speed (same datasets)
- β-hairpin mutant motility + swim speed (S2) — `2025-09-19_fliC_beta_hairpin_mutants_swimming`

**Data not in repo — dependencies:**
- WGS mutation table/figure (slide 7) — not present; awaiting postdoc, else cut
- Frozen-stock heritability panel (slide 5, panel 3) — Seiga has it; needs to be added
- Slide 4 high-quality selection images — locate Seiga's source

## Open framing notes
- **N441S:** kept out of the main story; lives only in supplement S1 (Q&A)
- **Honesty caveat (slide 11b):** IPTG optimum shift clean 0→5% Ficoll; 10% is plateau + collapse
- Keep *mutL* 20B (number) and C11A (shape) distinct; don't repeat the "C11A indistinguishable from WT" claim
- *Optional context for Q&A:* Liu et al. 2019 independently found A438V and N441S in an *E. coli* experimental evolution but did not characterize their phenotypes

## Rough timing (25 min)
- Setup (1–3): ~3 min
- Experiment + controls + puzzle (4–8): ~5 min
- Route 1 number (9–11c): ~5 min
- Route 2 shape (12–17): ~9 min
- Close (18–19): ~3 min
</content>
