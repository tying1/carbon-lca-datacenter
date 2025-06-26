# 🧠 AI-Powered Data Center Lifecycle Emissions Model

This open-source Python model simulates the **energy usage**, **cooling efficiency**, and **carbon footprint** of a high-performance data center using **NVIDIA AI chips** (e.g., A100). It calculates **Scope 1–3 emissions**, supporting hardware upgrade scenarios and cooling improvements — with assumptions grounded in academic and industry literature.

---

## 📘 Project Overview

This simulation estimates the lifecycle impacts of an AI cluster powered by NVIDIA chips, including:

- GPU power draw and energy consumption
- Cooling and PUE (Power Usage Effectiveness)
- Scope 2 emissions (electricity-related)
- Scope 3 emissions (hardware manufacturing)
- Upgrade cycles and embodied carbon

This project is inspired by real data from Meta's Research SuperCluster (RSC), NVIDIA's energy reports, and academic LCA benchmarks.

## 📁 Folder Structure
```pgsql

/data        → Sample input CSV data, like emissions/chips etc.
/sql         → SQL schema and query files
/src         → Python modules for calculations
/notebooks   → Jupyter notebooks with demo analysis

## ⚙️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/tying1/carbonp-lca-datacenter.git
cd ai-datacenter-lca
```

## 🧠 Background
This tool was developed by a Ph.D. researcher in Environmental Engineering with a deep background in lifecycle assessment (LCA), carbon intensity modeling, and sustainability strategy. It is designed to help data center teams and sustainability engineers evaluate environmental impacts in a transparent and reproducible way.

## 📬 Contact
Feel free to connect via LinkedIn [tianyuying](https://www.linkedin.com/in/tianyu-ying/) or email: tyying@umich.edu  
