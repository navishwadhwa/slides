"""Redraw the acetate/formate panels (salmo-acetate.png) for the CBP talk.

Values were digitized from salmo-acetate.png by pixel calibration against the
axis ticks (about +/-0.05 mM for acetate, +/-0.02 mM for formate). Error bars
that were shorter than the marker in the original are approximate.
"""
import matplotlib.pyplot as plt

pos = [-1.0, -0.1, 0.0, 0.1, 1.0]  # cm relative to colony edge
acetate = [11.21, 10.75, 11.40, 1.64, 0.89]
acetate_err = [0.46, 0.72, 0.34, 0.22, 0.19]
formate = [1.03, 1.51, 2.32, 0.25, 0.24]
formate_err = [0.05, 0.07, 0.13, 0.16, 0.11]

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 20,
    "axes.linewidth": 1.5,
    "xtick.major.width": 1.5,
    "ytick.major.width": 1.5,
    "xtick.major.size": 6,
    "ytick.major.size": 6,
})

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
panels = [
    (axes[0], acetate, acetate_err, "Acetate (mM)", "#1b7f8c", 15),
    (axes[1], formate, formate_err, "Formate (mM)", "#d9822b", 3),
]
for ax, y, err, label, color, ymax in panels:
    ax.axvspan(-1.4, 0, color="#eeeeee", zorder=0)
    ax.axvline(0, color="0.4", lw=1.5, ls="--", zorder=1)
    ax.errorbar(pos, y, yerr=err, fmt="o", ms=11, color=color,
                mec="white", mew=1.2, ecolor=color, elinewidth=2,
                capsize=5, capthick=2, zorder=3)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(0, ymax)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([0, ymax / 3, 2 * ymax / 3, ymax])
    ax.set_ylabel(label)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(-0.7, ymax * 0.93, "colony", ha="center", va="top",
            fontsize=17, color="0.35")
    ax.text(0.7, ymax * 0.93, "outside", ha="center", va="top",
            fontsize=17, color="0.35")

fig.supxlabel("Position relative to colony edge (cm)")
fig.get_layout_engine().set(w_pad=0.1, wspace=0.08)
fig.savefig("salmo-acetate-clean.png", dpi=200, transparent=False,
            facecolor="white")
