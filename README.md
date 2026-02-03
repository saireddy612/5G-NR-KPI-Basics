# 5G NR KPI vs Throughput Analysis (Near / Mid / Far Cell)

This project analyses the relationship between critical 5G NR KPIs and downlink throughput across Near, Mid, and Far cell conditions. The objective is to understand how RF quality and link reliability influence user-plane performance in a controlled test environment.

---

## Cell Range Definition

Cell conditions are classified using SS-RSRP thresholds:

- **Near Cell:** SS-RSRP ≥ −75 dBm  
- **Mid Cell:** SS-RSRP between −95 dBm and −98 dBm  
- **Far Cell:** SS-RSRP between −108 dBm and −110 dBm  

These ranges are used consistently across all visualisations and comparisons.

---

## KPIs Analysed

- **SS-RSRP:** Signal strength and coverage indicator  
- **SS-SINR:** Signal quality and interference indicator  
- **DL BLER:** Downlink block error rate, indicating link reliability  
- **DL MCS:** Downlink modulation and coding scheme (spectral efficiency)  
- **DL Throughput:** User-plane downlink data rate (performance metric)

---
## Region-wise KPI Impact (Near / Mid / Far)

![Near Mid Far KPI Panels](near_mid_far_vs_kpi.png)

### What this image shows
This stacked figure presents Near, Mid, and Far cell conditions derived from live
network data. Each region contains four subplots showing downlink throughput
versus RSRP, SINR, DL BLER, and DL MCS.

### What is happening
- **Near Cell:** High SINR and low BLER allow the scheduler to select higher MCS,
  resulting in stable and high throughput.
- **Mid Cell:** Throughput becomes more variable as SINR fluctuates due to
  interference and network load.
- **Far Cell:** Throughput collapse is dominated by high BLER and constrained MCS
  selection, even when signal strength is still measurable.

### Key takeaway
In real networks, throughput degradation from Near to Far cell is driven by
interference and decoding reliability rather than coverage alone.

---

## DL Throughput vs SINR

![SINR vs DL Throughput](SINR VS TPUT.png)

### What this image shows
This plot visualizes the relationship between SS-SINR and downlink throughput
using field-collected data.

### What is happening
Higher SINR values consistently align with higher throughput, while low SINR
conditions result in reduced and unstable throughput. SINR captures the combined
effect of signal quality, inter-cell interference, and noise.

### Impact on throughput
SINR directly influences whether higher-order modulation and coding schemes can
be sustained. Poor SINR increases error probability, forcing the scheduler to
reduce MCS and limiting achievable throughput.

**SINR is the strongest predictor of throughput in field conditions.**

---

## DL Throughput vs RSRP

![RSRP vs DL Throughput](RSRP VS TPUT.png)

### What this image shows
This plot compares SS-RSRP against downlink throughput using live network data.

### What is happening
Although higher RSRP generally corresponds to better performance, significant
throughput spread exists at similar RSRP levels.

### Impact on throughput
RSRP reflects coverage but does not account for interference or scheduler load.
As a result, similar signal strength values can produce very different throughput
outcomes depending on SINR and BLER.

**RSRP provides coverage context but is not a reliable performance predictor.**

---

## DL Throughput vs DL BLER

![DL BLER vs DL Throughput](BLER VS TPUT.png)

### What this image shows
This plot highlights the inverse relationship between DL BLER and throughput
under live network conditions.

### What is happening
As BLER increases, throughput drops sharply, with frequent near-zero throughput
events observed especially in far cell scenarios.

### Impact on throughput
High BLER indicates repeated decoding failures and retransmissions, which reduce
effective data delivery. Even moderate BLER levels can significantly degrade
throughput in real networks.

**BLER acts as a dominant throughput-limiting factor in degraded RF conditions.**

---

## DL Throughput vs DL MCS

![DL MCS vs DL Throughput](MCS VS TPUT.png)

### What this image shows
This plot shows how DL MCS selection correlates with achievable throughput.

### What is happening
Higher MCS values align with higher throughput in near and mid cell conditions.
In far cell conditions, persistent low SINR and elevated BLER constrain the
scheduler to lower MCS selections.

### Impact on throughput
MCS represents the scheduler’s adaptation to real-time RF and BLER feedback.
Lower MCS directly limits spectral efficiency and throughput regardless of
available radio resources.

**MCS is the practical bridge between RF conditions and throughput.**

---

## Final KPI Correlation Analysis

Using field data from a live 5G network, this analysis shows that downlink
throughput is primarily governed by SINR and BLER rather than signal strength
alone. RSRP provides coverage awareness, but SINR determines error behavior,
BLER reflects decoding reliability, and MCS translates these conditions into
achievable data rates.

Throughput degradation from Near to Far cell is driven by increasing interference,
scheduler conservatism, and link reliability constraints.

---

## Note on PRB Allocation

PRB allocation is intentionally not included in this analysis. PRBs are a
scheduler output rather than a root-cause KPI and depend heavily on cell load,
QoS configuration, and traffic conditions. This project focuses on RF and
link-layer indicators that directly influence scheduler decisions. PRB behavior
is planned as a follow-up analysis.

---

## Data Disclaimer

All data used in this project is anonymized and contains only numeric KPI values.
No device identifiers, chipset information, software versions, network IDs, or
vendor-specific configurations are included.


# 5G NR Throughput Behavior — Field Data Analysis

> **What this shows:**  
> How real 5G NR downlink throughput behaves in a live network as RF and link
> conditions degrade from Near → Mid → Far cell.

---

## 🔍 What’s Different About This Project
- ✅ Uses **field data from a live commercial network**
- ✅ Captures **real interference, scheduler behavior, and mobility**
- ❌ No lab isolation or artificial RF control
- 🎯 Focuses on **why throughput changes**, not just what changes

---

## 📍 Cell Regions (Field-Based)

| Region | SS-RSRP Range |
|------|---------------|
| Near Cell | ≥ −75 dBm |
| Mid Cell | −95 to −98 dBm |
| Far Cell | −108 to −110 dBm |

> These regions are used consistently across all visualizations.

---

## 🧠 KPIs in One Line (No Theory)

- **RSRP** → coverage  
- **SINR** → interference quality  
- **BLER** → decoding reliability  
- **MCS** → spectral efficiency  
- **Throughput** → user experience  

---

## 🧩 Big Picture: What Happens as RF Degrades?

![Near Mid Far KPI Panels](near_mid_far_vs_kpi.png)

### What you should notice
- **Near Cell:** high throughput, tight clustering
- **Mid Cell:** throughput spread increases
- **Far Cell:** frequent throughput collapse

### Why it happens
> The limiting factor shifts from **coverage → interference → decoding reliability**

---

## 🎯 KPI Impact — One by One

---

### 🔶 SINR → The Main Throughput Driver
![SINR vs DL Throughput](SINR VS TPUT.png)

**Pattern**
- Higher SINR → consistently higher throughput
- Low SINR → unstable, collapsing throughput

**Why**
- SINR governs whether higher MCS can be sustained

**Takeaway**
> If SINR is poor, throughput will suffer — even with good signal strength.

---

### 🔷 RSRP → Coverage, Not Performance
![RSRP vs DL Throughput](RSRP VS TPUT.png)

**Pattern**
- Similar RSRP → very different throughput outcomes

**Why**
- RSRP ignores interference and scheduler contention

**Takeaway**
> RSRP tells you *where* you are, not *how fast* you’ll go.

---

### 🔴 BLER → Throughput Killer
![DL BLER vs DL Throughput](BLER VS TPUT.png)

**Pattern**
- Rising BLER → sharp throughput drop
- Near-zero throughput at high BLER

**Why**
- Retransmissions dominate link behavior

**Takeaway**
> BLER is where RF problems turn into real user pain.

---

### 🟢 MCS → The Translation Layer
![DL MCS vs DL Throughput](MCS VS TPUT.png)

**Pattern**
- Higher MCS → higher throughput
- Far cell stuck at low MCS

**Why**
- Scheduler adapts MCS based on SINR + BLER

**Takeaway**
> MCS converts RF quality into actual data rates.

---

## 🔗 The Correlation Chain (This Is the Core Insight)

```text
RSRP  →  SINR  →  BLER  →  MCS  →  Throughput
coverage  quality  reliability  efficiency  experience
