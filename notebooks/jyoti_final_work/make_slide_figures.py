# Slide versions of the figures, drawn from the notebook's results CSV (no new numbers).
import sys, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
csv, out = sys.argv[1], sys.argv[2]
res = pd.read_csv(csv); TOL = 1e-6; g0 = 3.0
BG, NAVY, TEAL, GREY = "#F7F5F0", "#202B45", "#24777A", "#8C95A6"
plt.rcParams.update({"font.family": "Inter", "font.size": 17})
gd = res[res.method == "GD"].set_index("kappa")["iterations or steps"]
ks = gd.index.values; kk = np.linspace(1.6, 400, 400)
fig, ax = plt.subplots(figsize=(8.2, 5.6), facecolor=BG); ax.set_facecolor(BG)
ax.plot(kk, np.log(TOL / g0) / np.log((kk - 1) / (kk + 1)), color=TEAL, lw=3, label="theory")
ax.scatter(ks, gd.values, s=150, color=NAVY, zorder=3, label="measured")
for k, v in gd.items():
    ax.annotate(f"{v:.0f}", (k, v), textcoords="offset points", xytext=(12, 4) if k == 1 else (-12, 12),
                ha="left" if k == 1 else "right", fontsize=17, color=NAVY, fontweight="semibold")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xticks(ks); ax.set_xticklabels(ks); ax.minorticks_off()
ax.set_ylim(0.6, 5000); ax.set_yticks([1, 10, 100, 1000]); ax.set_yticklabels(["1", "10", "100", "1000"])
ax.set_xlabel("κ"); ax.set_ylabel("GD updates to tolerance")
ax.legend(frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
for s in ["left", "bottom"]: ax.spines[s].set_color(GREY)
ax.tick_params(colors=NAVY)
plt.tight_layout(); plt.savefig(out, dpi=300, facecolor=BG)
