#5G NR KPI Definitions

This document provides detailed explanations of key performance indicators(KPIs) used in 5G NR performance analysis and troubleshooting.

---
## SINR(Signal-to-Interferene-plus-Noise Ration)
SINR represents the ratio of the desired signal power to the sum of interference and noise. It is a primary indicator of channel quality and directly influences scheduler decisions, including MCS selection and achievable throughput.
| SINR Range (dB) | RF Quality | Expected Impact |
|-----------------|------------|-----------------|
| > 20 dB | Excellent | High MCS selection, low BLER, high throughput |
| 13 – 20 dB | Good | Stable MCS, good throughput |
| 5 – 12 dB | Fair | Reduced MCS, moderate BLER, throughput degradation |
| < 5 dB | Poor | Low MCS, high BLER, frequent retransmissions |

**Correlation:**  
Lower SINR limits the scheduler’s ability to select higher MCS, leading to reduced
spectral efficiency and throughput.

---
### MCS (Modulation and Coding Scheme)
MCS defines the modulation order and coding rate selected by the gNB scheduler.
| MCS Range | Interpretation |
|----------|----------------|
| 20 – 28 | High spectral efficiency (good RF conditions) |
| 10 – 19 | Moderate efficiency |
| < 10 | Robust transmission for poor RF |

**Correlation:**  
MCS is dynamically adjusted based on SINR and BLER targets. When RF degrades, the scheduler lowers MCS to maintain decoding reliability.

---
## BLER (Block Error Rate)
BLER indicates the percentage of transport blocks that fail decoding.
| BLER (%) | Link Condition |
|---------|----------------|
| < 5% | Healthy link |
| 5 – 10% | Acceptable |
| 10 – 20% | Degraded |
| > 20% | Poor / unstable |

**Correlation:**  
High BLER triggers HARQ retransmissions, increasing latency and reducing
effective throughput.

---
### Throughput (DL / UL)
Throughput represents the successfully delivered data rate over the air interface. It is a combined outcome of radio conditions, scheduler behaviour, and retransmission mechanisms.
| Throughput Level | Interpretation |
|------------------|----------------|
| Near peak | Good RF, high MCS, low BLER |
| Moderate | Average RF or scheduler constraints |
| Low | Poor RF, low MCS, high BLER |

**Correlation:**  
Throughput is a combined outcome of SINR, MCS selection, BLER behaviour, and available resource allocation.



























