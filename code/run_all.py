# code/run_all.py
from __future__ import annotations

from pathlib import Path

# Local imports
from loader import load_regions, load_all_combined
from plots import plot_individual_kpis, plot_region_panel_near_mid_far

def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    dataset_dir = repo_root / "dataset"
    plots_dir = repo_root / "plots"

    # 1) Load data
    regions = load_regions(dataset_dir)
    df_all = load_all_combined(regions)

    # 2) Identify KPIs (handled by kpis.py implicitly)

    # 3) Plot
    plot_individual_kpis(df_all, plots_dir / "individual")
    plot_region_panel_near_mid_far(regions, plots_dir / "near_mid_far_vs_kpi.png")

    print("✅ Done. Generated plots:")
    print(f" - {plots_dir / 'near_mid_far_vs_kpi.png'}")
    print(f" - {plots_dir / 'individual'}/*.png")

if __name__ == "__main__":
    main()
