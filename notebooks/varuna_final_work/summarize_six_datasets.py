from pathlib import Path
import numpy as np
import pandas as pd

WORK_FOLDER = Path(__file__).resolve().parent
REPO_FOLDER = WORK_FOLDER.parent.parent
TOLERANCE = 1e-6

# Read the original datasets and the three new review datasets.
datasets = [
    (1, REPO_FOLDER / "data/round_k1.csv"),
    (3, WORK_FOLDER / "datasets_for_review/synthetic_k3.csv"),
    (10, REPO_FOLDER / "data/moderate_k10.csv"),
    (30, WORK_FOLDER / "datasets_for_review/synthetic_k30.csv"),
    (100, REPO_FOLDER / "data/narrow_k100.csv"),
    (300, WORK_FOLDER / "datasets_for_review/synthetic_k300.csv"),
]

rows = []

for expected_kappa, path in datasets:
    df = pd.read_csv(path)
    X = df[["x1", "x2"]].to_numpy(dtype=float)
    y = df["y"].to_numpy(dtype=float)
    n = len(df)

    # Calculate the Hessian and its eigenvalues from the CSV.
    H = X.T @ X / n
    lambda_min, lambda_max = np.linalg.eigvalsh(H)
    measured_kappa = lambda_max / lambda_min

    target_difference = np.max(
        np.abs(y - X @ np.array([3.0, 2.0]))
    )

    # Check the data before including it in the summary.
    assert n == 200, f"Wrong row count: {path.name}"
    assert np.isfinite(X).all() and np.isfinite(y).all()
    assert np.max(np.abs(X.mean(axis=0))) < 1e-12
    assert target_difference < 1e-12
    assert np.allclose(
        H,
        np.diag([1.0, 1.0 / expected_kappa]),
        rtol=0,
        atol=1e-12,
    ), f"Unexpected Hessian: {path.name}"

    gd_step = 2.0 / (lambda_min + lambda_max)
    starting_gradient = -(X.T @ y) / n
    starting_gradient_norm = np.linalg.norm(starting_gradient)

    # Predict GD updates using the project's quadratic model.
    rho = (expected_kappa - 1.0) / (expected_kappa + 1.0)

    if expected_kappa == 1:
        predicted_updates = 1
    else:
        predicted_updates = int(np.floor(
            np.log(TOLERANCE / starting_gradient_norm)
            / np.log(rho)
        )) + 1

    rows.append({
        "dataset": path.name,
        "source_path": path.relative_to(REPO_FOLDER).as_posix(),
        "rows": n,
        "expected_kappa": expected_kappa,
        "measured_kappa": measured_kappa,
        "H11": H[0, 0],
        "H12": H[0, 1],
        "H22": H[1, 1],
        "lambda_min": lambda_min,
        "lambda_max": lambda_max,
        "contour_axis_ratio": np.sqrt(measured_kappa),
        "GD_step": gd_step,
        "GD_shrink_factor": rho,
        "starting_gradient_norm": starting_gradient_norm,
        "predicted_GD_updates": predicted_updates,
        "max_target_difference": target_difference,
        "checks_passed": True,
        "GD_count_status": "Theoretical prediction",
    })

summary = pd.DataFrame(rows)
output_path = WORK_FOLDER / "varuna_six_dataset_summary.csv"
summary.to_csv(output_path, index=False)

print("\nALL SIX DATASETS: CHECKS PASSED\n")
print(summary[[
    "expected_kappa",
    "lambda_min",
    "lambda_max",
    "contour_axis_ratio",
    "GD_step",
    "predicted_GD_updates",
]].to_string(index=False, float_format=lambda v: f"{v:.6f}"))

print("\nDataset properties were calculated from the CSV files.")
print("GD update counts are theoretical predictions, not training results.")
print("Assumptions: start (0, 0), full-gradient L2 norm < 1e-6.")
print("\nSaved:", output_path)
