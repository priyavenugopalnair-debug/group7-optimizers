# Group 7 – Final phase tasks

**Project:** Why training slows down on narrow loss valleys
**Goal:** Show how much a stretched loss valley slows SGD, and whether L-BFGS copes better.
**Final presentation:** Dec 7, 2026 · **Time limit:** TO CONFIRM · **Report:** up to 8 double-column pages (16 single-column), not counting references · **Report deadline:** TO CONFIRM
**First notebook results:** Nov 20 · **Drafts of slides and report sections:** Nov 22

Read this file top to bottom once. Then work only from your own section.

---

## 0. Ground rules (apply to everyone)

1. **One source of truth for numbers.** A number goes on a slide or into the report only if it is in a notebook cell that has been re-run and checked by your reviewer. Put the notebook name and section under every table and chart ("Source: Jyoti_Maths_project.ipynb, section 9").
2. **Never change the mid-presentation results:** GD updates 1 / 75 / 746 and L-BFGS iterations 2 / 6 / 5 for κ = 1 / 10 / 100. Add new work below the old cells.
3. **Label** anything not yet checked "preliminary".
4. **Same setup everywhere:** start (0,0), true weights w* = (3,2), stop when the gradient norm is below 1e-6, loss = ½·mean((Xw − y)²), do not standardize features, seed 42 for datasets.
5. **Same counting everywhere:** report iterations, distinct gradient evaluations (as in Jyoti's `Problem` class), and for SGD also epochs.
6. **Notebooks must run from top to bottom for anyone.** First cell says what it does and which libraries it needs (numpy, pandas, scipy, matplotlib). Load data from the GitHub raw link with a local fallback. No Colab-only code such as `google.colab.files`.
7. **Never edit someone else's file.** If you find a mistake, message the owner and your reviewer.
8. **Never commit to `main` directly.** Use your branch and a pull request.
9. **Do not copy text from papers.** Paraphrase, cite the source, and read the source before using its number.
10. **Reply "got it"** in the group chat within 24 hours of reading this file.

---

## 1. The Git routine (8 steps, same for everyone)

1. Open GitHub Desktop, select `group7-optimizers`, press **Fetch origin**, then **Pull origin**.
2. Current Branch → **New Branch**, name it `yourname-final` (for example `jyoti-final`), then **Publish branch**.
3. Do your work. Edit only your own files. Never edit `data/` unless the team agreed.
4. Notebook: open it in Colab, add new sections at the bottom, Runtime → **Run all** with no errors, File → Download → .ipynb.
5. Copy the file into your local repo folder: notebooks in `notebooks/`, slides in `slides/`, report sections in `report/`, figures in `report/figures/`.
6. In GitHub Desktop write a short summary (for example "Add SGD runs, preliminary"), press **Commit**, then **Push origin**.
7. Branch → **Create Pull Request**. Name your reviewer and say which slide or section your work supports.
8. The reviewer checks the numbers, then approves. Priya merges.

**File names:** slides `YourName_Group_slideN.pdf`, notebooks `YourName_Maths_project.ipynb`, report `YourName_section.docx`, figures `fig_description.png` (300 dpi).

**Reviewers:** Priya ← Varuna, Varuna ← Priya, Jyoti ← Sanjana, Saranya ← Jyoti, Sanjana ← Saranya.

**What a reviewer must do:** download the branch, re-run the notebook, compare each number to the slide, and reply "approved" or list the mismatches. A pull request with no review is not merged.

---

## 2. The final deck: one message per slide

| Slide | Message | Owner |
|---|---|---|
| 1 | Title, goal, and why training slows on narrow valleys (with κ) | Priya |
| 2 | Labelled pictures for κ = 1, 10, 100: GD path and L-BFGS path, κ defined in one line | Priya |
| 3 | What κ is and how it sets valley width (√κ) | Varuna |
| 4 | Why GD slows as κ grows | Jyoti |
| 5 | How L-BFGS uses curvature and why it speeds up | Saranya |
| 6 | Existing work, limits and the gap (with our baseline row) | Saranya |
| 7 | Datasets, metrics, our approach and what is new in our study | Varuna, Jyoti |
| 8 | Results: GD, SGD and L-BFGS at every κ, with the headline answer | Sanjana |
| 9 | Conclusion, limits, next steps, GitHub link | Sanjana |

**Time rule:** about 1 to 1.5 minutes per slide. If the time limit is under 9 minutes, move slide 7 into the spoken part of slides 4 and 6, and keep it in the report. Decide this as soon as the time limit is confirmed.

---

## 3. Handoffs between people (these are where work gets stuck)

| What | From | To | Due | Done when |
|---|---|---|---|---|
| New datasets κ = 3, 30, 300 (CSVs) | Varuna | Jyoti, Saranya | Nov 16 | CSVs posted in the group chat and eigenvalues printed (κ matches) |
| L-BFGS path for κ = 1, 10, 100 (CSV of weights per iteration) | Saranya | Priya | Nov 17 | File in `notebooks/` or `report/figures/`, columns `iter,w1,w2,kappa` |
| GD, SGD, L-BFGS results at all six κ | Jyoti | Sanjana, Priya | Nov 20 | Results table CSV, one row per method and κ |
| Wording of κ definition | Priya and Varuna | each other | Nov 15 | Same one-line wording on slides 2 and 3 |
| Checked numbers table | Sanjana | everyone | Nov 22 | Every number on every slide has a "pass" row |
| Slides and report sections | everyone | Priya | Nov 22 | In `slides/` and `report/` on a merged pull request |

If you are going to miss a handoff date, say so in the group chat **one day before**, not after.

---

## 4. Tasks per person

### Priya – opening, introduction, merge, professor  (reviewer: Varuna)

**Slides 1 and 2.**
1. Plot loss contours for κ = 1, 10, 100 with `0.5*(e1**2 + e2**2/k)`, `e = w − [3,2]`.
2. Each picture: axes named (w1, w2), start (0,0) and minimum (3,2) marked, κ in the title, one-line caption.
3. Draw the GD path (step `2/(1 + 1/k)`) and the L-BFGS path (from Saranya's CSV). GD zigzags across the valley in many steps. L-BFGS goes almost straight in a few. Put the step counts in the legend.
4. Define κ in one line on slide 2: "κ = steepest curvature ÷ flattest curvature; the valley is √κ times longer than wide". Use the same wording as Varuna.
5. Slide 1 explains why training slows on narrow valleys using κ, in plain words.
6. In your script say: "We explain the slowdown with GD because the maths is clearest, then show SGD slows too."

**Report:** title, authors, abstract (write last, after the results exist), introduction: purpose and motivation (about 1.5 pages).

**Also:**
7. **Email the professor this week** and paste the reply in the group chat. Draft: "Dear Professor, our final project is a controlled study of how the condition number κ slows SGD and whether L-BFGS copes better, on noise-free synthetic data where only κ changes. For the technical novelty criterion, is a controlled comparison with a theory check acceptable, or do you expect a new method? Also, what is the time limit for the presentation and the deadline for the report? Thank you."
8. Update `README.md` for the final phase and keep it current.
9. Merge slides into one deck named `Group 7` and report sections into one document. Check page count and format.
10. Keep a list of open problems on the Issues tab and chase late handoffs.

**Definition of done:**
- [ ] Slides 1 and 2 reviewed by Varuna
- [ ] Both paths drawn on every picture, labels readable at the back of a room
- [ ] Professor's reply received and recorded here
- [ ] README updated
- [ ] Final deck and report merged, page limit checked

---

### Saranya – prior work and L-BFGS  (reviewer: Jyoti)

**Slides 5 and 6.**
1. Keep your sources table, momentum and scipy checks.
2. Record s = change in weights and y = change in gradient for two steps at κ = 100. Check that y = H·s and that `Y @ inv(S)` gives back H.
3. Run L-BFGS with memory m = 1, 3, 10 and tabulate iterations.
4. Slide 5 text: "L-BFGS remembers recent moves, learns the curvature from them, and rescales the flat direction, so it takes a few big steps instead of many tiny ones."
5. **Save the L-BFGS path** (weights at each iteration) for κ = 1, 10, 100 as `lbfgs_path.csv` and give it to Priya by Nov 17.
6. **Cross-check L-BFGS on the new datasets κ = 3, 30, 300** against Jyoti's runs (scipy `L-BFGS-B` is fine). Report any mismatch to Jyoti.

**Rubric row 2: baseline performance from prior work.**
7. Make a table with columns: source, method, dataset, metric, baseline result, limit. Fill it only from sources you have read: Goh (2017) GD on a quadratic, error factor (κ−1)/(κ+1) per step; Le et al. (2011) L-BFGS on MNIST, 0.69% test error; Kingma and Ba (2015) MNIST and CIFAR-10; Byrd et al. (2016) L-BFGS with noisy mini-batches; Braglia et al. speed-up at κ around 1e4 and 1e6.
8. Add a row for **our baseline**: full-batch GD at the best step size, with measured updates 1 / 75 / 746.
9. Under the table write the gap: "Existing results use real datasets where κ is unknown or changes. None isolates κ." Add: "Prior works use MNIST and CIFAR-10 for accuracy. We use synthetic data because κ must be controlled. Our metric is updates to a gradient norm below 1e-6."
10. Say in one sentence that the rubric's "deep learning baseline" corresponds, in our project, to the standard optimizers GD and SGD.

**Report:** related works and the full reference list, in one citation style (about 1 page).

**Definition of done:**
- [ ] Every number in the prior-work table checked against its source (note page or section)
- [ ] `lbfgs_path.csv` delivered to Priya
- [ ] L-BFGS on κ = 3, 30, 300 cross-checked
- [ ] y = H·s check printed in the notebook
- [ ] References complete, no source cited that you did not read

---

### Varuna – datasets, κ and metrics  (reviewer: Priya)

**Slides 3 and 7 (datasets and metrics part).**
1. Add a cell that prints valley length ÷ width = `sqrt(lam_max/lam_min)`. It should show 1, 3.16, 10 for the three datasets.
2. Slide 3: κ = largest curvature ÷ smallest, and the valley is √κ times longer than wide. Use one picture of two contour ellipses (κ = 1 and 100) with the axes' lengths marked. Same wording as Priya.
3. **Make datasets for κ = 3, 30, 300** with the same seed-42 method (QR of centered Gaussian columns, `X = √n·Q·[1, 1/√κ]`, w* = (3,2), 200 rows). Print eigenvalues and κ to confirm. Share the CSVs by Mon Nov 16. Add to `data/` only after the team agrees.
4. Delete the Colab-only download cells.
5. State the metrics once, clearly: iterations to tolerance, distinct gradient evaluations, epochs for SGD, final gradient norm, final loss.
6. State the model: linear regression with 2 parameters, loss ½·mean((Xw − y)²). This is the "model architecture" the rubric asks for.

**Report:** methods part A: datasets, κ, the 2-parameter linear model, metrics (about 1.5 pages).

**Definition of done:**
- [ ] Printed √κ ratios 1, 3.16, 10 match the slide
- [ ] Six datasets with correct κ posted to the team
- [ ] Notebook runs without Colab-only code
- [ ] Metrics defined in one place and used the same way by Jyoti and Sanjana

---

### Jyoti – approach and experiments  (reviewer: Sanjana)

**Slides 4 and 7 (approach part).**
1. Keep your GD and L-BFGS results unchanged.
2. Add an SGD runner: batch sizes 16 and full, 5 random seeds, report mean and spread.
3. **Fair step sizes:** tune the learning rate for each batch size on a small grid and record the grid and the winner, so SGD is not handicapped. GD uses the best fixed step `2/(λmin + λmax)`.
4. **Compare methods in gradient work.** One full-gradient evaluation = 1 epoch. For L-BFGS use distinct gradient evaluations, for SGD use epochs, for GD use updates + 1. Report iterations or steps as a second number. Never compare epochs with iterations directly. Run time is a side note.
5. **Run GD, SGD and L-BFGS on all six κ values** (1, 3, 10, 30, 100, 300) with the same start and stopping rule. Save one results table (CSV) with one row per method and κ.
6. Plot steps against κ for the three methods on one chart (log scale for steps).
7. Slide 4: why GD slows. The step size must stay below 2/λmax because of the steep direction, so the flat direction shrinks by only (κ−1)/(κ+1) per step. Steps ≈ (κ/2)·ln(‖g0‖/tol). Add the "steps against κ" chart with the formula's line over your measured points.
8. Say on the slide: our data has no noise, so SGD still converges. Noisy data may behave differently (Byrd et al. 2016).

**Rubric row 3: technical novelty.**
9. State our contribution directly: "A controlled, noise-free study where only κ changes (1 to 300), measuring how much GD, SGD and L-BFGS slow down."
10. Show three points that make it new as a study: (a) only κ changes between datasets (same seed, same w* = (3,2)); (b) every method is counted the same way; (c) measured results are checked against theory (the 1/75/746 prediction).
11. Add one line on how it overcomes the limit: "It shows κ's effect directly, which a deep-network benchmark cannot."

**Report:** methods part B: GD, SGD, L-BFGS, step sizes, fair-comparison rules (about 1.5 pages).

**Definition of done:**
- [ ] Old GD and L-BFGS numbers unchanged
- [ ] SGD at all six κ with mean and spread over 5 seeds
- [ ] Learning-rate grid and winner recorded
- [ ] Results CSV delivered to Sanjana and Priya
- [ ] Slide 4 chart shows measured points and the formula line

---

### Sanjana – results, checking, flow  (reviewer: Saranya)

**Slides 8 and 9.**
1. Change "Group 8" to "Group 7" in your notebook title.
2. Build the check table: one row per number on any slide or in the report: where it appears, who produced it, their value, your independent re-run value, pass or fail. Re-run at least the full-batch GD and L-BFGS numbers yourself; for SGD, re-run one seed and confirm it matches Jyoti's.
3. Combine the results into one table and one chart (GD, SGD, L-BFGS at every κ, iterations and gradient evaluations).
4. **Write the headline answer to the goal** on slide 8 and in the abstract, in one sentence, for example "At κ = 100, GD needs X updates, SGD Y epochs and L-BFGS Z iterations". Use only numbers that passed your check table.
5. State the limits plainly on slide 9: noise-free data, 2 parameters, full-batch L-BFGS, SGD with fixed batch sizes.
6. Write the timing plan for the final presentation after the time limit is confirmed. Give each speaker a time and rehearse.
7. Collect everyone's speaker script and likely questions (see section 6).

**Report:** results with tables and figures, and conclusions (about 2 pages). Then read the whole report for flow, consistent terms and notation.

**Definition of done:**
- [ ] Every number on every slide has a "pass" row
- [ ] Headline sentence matches the results table exactly
- [ ] Limits stated
- [ ] Timing plan fits the limit
- [ ] Whole report read once for coherence

---

## 5. Professor's rubric: evidence for every row

### Presentation (5 criteria, 2 points each)

| Criterion | What the professor wants | Our slides | Owner | Evidence that it is met |
|---|---|---|---|---|
| 1. Project domain / problem | Area and challenge | 1, 2 | Priya | Names optimization for machine learning; explains why training slows on narrow valleys with κ; labelled pictures a stranger can read |
| 2. Current baseline / dataset / metrics | Existing works, limits, gaps; datasets and metrics from prior work and baseline performance | 6, 7 | Saranya, Varuna | Prior-work table with datasets, metrics and baseline results, our baseline row, gap sentence, our datasets and metrics |
| 3. Approach / technical novelty | What we do compared to baselines; how it overcomes limits | 3, 4, 5, 7 | Varuna, Jyoti, Saranya | Contribution sentence, three "new as a study" points, κ explanation, why GD slows, how L-BFGS uses curvature |
| 4. Results | Our performance versus baselines, using the metrics | 8 | Sanjana, Jyoti | One table and chart of GD, SGD, L-BFGS at six κ values, headline sentence, limits |
| 5. Presentation | Logical flow, attractive, effective, within time | all | Sanjana, Priya | One message per slide, timed rehearsals at or under the limit, scripts done |

### Technical report (up to 8 double-column pages, 1 point each)

| Criterion | Section | Owner | Evidence |
|---|---|---|---|
| 1. Domain / problem | Introduction | Priya | Area, problem and motivation stated in the first page |
| 2. Baseline / dataset / metrics | Related works, Methods A | Saranya, Varuna | Prior-work table, datasets, metrics, baseline numbers |
| 3. Approach / novelty | Methods B | Jyoti | Contribution, setup, fair-comparison rules |
| 4. Results | Results | Sanjana | Tables and figures comparing methods with metrics |
| 5. Writing skill | Whole | Sanjana reads, Priya merges | Same terms and symbols throughout, clear transitions |

The report must also contain: title, authors, abstract, introduction, related works (optional), methods including dataset and model architecture, results with figures and tables, conclusions, references.

**Page budget (double column):** abstract and introduction 1.5, related works 1, methods 3, results 2, conclusions 0.5 = 8 pages, references extra.

**The two rows most at risk:** criterion 3 (we study, we do not propose a new method) and criterion 2 (prior-work results are deep-learning results, ours is a 2-parameter problem). The steps above address both. At the check, Sanjana scores these two rows first, using the professor's own description text.

**Final rubric check (Dec 1–3, Priya and Sanjana):** go through every row, slide by slide and section by section, and tick it with evidence. Anything not ticked goes back to its owner with a deadline.

---

## 6. Things that are easy to forget

1. **Speaker scripts.** Each person writes a short script for their own slides. Plain words, one idea per sentence, timed with a stopwatch. Due Nov 30.
2. **Question practice.** Each person writes three likely questions and short answers for their own part, for example: "Why only 2 parameters?", "Why no noise?", "Why is SGD tested only on noise-free data?", "How does L-BFGS know the curvature?", "Why does the L-BFGS result not carry to deep networks?". Send them to Sanjana by Dec 1.
3. **Two timed rehearsals** with the whole team: Nov 30–Dec 3 and Dec 4–6.
4. **Backup.** Everyone keeps a PDF of the final deck on their own device and a copy on a USB stick or cloud drive.
5. **Repo check on Dec 6.** Open the repo page and confirm the final deck, report, notebooks and README are present, and the GitHub link on the last slide opens.
6. **Optional extension, only after the core work is checked** (Varuna, a few hours): run GD with the flat direction rescaled by √κ (a simple preconditioner). It converges in a single step at every κ, which shows the slowdown comes from the curvature mismatch, not from the data size. Mark it "extension" and do not let it delay anything else.

---

## 7. Risks and fallbacks

| Risk | What we do |
|---|---|
| Professor says a controlled study is not enough novelty | Keep the study, add the preconditioning extension (section 6) as our "method", and describe both in Methods B |
| SGD results are not ready on Nov 20 | Jyoti posts what she has on Nov 21. If still missing on Nov 22, slides say "SGD: preliminary, 3 seeds" and the goal sentence is worded as what we showed |
| SGD behaves differently from expectation | Report it exactly as measured. The goal is "how much it slows", not "that it slows" |
| Time limit is shorter than expected | Merge slide 7 into slides 4 and 6 (section 2) |
| A number on a slide does not match a notebook | Sanjana's check table fails it, the owner fixes it, the reviewer re-checks. No slide goes into the final deck with a failed row |
| A prior-work number cannot be verified | Remove it. Never leave an unchecked citation in |
| Someone is late or ill | Their reviewer takes over the slide with the owner's notebook. Priya decides within one day |
| Two people edited the same file | Do not overwrite. Pull first, message Priya, keep both parts |
| Report exceeds 8 pages | Cut related works and methods details first, keep results |

---

## 8. Timeline

| Dates | What |
|---|---|
| Nov 13–15 | Everyone reads this file, replies "got it", creates a branch. Priya emails the professor. Priya and Varuna agree the κ wording by Nov 15 |
| Mon Nov 16 | Varuna posts the κ = 3, 30, 300 datasets |
| Tue Nov 17 | Saranya delivers the L-BFGS path to Priya |
| Fri Nov 20 | Jyoti delivers results at all six κ. First notebook pull requests |
| Sun Nov 22 | Drafts of slides and report sections in the repo. Sanjana's check table complete |
| Nov 23–29 | Reviews and fixes (Thanksgiving is Nov 26). Priya merges deck and report by Nov 29 |
| Nov 30–Dec 3 | Speaker scripts, first timed rehearsal, rubric check, question practice |
| Dec 4–6 | Second rehearsal, final files, backups, repo check (Dec 6) |
| Mon Dec 7 | Final presentation |

---

## 9. If you get stuck

- **Pull fails:** commit or discard your changes in GitHub Desktop, then pull again.
- **Conflict message:** do not overwrite. Message Priya before pushing.
- **Can't see the repo:** check your email for the invitation, or open the repo link while signed in.
- **Notebook will not run for the reviewer:** check that it loads data from the GitHub raw link, uses no local paths, and states its libraries in the first cell.
- **You think a number is wrong:** tell the owner and your reviewer. Do not change it yourself.
