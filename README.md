# group7-optimizers
Why optimizers converge differently
GD / SGD vs L-BFGS on ill-conditioned regression (DATA 220)

**Team:** Sanjana, Priya, Varuna, Jyoti, Saranya
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
