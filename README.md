# group7-optimizers
**Why optimizers converge differently: GD / SGD vs L-BFGS on ill-conditioned regression (DATA 220)**

**Team:** Priya, Varuna, Sanjana, Jyoti, Saranya
**Presentation:** Nov 2, 2026 (7 min) | **Final:** Dec 7, 2026

## Research question
How does the Hessian condition number κ affect convergence of gradient descent versus L-BFGS?

**Goal:** Show how much a stretched loss valley (large κ) slows SGD, and whether L-BFGS copes better.
We change only κ (1, 10, 100) on noise-free synthetic data, with the same start and the same stop rule for every method.

## Baseline and what we compare
- **Baseline:** Standard gradient descent (GD). Its performance is known from theory: the error shrinks by (κ−1)/(κ+1) per step, which is 0 at κ = 1, 0.82 at κ = 10 and 0.98 at κ = 100.
- **Compared against:** L-BFGS, which learns curvature from the last few gradient changes.
- **GD vs SGD:** GD uses all 200 rows at every step (full batch). SGD uses a small random batch. Results so far are from **full-batch GD, our control**. **Mini-batch SGD has not been run yet** and is a next step.

## Preliminary results (full-batch GD vs L-BFGS)
Same data, same start w = (0, 0), same stop rule (gradient norm < 1e-6).

| Dataset | κ | GD updates | L-BFGS iterations | GD gradient evals | L-BFGS gradient evals |
|---|---|---|---|---|---|
| `round_k1.csv` | 1 | 1 | 2 | 2 | 3 |
| `moderate_k10.csv` | 10 | 75 | 6 | 76 | 7 |
| `narrow_k100.csv` | 100 | 746 | 5 | 747 | 10 |

- GD update counts match theory exactly (predicted 1, 75, 746).
- L-BFGS was cross-checked against scipy L-BFGS-B (2, 6, 5 iterations).
- Gradient evaluations count distinct points.
- These results are **preliminary**. Fewer iterations does not mean lower total computational cost.
- Limits: noise-free, 2 parameters, full-batch gradients. Nothing yet about noisy mini-batches, where L-BFGS is known to be unstable.

**Next steps:** repeat from new starting points, measure gradient calls and runtime, try mini-batch SGD or feature scaling.

## Data (`data/`)
Three synthetic datasets, 200 rows each, all following y = 3·x1 + 2·x2.
True weights w* = (3, 2). No noise. Generated with AI assistance, no real observations.

| File | κ | Hessian eigenvalues |
|---|---|---|
| `round_k1.csv` | 1 | 1, 1 |
| `moderate_k10.csv` | 10 | 0.1, 1 |
| `narrow_k100.csv` | 100 | 0.01, 1 |

`dataset_manifest.json` has the full details (seed, loss, checksums).

## Shared setup (everyone uses this)
- Features: `x1`, `x2` only (ignore `sample_id`). No bias term.
- Start: w = (0, 0)
- Loss: ½ · mean((prediction − y)²)
- Gradient: Xᵀ(Xw − y)/n. Hessian: XᵀX/n (equals diag(1, 1/κ) on these datasets)
- Stop: gradient norm < 1e-6
- GD step size: 2 / (λmin + λmax)

## Final presentation deck
The final deck is `Group 7.pdf` in `slides/` (7 pages). Deck pages are one more than the slide numbers below, because the deck also has an intro slide and a closing slide.

| Deck page | Content | Presenter |
|---|---|---|
| 1 | Intro: goal, project overview, baseline | Group |
| 2 | Problem and domain | Priya |
| 3 | Existing baselines | Saranya |
| 4 | Dataset and metrics | Varuna |
| 5 | Approach and experiments | Jyoti |
| 6 | What we found and what is next | Sanjana |
| 7 | Summary, thank you, link to this repo | Group |

## Repo structure
```
data/        datasets (do not edit)
slides/      one slide per person (PDF or PPTX) and the final deck (Group 7.pdf)
notebooks/   one notebook per person (.ipynb)
README.md    this file
```

## Who does what
| Person | Part | Slide |
|---|---|---|
| Priya | Problem | 1 |
| Saranya | Existing baselines | 2 |
| Varuna | Dataset and metrics | 3 |
| Jyoti | Approach and experiments | 4 |
| Sanjana | Wrap-up, deck assembly, timing | 5 |

## How to add your work (everyone, please follow this)

### Where files go
| What | Folder | File name |
|---|---|---|
| Your slide (PDF or PPTX) | `slides/` | `YourName_Group_slideN.pdf` (e.g. `Saranya_Group_slide2.pdf`) |
| Your notebook / code | `notebooks/` | `YourName_Maths_project.ipynb` (e.g. `Varuna_Maths_project.ipynb`) |
| Final deck | `slides/` | `Group 7.pdf` |
| Datasets | `data/` | **Do not edit or add files here** |

Use your own name in your file names so nobody overwrites anyone else's work.
Avoid spaces in file names (the final deck `Group 7.pdf` is the one exception, because the class asks for that exact name).

### Steps (GitHub Desktop)
1. Open GitHub Desktop and click **Fetch origin**, then **Pull origin** to get the latest changes.
2. Put your files in the folders above (**Repository → Show in Finder** opens the repo folder).
3. Back in GitHub Desktop, tick your files under **Changes**.
4. **Untick `.DS_Store`** if it appears (hidden Mac file, not our work).
5. Write a short message in **Summary** (e.g. `Add slide 2 and notebook`) and click **Commit to main**.
6. Click **Push origin**.
7. Open the repo on github.com and check your files appear.

If you see **"Newer commits on remote"**: click **Fetch**, then **Pull origin**, then **Push origin** again.
If you see a merge conflict, don't force anything. Tell the team which file it names.

## How to use someone else's notebook
1. **Fetch origin**, then **Pull origin** in GitHub Desktop. Their notebook appears in `notebooks/`.
2. Go to colab.research.google.com → **File → Upload notebook** and choose the `.ipynb`.
3. Open the Files panel (folder icon) and upload the 3 CSVs from `data/`.
4. Run all cells (**Runtime → Run all**).

## Working rules
- Pull before you start, push when you finish.
- Edit only your own files.
- Never change files in `data/`.
- Before pushing a notebook, run all cells so the outputs are saved in it.
- Label any number that is not final as "preliminary" or "predicted".
