import matplotlib.pyplot as plt
from load_data import load_kpi_file

FILES = {
    "Near Cell": "dataset/near_cell.xlsx",
    "Mid Cell": "dataset/mid_cell.xlsx",
    "Far Cell": "dataset/far_cell.xlsx",
}

KPIS = {
    "RSRP": "5G KPI PCell RF Serving SS-RSRP [dBm]",
    "SINR": "5G KPI PCell RF Serving SS-SINR [dB]",
    "DL BLER": "5G KPI PCell Layer1 DL BLER [%]",
    "DL MCS": "5G KPI PCell Layer1 DL MCS (Avg)",
}

TPUT = "5G KPI Total Info Layer1 PDSCH Throughput [Mbps]"

fig, axes = plt.subplots(3, 4, figsize=(16, 9), sharey=True)

for r, (region, path) in enumerate(FILES.items()):
    df = load_kpi_file(path)
    for c, (kpi, col) in enumerate(KPIS.items()):
        axes[r, c].scatter(df[col], df[TPUT], alpha=0.6)
        axes[r, c].set_title(f"{region} – {kpi}")

plt.tight_layout()
plt.savefig("plots/near_mid_far_vs_kpi.png", dpi=300)
