from pathlib import Path
import numpy as np
import pandas as pd

# Shared project settings
N = 200
SEED = 42
TRUE_WEIGHTS = np.array([3.0, 2.0])
TOLERANCE = 1e-6

WORK_FOLDER = Path(__file__).resolve().parent
REPO_FOLDER = WORK_FOLDER.parent.parent
OUTPUT_FOLDER = WORK_FOLDER / "datasets_for_review"

# Create two centred, orthogonal columns.
rng = np.random.default_rng(SEED)
A = rng.standard_normal((N, 2))
A = A - A.mean(axis=0)

Q, R = np.linalg.qr(A)

# Fix QR signs so the features match the original dataset.
Q = Q * np.where(np.diag(R) < 0, -1.0, 1.0)
base_features = np.sqrt(N) * Q

# Check consistency with the existing round dataset.
original = pd.read_csv(REPO_FOLDER / "data" / "round_k1.csv")
assert np.allclose(
    base_features,
    original[["x1", "x2"]].to_numpy(),
    rtol=0,
    atol=1e-12,
), "Original features do not match. Stop and check the generator."

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
summary = []

for kappa in (3, 30, 300):
    # Scale the second feature to control the Hessian.
    X = base_features @ np.diag([1.0, 1.0 / np.sqrt(kappa)])
    y = X @ TRUE_WEIGHTS

    dataset = pd.DataFrame({
        "sample_id": np.arange(1, N + 1),
        "x1": X[:, 0],
        "x2": X[:, 1],
        "y": y,
    })

    filename = f"synthetic_k{kappa}.csv"
    dataset.to_csv(OUTPUT_FOLDER / filename, index=False)

    # Read the saved file back and verify its actual contents.
    saved = pd.read_csv(OUTPUT_FOLDER / filename)
    X_saved = saved[["x1", "x2"]].to_numpy()
    y_saved = saved["y"].to_numpy()

    H = X_saved.T @ X_saved / N
    eigenvalues = np.linalg.eigvalsh(H)
    lambda_min, lambda_max = eigenvalues

    target_difference = np.max(
        np.abs(y_saved - X_saved @ TRUE_WEIGHTS)
    )

    assert len(saved) == N
    assert np.isfinite(saved.to_numpy()).all()
    assert np.max(np.abs(X_saved.mean(axis=0))) < 1e-12
    assert target_difference < 1e-12
    assert np.allclose(
        H, np.diag([1.0, 1.0 / kappa]),
        rtol=0, atol=1e-12,
    )

    gd_step = 2.0 / (lambda_min + lambda_max)
    rho = (kappa - 1.0) / (kappa + 1.0)
    starting_gradient_norm = np.linalg.norm(H @ TRUE_WEIGHTS)

    predicted_updates = int(np.ceil(
        np.log(TOLERANCE / starting_gradient_norm) / np.log(rho)
    ))

    summary.append({
        "dataset": filename,
        "rows": len(saved),
        "kappa": kappa,
        "lambda_min": lambda_min,
        "lambda_max": lambda_max,
        "measured_kappa": lambda_max / lambda_min,
        "contour_axis_ratio": np.sqrt(kappa),
        "GD_step": gd_step,
        "predicted_GD_updates": predicted_updates,
        "max_target_difference": target_difference,
        "checks_passed": True,
        "GD_count_status": "Theoretical prediction",
    })

results = pd.DataFrame(summary)
results.to_csv(
    WORK_FOLDER / "varuna_new_dataset_checks.csv",
    index=False,
)

print("\nOriginal dataset consistency check: PASSED")
print("\nAll three new datasets: CHECKS PASSED\n")
print(results[[
    "dataset",
    "rows",
    "measured_kappa",
    "GD_step",
    "predicted_GD_updates",
    "checks_passed",
]].to_string(index=False))

print("\nGD counts are predictions, not measured optimizer results.")
print("\nFiles saved in:", WORK_FOLDER)
