# GeoInflate  
## Micro Inflation Intelligence System

## Deployed via Streamlit: https://geoinflate.streamlit.app/

GeoInflate is a data analytics based web application designed to track and analyze inflation at a personal and city level. The system focuses on micro-level inflation intelligence using user-generated expense data and geo-spatial visualization.

The project combines:
- Expense tracking
- Inflation calculation
- Geo-based analytics
- Visualization dashboards
- Rule-based insights

---

# 🚀 Features

## ✅ Expense Tracking
Users can:
- Add expense details
- Track monthly spending
- Analyze item-wise expenses

---

## ✅ Personal Inflation Rate
The system calculates:
- Month-to-month inflation percentage
- Expense growth trends
- Personal inflation metrics

---

## ✅ Geo-Spatial Inflation Map
Interactive India map with:
- City-wise inflation markers
- Color-coded inflation intensity
- Inflation hotspot visualization

---

## ✅ Shrinkflation Detection
The system flags abnormal inflation patterns that may indicate:
- Quantity reduction
- Hidden price increase
- Packaged goods inflation

---

## ✅ CPI Gap Analysis
Compares:
- Personal inflation
- Official CPI values

This helps identify the difference between user experience and government-reported inflation.

---

## ✅ PIVS Score
Personal Inflation Vulnerability Score indicates how vulnerable a user is to rising inflation.

---

## ✅ AI Insights
Rule-based insights are generated based on:
- Inflation trends
- Spending changes
- Risk levels

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Web application |
| Pandas | Data processing |
| Plotly | Charts and visualization |
| Folium | Geo-spatial maps |
| Streamlit-Folium | Map integration |

---

# 📂 Project Structure

```plaintext
GeoInflate/
│
├── app.py
├── data.csv
├── india_map_data.csv
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Used

The project currently uses:
- User-generated expense data
- Sample city-wise inflation data

### Dataset Fields
- City
- Item
- Price
- Quantity
- Month
- Inflation values

---

# ⚙️ Algorithms Used

## Expense Calculation

```plaintext
Total Expense = Price × Quantity
```

## Inflation Calculation

```plaintext
Inflation (%) =
(Current Expense − Previous Expense)
÷ Previous Expense × 100
```

## Price vs Consumption Analysis
- Price Effect
- Consumption Effect

---

# 🌍 Geo-Spatial Analysis

The system visualizes inflation across cities using:
- 🟢 Green → Low inflation
- 🟠 Orange → Moderate inflation
- 🔴 Red → High inflation

---

# 📈 Output

The application provides:
- KPI dashboard
- Expense trend charts
- Geo inflation map
- Inflation insights
- PIVS score
- CPI gap analysis

---

# 🎯 Objectives

- To track personal inflation trends
- To visualize expense changes
- To analyze inflation geographically
- To build a scalable analytics platform
- To improve awareness of inflation impact

---

# 🔥 Novelty

GeoInflate combines:
- Personal expense tracking
- Inflation analytics
- Geo-spatial mapping
- Shrinkflation detection
- Insight generation

into a single platform.

---

# 🚀 Future Enhancements

- Real-time inflation datasets
- AI-based prediction models
- Multi-sector expansion
- Backend database integration
- Mobile application support
- District-level geo analytics

---

# ▶️ Run Locally

## Install Requirements

```bash
py -m pip install -r requirements.txt
```

## Run Streamlit App

```bash
py -m streamlit run app.py
```

---

# 📌 Developed As

Mini Project – Data Analytics / Inflation Intelligence System
