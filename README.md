# group7-optimizers
Why optimizers converge differently
GD / SGD vs L-BFGS on ill-conditioned regression (DATA 220)

**Team:** Priya, Varuna,Sanjana, Jyoti, Saranya
**Presentation:** Nov 2, 2026 (7 min) | **Final:** Dec 7, 2026

## Research question
How does the Hessian condition number κ affect convergence of gradient descent
versus L-BFGS?

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
- Stop: gradient norm < 1e-6
- GD step size: 2 / (λmin + λmax)

## Who does what
| Person | Part |
|---|---|
| Priya | Slide 1: problem |
| Saranya | Slide 2: existing baselines |
| Varuna | Slide 3: dataset and metrics |
| Jyoti | Slide 4: approach and experiments |
| Sanjana | Slide 5: wrap-up, deck assembly, timing |

## Working rules
- Run `git pull` before you start.
- Edit only your own files.
- Don't change files in `data/`.

## How to add your work (everyone, please follow this)

### Where files go
| What | Folder | File name |
|---|---|---|
| Your slide (PDF or PPTX) | `slides/` | `YourName_Group_slideN.pdf` (e.g. `Saranya_Group_slide2.pdf`) |
| Your notebook / code | `notebooks/` | `YourName_Maths_project.ipynb` (e.g. `Varuna_Maths_project.ipynb`) |
| Datasets | `data/` | **Do not edit or add files here** |

Slide numbers: 1 = Priya, 2 = Saranya, 3 = Varuna, 4 = Jyoti, 5 = Sanjana.

Use your own name in your file names so nobody overwrites anyone else's work.

### Steps (GitHub Desktop)
1. Open GitHub Desktop and click **Fetch origin / Pull origin** to get the latest changes.
2. Put your files in the folders above (right-click in Finder/Explorer to open the repo folder: **Repository → Show in Finder**).
3. Back in GitHub Desktop, tick your files under **Changes**.
4. **Untick `.DS_Store`** if it appears (it's a hidden Mac file, not our work).
5. Write a short message in **Summary** (e.g. `Add slide 2 and notebook`) and click **Commit to main**.
6. Click **Push origin**.
7. Open the repo on github.com and check your files appear.

### Rules
- Pull before you start, push when you finish.
- Only edit your own files.
- Never change files in `data/`.
- Before pushing a notebook, run all cells so the outputs are saved in it.
- Label any number that is not final as "preliminary" or "predicted".
