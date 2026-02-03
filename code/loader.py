# code/loader.py
from __future__ import annotations

import pandas as pd
from pathlib import Path
from typing import Dict
from .kpis import KPI_MAP, THROUGHPUT_COL

def load_excel(path: Path) -> pd.DataFrame:
    """Load one Excel file and coerce KPI columns to numeric."""
    df = pd.read_excel(path)

    required_cols = [THROUGHPUT_COL] + [col for col, _ in KPI_MAP.values()]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns in {path.name}: {missing}\n"
            f"Available columns: {list(df.columns)}"
        )

    # Convert required columns to numeric
    for c in required_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Drop rows where throughput is missing (can't plot)
    df = df.dropna(subset=[THROUGHPUT_COL]).reset_index(drop=True)
    return df

def load_regions(dataset_dir: Path) -> Dict[str, pd.DataFrame]:
    """Load Near/Mid/Far region datasets."""
    files = {
        "Near Cell": dataset_dir / "near_cell.xlsx",
        "Mid Cell":  dataset_dir / "mid_cell.xlsx",
        "Far Cell":  dataset_dir / "far_cell.xlsx",
    }

    for name, p in files.items():
        if not p.exists():
            raise FileNotFoundError(f"Expected dataset file not found: {p}")

    return {region: load_excel(path) for region, path in files.items()}

def load_all_combined(regions: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Combine all regions into one DataFrame for overall (individual) plots."""
    out = []
    for region, df in regions.items():
        tmp = df.copy()
        tmp["Region"] = region
        out.append(tmp)
    return pd.concat(out, ignore_index=True)
