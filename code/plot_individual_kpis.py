import matplotlib.pyplot as plt
import pandas as pd

files = [
    "dataset/near_cell.xlsx",
    "dataset/mid_cell.xlsx",
    "dataset/far_cell.xlsx",
]

df = pd.concat([pd.read_excel(f) for f in files])
df = df.apply(pd.to_numeric, errors="coerce")

TPUT = "5G KPI Total Info Layer1 PDSCH Throughput [Mbps]"
KPIS = {
    "sinr": "5G KPI PCell RF Serving SS-SINR [dB]",
    "rsrp": "5G KPI PCell RF Serving SS-RSRP [dBm]",
    "dlbler": "5G KPI PCell Layer1 DL BLER [%]",
    "dlmcs": "5G KPI PCell Layer1 DL MCS (Avg)",
}

for name, col in KPIS.items():
    plt.figure()
    plt.scatter(df[col], df[TPUT], alpha=0.6)
    plt.xlabel(col)
    plt.ylabel("DL Throughput (Mbps)")
    plt.tight_layout()
    plt.savefig(f"plots/individual/dl_vs_{name}.png", dpi=300)
