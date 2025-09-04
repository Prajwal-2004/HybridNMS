# HybridNMS



\# Hybrid Self-Healing NMS Prototype



This project implements a hybrid Network Management System (NMS) prototype with self-healing capabilities. It integrates:



\- \*\*Mininet\*\* (network emulation)

\- \*\*Prometheus\*\* (telemetry collection)

\- \*\*Custom Python Exporter\*\* (for Mininet metrics)

\- \*\*Grafana\*\* (visualization)

\- \*\*Automation hooks (future)\*\* for self-healing.



---



\## Features



\- Simulated network topology using Mininet (hosts + switches).

\- Exporter exposes metrics on latency, throughput, packet loss.

\- Prometheus scrapes metrics via HTTP.

\- Grafana dashboards visualize performance.

\- Fault injection in Mininet to test MTTR and SLA compliance.



---



\## Installation \& Setup



\### 1. Enable WSL2 and Virtualization

```powershell

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart



