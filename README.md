# HybridNMS



# 🚀 Hybrid Self-Healing NMS Prototype

This project implements a **hybrid Network Management System (NMS)** prototype with **self-healing capabilities**.  

It integrates:  
- 🖧 **Mininet** → Network emulation  
- 📊 **Prometheus** → Telemetry collection  
- 🐍 **Custom Python Exporter** → Mininet metrics  
- 📈 **Grafana** → Visualization  
- ⚙️ **Automation Hooks (future)** → Self-healing actions  

---

## ✨ Features

- 🔹 Simulated network topology using **Mininet** (hosts + switches).  
- 🔹 **Exporter** exposes metrics: latency, throughput, packet loss.  
- 🔹 **Prometheus** scrapes metrics via HTTP endpoints.  
- 🔹 **Grafana dashboards** visualize network performance.  
- 🔹 **Fault injection in Mininet** to test MTTR & SLA compliance.  

---

## ⚡ Installation & Setup

### 1️⃣ Enable WSL2 & Virtualization (Windows)

Run the following commands in **PowerShell (Administrator mode):**

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart


