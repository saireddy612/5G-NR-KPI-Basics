# code/plots.py
from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import pandas as pd

from .kpis import KPI_MAP, THROUGHPUT_COL

def _ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def plot_individual_kpis(
    df_all: pd.DataFrame,
    out_dir: Path,
) -> None:
    """
    Creates 4 individual scatter plots:
    - dl_vs_rsrp.png
    - dl_vs_sinr.png
    - dl_vs_dlbler.png
    - dl_vs_dlmcs.png
    """
    _ensure_dir(out_dir)

    for short_name, (xcol, xlabel) in KPI_MAP.items():
        tmp = df_all[[xcol, THROUGHPUT_COL]].dropna()
        plt.figure(figsize=(8, 5))
        plt.scatter(tmp[xcol], tmp[THROUGHPUT_COL], alpha=0.6, s=40)
        plt.xlabel(xlabel)
        plt.ylabel("DL Throughput (Mbps)")
        plt.title(f"DL Throughput vs {xlabel}")
        plt.grid(True, linestyle="--", alpha=0.35)
        plt.tight_layout()
        plt.savefig(out_dir / f"dl_vs_{short_name}.png", dpi=300)
        plt.close()

def plot_region_panel_near_mid_far(
    regions: Dict[str, pd.DataFrame],
    out_path: Path,
) -> None:
    """
    Creates one figure: 3 rows (Near/Mid/Far) × 4 columns (RSRP/SINR/BLER/MCS)
    Saved as: plots/near_mid_far_vs_kpi.png
    """
    _ensure_dir(out_path.parent)

    region_order = ["Near Cell", "Mid Cell", "Far Cell"]
    kpi_items: Tuple[Tuple[str, Tuple[str, str]], ...] = tuple(KPI_MAP.items())

    fig, axes = plt.subplots(
        nrows=3, ncols=4, figsize=(16, 9), sharey=True
    )

    for r, region in enumerate(region_order):
        df = regions[region]
        for c, (short_name, (xcol, xlabel)) in enumerate(kpi_items):
            ax = axes[r, c]
            tmp = df[[xcol, THROUGHPUT_COL]].dropna()
            ax.scatter(tmp[xcol], tmp[THROUGHPUT_COL], alpha=0.6, s=22)
            if r == 0:
                ax.set_title(xlabel)
            if c == 0:
                ax.set_ylabel(f"{region}\nDL Throughput (Mbps)")
            ax.set_xlabel("")
            ax.grid(True, linestyle="--", alpha=0.25)

    fig.suptitle("Near / Mid / Far: DL Throughput vs KPIs", fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
