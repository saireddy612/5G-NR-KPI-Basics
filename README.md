# 5G NR KPI vs Throughput Analysis (Near / Mid / Far Cell)

This project analyses the relationship between critical 5G NR KPIs and downlink
throughput across Near, Mid, and Far cell conditions. The objective is to
understand how RF quality and link reliability influence user-plane performance
in a live network environment.

---

## Cell Range Definition

Cell conditions are classified using SS-RSRP thresholds:

- **Near Cell:** SS-RSRP ≥ −75 dBm  
- **Mid Cell:** SS-RSRP between −95 dBm and −98 dBm  
- **Far Cell:** SS-RSRP between −108 dBm and −110 dBm  

---

## Throughput and KPI Behaviour Across Cell Regions

![Near / Mid / Far KPI Panel](https://github.com/saireddy612/5G-NR-KPI-Basics/blob/b85c969fb73e567050da66cd79961a7812026865/plots/near_mid_far_vs_kpi.png)

This figure summarises how downlink throughput behaves across Near, Mid, and Far
cell regions in a live 5G NR network. Cell regions are defined using SS-RSRP
thresholds, while throughput behaviour is explained through the combined impact
of signal quality, interference, and link reliability KPIs.

Rather than evaluating KPIs independently, this panel highlights how their
interaction governs throughput as RF conditions degrade.

---

### Near Cell Region

In the near cell region, throughput remains consistently high with relatively
tight clustering. Strong RF conditions enable high SINR and low DL BLER, allowing
the scheduler to sustain higher DL MCS levels.

While minor throughput variation exists, it is not driven by RF limitations.
Instead, throughput remains largely stable because link reliability is
maintained and aggressive MCS selection is feasible.

**Interpretation:**  
Throughput performance in near cell conditions is enabled by high SINR and low
BLER, with RSRP primarily serving as coverage context rather than a limiting
factor.

---

### Mid Cell Region

In the mid cell region, throughput variability increases noticeably. Although
RSRP remains adequate, SINR begins to fluctuate due to increased interference.
These SINR variations lead to intermittent increases in DL BLER.

As BLER rises, the scheduler adapts by lowering DL MCS more frequently, which
introduces visible throughput spread and sensitivity to short-term RF changes.

**Interpretation:**  
Throughput in the mid cell region is no longer governed by signal strength alone,
but by interference-driven SINR variability and its impact on BLER and MCS
selection.

---

### Far Cell Region

In the far cell region, throughput degradation becomes pronounced. Despite the
presence of measurable signal strength, SINR is consistently low and DL BLER
increases significantly.

High BLER results in repeated retransmissions and constrains DL MCS to lower
values, leading to frequent low or near-zero throughput events. At this stage,
throughput collapse is dominated by link reliability rather than coverage alone.

**Interpretation:**  
Throughput in far cell conditions is limited by decoding reliability and
conservative MCS selection, not by the absence of signal strength.

---

### Cross-Region Throughput Insight

Across Near, Mid, and Far cell regions, throughput degradation follows a clear
progression in dominant limiting factors:

- **Near Cell:** Throughput enabled by high SINR and low BLER  
- **Mid Cell:** Throughput constrained by SINR variability and rising BLER  
- **Far Cell:** Throughput limited by persistent high BLER and low MCS  

This progression demonstrates that downlink throughput in live networks is not
directly proportional to signal strength. Instead, throughput is governed by the
combined interaction of SINR, BLER, and MCS as RF conditions degrade.

---

### Key Takeaway

Downlink throughput behaviour across cell regions reflects a shift from
coverage-enabled performance to interference- and reliability-limited
performance. RSRP provides location context, but SINR and BLER determine whether
higher MCS can be sustained, ultimately defining achievable throughput.
