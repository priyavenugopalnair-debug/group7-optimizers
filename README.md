# group7-optimizers
**Why optimizers converge differently: GD / SGD vs L-BFGS on ill-conditioned regression (DATA 220)**

**Team:** Priya, Varuna, Sanjana, Jyoti, Saranya
**Presentation:** Nov 2, 2026 (7 min) | **Final:** Dec 7, 2026

## Research question
How does the Hessian condition number κ affect convergence of gradient descent versus L-BFGS?

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

## Repo structure
```
data/        datasets (do not edit)
slides/      one slide per person (PDF or PPTX)
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
| Datasets | `data/` | **Do not edit or add files here** |

Use your own name in your file names so nobody overwrites anyone else's work.
Avoid spaces in file names.

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
