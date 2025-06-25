# 🖥️ Data Center LCA Modeling Tool

This project estimates the **lifecycle carbon footprint (CI score)** of data center hardware under different replacement scenarios (e.g., 3-year vs. 5-year refresh cycles). 
It combines LCA expertise with Python and SQL to model and visualize sustainability trade-offs.

## 🧭 Project Modules

### 📦 Data Center CI Calculator
Located in `/src/`, this module estimates the lifecycle CI score for hardware replacement scenarios in cloud infrastructure.

### ♻️ Biogas Lifecycle Calculator
Located in `/biogas_lca/`, this submodule estimates the carbon intensity of dairy manure-based biogas pathways under different conditions (e.g., lagoon covers, digesters, RNG conversion).

## 🔧 Features

- ✅ CI (Carbon Intensity) calculator using Python
- ✅ SQL-based lifecycle inventory for emission factors
- ✅ Visualizations of cumulative carbon emissions over time
- ✅ Supports scenario comparisons (refresh every 3 vs 5 years)

## 🚀 Getting Started

1. Clone the repository

```bash
git clone https://github.com/tying1/carbon-lca-datacenter.git
cd carbon-lca-datacenter 
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the model

```bash

python src/ci_calculator.py
```
4. Open the Jupyter notebook demo

```bash

jupyter notebook notebooks/lca_demo.ipynb
```

## 📁 Folder Structure
```pgsql

/data        → Input CSVs (e.g., hardware, emission factors)
/sql         → SQL schema and query files
/src         → Python modules for calculations
/notebooks   → Jupyter notebooks with demo analysis
```

## 🧠 Background
This tool was developed by a Ph.D. researcher in Environmental Engineering with a deep background in lifecycle assessment (LCA), carbon intensity modeling, and sustainability strategy. It is designed to help data center teams and sustainability engineers evaluate environmental impacts in a transparent and reproducible way.

## 📬 Contact
Feel free to connect via LinkedIn [tianyuying](https://www.linkedin.com/in/tianyu-ying/) or email: tyying@umich.edu  
