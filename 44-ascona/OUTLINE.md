# Ascona Talk Outline — Experimental Evolution of Flagellar Motility

**Talk:** Ascona 2026, "Mechanobiology of Infection"
**Length:** 25 min talk + 5 min Q&A
**Scope:** Single topic — Seiga Yanagisawa's experimental evolution project
**Audience:** Biophysics / microbial mechanobiology
**Mutant naming:** Use real designations (*mutL* 20B, A438V, N441S, V148L), not generic "Mutant A/B"

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
- Frame for infection relevance (pathogens must move through structured host environments)
- **Assets:** reuse soil/pond/gut/pipe images

### Slide 3 — Flagella power motility — but how is it tuned?
- **Header/message:** Bacteria swim by rotating helical flagella — but how do they tune motility in structured environments, and is liquid swimming speed even the right proxy?
- Quick visual: flagellar bundle rotates → propulsion (keep physics minimal; this audience knows low-Re)
- Plant the central question that the talk answers
- **Assets:** reuse fluo-bundle.gif + swimming schematic

---

## Part 1 — The experiment, the controls, and the puzzle

### Slide 4 — Experimental evolution selects for soft-agar motility
- **Header/message:** Experimental evolution selects for enhanced motility in soft agar
- Serial soft-agar selection: inoculate → halo expands → pick the leading edge → transfer
- Parallel WT and Δ*mutL* (hypermutator) backgrounds
- **Note:** change header from "Directed evolution" → "Experimental evolution" (directed evolution = protein engineering to this audience)
- **Assets:** reuse dee-1…5 build animation

### Slide 5 — Motility is rapidly and heritably enhanced
- **Header/message:** Motility rapidly improves over selection rounds, in both backgrounds
- Halo radius grows monotonically with round
- Hypermutator background gains more and faster
- Heritable (frozen-stock re-inoculation retains enlarged halos) — *frozen-stock panel pending in project*
- **Assets:** reuse dee-20 plot

### Slide 6 — Control: it's not just faster growth  *(NEW)*
- **Header/message:** Evolved lines don't grow faster in liquid — the bigger halos aren't a growth-rate artifact
- Preempts the Fisher–Kolmogorov objection (halo speed ~ √(growth × motility))
- Liquid TB growth curves: hypermutator-derived lines match or grow *slower* than ancestor; motility gains came with a fitness cost in liquid
- Honest scope: rules out a uniform shift in intrinsic growth rate (not in-agar growth-coupled physics)
- **Assets:** NEW — render growth-curve panel from project `outputs/figure-panels/growth-curves/`

### Slide 7 — Genetic basis: selection targets the flagellar system  *(PLACEHOLDER)*
- **Header/message:** Whole-genome sequencing shows selection repeatedly and independently hits the flagellar system
- Two routes visible in the genetics: *flhDC* promoter mutations (→ number route); *fliC* point mutations A438V / N441S (→ shape route); plus chemotaxis genes
- Bridges evolution → mechanism; motivates dissecting each route
- **Assets:** PLACEHOLDER — processed WGS figure does not yet exist in project; leave empty figure slot. Postdoc may supply in time. If not, cut this slide; talk still stands on plasmid-complementation causality.

### Slide 8 — The puzzle: liquid speed ≠ structured-environment motility
- **Header/message:** Swimming speed in liquid does not predict motility in structured environments
- Some evolved lines swim *slower* than the ancestor in liquid yet make *larger* halos
- This is the hook the rest of the talk resolves — twice (number, then shape)
- **Assets:** reuse tracking-video gif + mutant-swimming plot

---

## Part 2 — Route 1: flagellar number

### Slide 9 — Selection drives morphological change
- **Header/message:** Selection changes flagellar morphology
- TEM shows evolved cells differ in flagellar number and filament shape — bridges into the two routes
- **Assets:** reuse em.png

### Slide 10 — *mutL* 20B has more flagella
- **Header/message:** The *mutL* 20B line carries ~2× as many flagella as the ancestor
- TEM counts (two-Poisson mixture fits); 20B ≈ 2× WT
- **Caution:** keep 20B (more flagella) distinct from C11A; do not claim C11A is "indistinguishable from WT" — project data show C11A actually has slightly *fewer* flagella
- **Assets:** reuse wt-mutantA-em + flagella-counts

### Slide 11a — More flagella improve migration
- **Header/message:** Increasing flagellar number is sufficient to improve soft-agar motility
- Inducible *Ptac::flhDC* (IPTG titrates flagellar number, ~1–18 per cell)
- More flagella → faster runs, smaller reorientation angle, bigger halos
- **Assets:** reuse IPTG-sketch + IPTG-data (current 3-concentration bar)

### Slide 11b — But the optimum is viscosity-dependent — and it's not a speed effect  *(NEW figures)*
- **Header/message:** The optimal flagellar number depends on viscosity, and the high-viscosity cost is not a swimming-speed effect
- Halo across IPTG × Ficoll: peak halo shifts to *lower* induction as viscosity rises; at high viscosity the benefit collapses
- Swim speed across IPTG × Ficoll: speed *saturates* (plateaus) with induction — so the halo decline at high IPTG cannot be a speed effect → a structured-environment-specific cost of too many flagella
- **Makes Route 1 a second instance of the central thesis** (liquid speed ≠ structured motility)
- **Honesty caveat (from project session notes):** "optimum shifts lower with viscosity" is statistically clean 0%→5% Ficoll; at 10% it is a plateau + magnitude collapse, not a clean peak shift. Phrase as "optimum drops with viscosity, and at high viscosity the benefit collapses."
- **Assets:** NEW — render IPTG × Ficoll halo matrix + swim-speed-vs-IPTG from project (`halo-area-vs-iptg_vs1683.py`; VS1683 swim-speed data)

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
- **Assets:** reuse plate-speed; ADD flic-mutants halo × Ficoll figure (WT/A438V/N441S at 0%/10%) — NEW render; this figure also carries N441S for slide 17

### Slide 15 — Primer: the polymorphic landscape
- **Header/message:** Flagellar filaments are polymorphic — they switch between a discrete set of helical waveforms
- The twist (τ) landscape: L-straight, f1, Normal, Coiled (left-handed) | Semi-coiled, Curly I, Curly II … R-straight (right-handed)
- WT *fliC* sits at Normal, at rest and rotating
- **Placed here deliberately** (after the inversion) so it arrives as the answer-key to the puzzle and sets up the mechanism
- **Assets:** reuse wt-twist.png (this is the existing slide-31 sketch — it works as the primer)

### Slide 16 — The switch
- **Header/message:** A438V is a rotation-driven shape switch
- mutant-twist: A438V sits at Semi-coiled at rest → jumps to Normal/f1 during rotation → snaps back when rotation stops/reverses
- Shape change initiates proximally and propagates distally (dramatic extension/retraction)
- **Assets:** reuse mutant-twist.png + one resting/rotating gif for the visceral effect

### Slide 17 — A programmable switch: design rules at the β-hairpin
- **Header/message:** Mutations at the flagellin β-hairpin interface predictably tune the filament's shape and switching
- Residue size at the C-D1 α-helix / β-hairpin interface predictably shifts the resting waveform and the switch (larger/smaller side chains → predictable moves on the landscape)
- **N441S (specificity / open question):** a near-twin of A438V — also raises curvature, also performs the same rotation-dependent switch — yet gives *no* halo advantage and is *not* slower in liquid. The only difference found so far is slightly different twist values in both conformations (Δτ ≈ 3.7 vs 4.7 µm⁻¹). → The benefit depends on the *precise* twist the filament reaches, not on switching per se. Which feature of A438V's switch is productive is still open.
- **V148L / Curly-locked (necessity):** lock the filament so it can't switch → non-motile, with reverse / momentarily-forward swimming (matches naturally Curly-locked *fliC* N87K). → Switching is necessary for productive motility.
- Elevation: from "a lucky mutation" to "we understand the design rules and can program the switch"
- **Assets:** reuse fliC-structure + mutant structure panel (A438V, I156V-A438V, V148A-A438V, V148I, V148L) + V148L gif; consider placing N441S and V148L on the τ landscape

---

## Part 4 — Close

### Slide 18 — Summary
- **Header/message:** Evolution tunes the flagellum as a load-responsive mechanical system, not by maximizing speed
- Two separable mechanical routes:
  - **Number:** more flagella → faster runs / smaller reorientation; optimum is viscosity-dependent
  - **Shape:** a flagellin switch (A438V) that trades liquid speed for structured-environment migration
- Liquid swimming speed is the wrong proxy for motility in complex environments
- Implication for infection: how pathogens may tune flagellar function to move through host tissue
- **Assets:** reuse em-conclusions (or a built two-route summary)

### Slide 19 — Acknowledgements
- **Header/message:** Acknowledgements
- Seiga Yanagisawa front and center; Wadhwa lab; collaborators; funding
- **Assets:** reuse acknowledgements slide

---

## Cuts from the source deck
- Part I rotary-motor remodeling section (PNAS stator work) — cut; optional single backup slide
- Part III surface motility / swashing (Panich et al.) — cut entirely (off-abstract)
- Reynolds number / scallop theorem / two-strategies physics primer — cut or compress to a single line on slide 3

## New figures to render from Seiga's project (`2026-Yanagisawa-Flagellar`)
1. **Growth curves** (slide 6) — `outputs/figure-panels/growth-curves/`
2. **IPTG × Ficoll halo matrix + swim-speed-vs-IPTG** (slide 11b) — `halo-area-vs-iptg_vs1683.py` + VS1683 swim-speed data
3. **flic-mutants halo × Ficoll incl. N441S** (slides 14 + 17) — `halo-area_flic-mutants.py`

## Open items / dependencies
- **WGS figure (slide 7):** processed figure not yet in project; placeholder until postdoc supplies, else cut
- **Frozen-stock heritability (slide 5):** panel pending in project; state verbally for now
- **N441S framing (slide 17):** woven in as specificity / open question; can be removed later if it muddies
- **Honesty caveat (slide 11b):** IPTG optimum shift clean 0→5% Ficoll; 10% is plateau + collapse
- Keep *mutL* 20B (number) and C11A (shape) distinct; don't repeat the "C11A indistinguishable from WT" claim

## Rough timing (25 min)
- Setup (1–3): ~3 min
- Experiment + controls + puzzle (4–8): ~5 min
- Route 1 number (9–11b): ~5 min
- Route 2 shape (12–17): ~9 min
- Close (18–19): ~3 min
</content>
</invoke>
