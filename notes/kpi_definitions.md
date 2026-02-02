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
