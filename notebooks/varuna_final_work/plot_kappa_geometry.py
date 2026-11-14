from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTPUT_FOLDER = Path(__file__).resolve().parent / "figures"
OUTPUT_FOLDER.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
fig.subplots_adjust(left=0.09, right=0.96, top=0.83, bottom=0.14, hspace=0.7)
fig.suptitle("How κ changes the loss contour", fontsize=21, fontweight="bold", y=0.97)
fig.text(0.5, 0.915, "κ = steepest curvature ÷ flattest curvature = λmax ÷ λmin", ha="center", fontsize=13)
fig.text(0.5, 0.875, "Same loss level f(w) = 0.5; same axis limits and equal unit scaling", ha="center", fontsize=11)

theta = np.linspace(0, 2 * np.pi, 600)
for ax, kappa, color in zip(axes, (1, 100), ("#206C90", "#C8533A")):
    a = np.sqrt(kappa)
    w2 = 2 + a * np.cos(theta)
    w1 = 3 + np.sin(theta)
    loss = 0.5 * ((w1 - 3)**2 + (w2 - 2)**2 / kappa)
    assert np.allclose(loss, 0.5, atol=1e-12, rtol=0)
    ax.fill(w2, w1, color=color, alpha=0.08)
    ax.plot(w2, w1, color=color, linewidth=2.5)
    ax.scatter([2], [3], marker="*", s=120, color="#172638", zorder=4)
    ax.annotate("Minimum: (w1, w2) = (3, 2)", xy=(2, 3), xytext=(4, 1.1),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("", xy=(2-a, 4.65), xytext=(2+a, 4.65),
                arrowprops={"arrowstyle": "<->", "color": color})
    ax.text(2, 4.85, f"Length = {2*a:g}", ha="center", color=color, fontsize=11)
    bracket_x = 2 + a + 0.65
    ax.annotate("", xy=(bracket_x, 2), xytext=(bracket_x, 4),
                arrowprops={"arrowstyle": "<->", "color": color})
    ax.text(bracket_x+0.3, 3, "Width = 2", va="center", color=color, fontsize=10)
    ax.set_title(f"κ = {kappa}: length ÷ width = {a:g}", loc="left", fontsize=13, fontweight="bold")
    ax.set_xlim(-10, 16)
    ax.set_ylim(0.5, 5.8)
    ax.set_xticks([-8, -3, 2, 7, 12])
    ax.set_yticks([1, 3, 5])
    ax.set_xlabel("w2 (flatter direction when κ > 1)", fontsize=10)
    ax.set_ylabel("w1", fontsize=11)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)

fig.text(0.5, 0.065, "For this quadratic loss: contour length ÷ width = √κ.", ha="center", fontsize=13, fontweight="bold")
fig.text(0.5, 0.03, "At κ = 100, the contour is 10 times longer than wide. These curves show loss geometry, not optimizer paths.", ha="center", fontsize=10)
for extension in ("png", "pdf"):
    path = OUTPUT_FOLDER / f"varuna_kappa_geometry.{extension}"
    fig.savefig(path, dpi=220, facecolor="white")
    print("Saved:", path)
plt.close(fig)
