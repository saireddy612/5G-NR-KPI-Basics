# code/kpis.py

# ---- Required KPI column names (must match Excel exactly) ----
COL_RSRP = "5G KPI PCell RF Serving SS-RSRP [dBm]"
COL_SINR = "5G KPI PCell RF Serving SS-SINR [dB]"
COL_DLBLER = "5G KPI PCell Layer1 DL BLER [%]"
COL_DLMCS = "5G KPI PCell Layer1 DL MCS (Avg)"
COL_DLTPUT = "5G KPI Total Info Layer1 PDSCH Throughput [Mbps]"

# For plotting (labeling)
KPI_MAP = {
    "rsrp": (COL_RSRP, "SS-RSRP (dBm)"),
    "sinr": (COL_SINR, "SS-SINR (dB)"),
    "dlbler": (COL_DLBLER, "DL BLER (%)"),
    "dlmcs": (COL_DLMCS, "DL MCS (Avg)"),
}

THROUGHPUT_COL = COL_DLTPUT
