# 📊 Interactive Dashboard: NYC Flight Weather Analysis

An interactive Tableau dashboard analyzing wind speed patterns at New York City's three major airports (JFK, LGA, EWR) to support aviation safety and operational planning.

![Tableau](https://img.shields.io/badge/Tableau-Data%20Visualization-blue.svg)
![Dashboard](https://img.shields.io/badge/Type-Interactive%20Dashboard-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🔗 Live Dashboard

**[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/victor.prefa4462/viz/Dasfhboard1/NYCFlightWeatherDashboard)**

## 📋 Overview

The NYC Flight Weather Dashboard is an interactive data visualization platform that provides comprehensive insights into wind speed patterns at major New York City airports. This decision-support tool is designed for aviation professionals, meteorologists, flight planners, and airline operations teams.

### Key Features:
- 📈 **Daily Wind Speed Trends** - Time series visualization for the entire 2013 year
- 📊 **Monthly Averages Table** - Comparative statistics across airports
- 🏆 **Top Windiest Days** - Identification of extreme weather events
- 🔍 **Interactive Filters** - Airport and time-based filtering
- 📉 **Seasonal Patterns** - Visual identification of trends

## 🎯 Dashboard Components

### 1. Daily Mean Wind Speed Chart
- Time series visualization (Jan-Dec 2013)
- Wind speed range: 0-12 m/s
- Interactive tooltips with exact values
- Filterable by airport

### 2. Monthly Average Wind Speed Table
| Month | EWR | JFK | LGA |
|-------|-----|-----|-----|
| January | 4.51 | 5.44 | 5.23 |
| February | 5.61 | 6.03 | 5.65 |
| **March** | **5.19** | **6.15** | **5.85** |
| April | 4.32 | 5.47 | 4.97 |
| May | 3.80 | 4.58 | 4.27 |
| June | 4.18 | 4.86 | 4.36 |
| July | 4.19 | 4.49 | 4.17 |
| **August** | **3.43** | **4.32** | **3.73** |
| September | 3.68 | 4.39 | 3.98 |
| October | 3.68 | 4.61 | 4.57 |
| November | 4.70 | 5.75 | 5.43 |
| December | 3.89 | 4.82 | 4.43 |

### 3. Top Windiest Days at LGA Airport (2013)
| Rank | Date | Wind Speed (m/s) |
|------|------|------------------|
| 1 | November 24, 2013 | 11.47 |
| 2 | January 31, 2013 | 10.77 |
| 3 | March 6, 2013 | 10.22 |
| 4 | February 18, 2013 | 9.86 |
| 5 | February 17, 2013 | 9.65 |
| 6 | February 21, 2013 | 9.24 |
| 7 | May 26, 2013 | 9.00 |
| 8 | March 14, 2013 | 8.92 |
| 9 | November 19, 2013 | 8.66 |
| 10 | February 1, 2013 | 8.23 |

### 4. Monthly Wind Speed Visualization
- Multi-line chart comparing all three airports
- Color-coded: EWR (Red), JFK (Blue), LGA (Green)
- Clear seasonal pattern identification

## 🔬 Key Insights

### Seasonal Patterns
- **March Peak**: Highest wind speeds across all airports (JFK: 6.15 m/s)
- **August Trough**: Lowest wind speeds (EWR: 3.43 m/s)
- **Secondary Winter Peak**: November shows elevated winds
- **Summer Stability**: June-August exhibits consistent, lower wind speeds

### Airport Comparisons
| Airport | Characteristic | Reason |
|---------|---------------|--------|
| **JFK** | Highest winds | Exposed coastal position |
| **LGA** | Intermediate | Moderate coastal exposure |
| **EWR** | Lowest winds | Inland location (New Jersey) |

### Extreme Events
- **Highest Recorded**: 11.47 m/s (November 24, 2013 at LGA)
- **Winter Dominance**: 50% of top 10 windiest days occur in winter
- **February Cluster**: Multiple high-wind days concentrated in February

## 💼 Business Recommendations

### For Airlines

**Operational Planning**
- Schedule maintenance during calm August periods
- Build buffer time into March schedules
- Optimize fuel loads based on seasonal wind patterns

**Airport-Specific Strategy**
- Route wind-sensitive aircraft through EWR when possible
- Maintain extra fuel reserves for JFK operations
- Implement flexible scheduling during peak wind seasons

**Cost Management**
- Budget for higher winter operating costs
- Leverage efficient summer conditions
- Plan major maintenance during low-wind periods

### For Airport Operations

**Safety Protocols**
- Enhanced monitoring November-February
- Specialized winter protocols for ground operations
- Robust wind monitoring during high-risk months

**Infrastructure Planning**
- Consider wind patterns for runway orientations
- Design wind barriers based on historical data
- Plan expansion projects with seasonal wind data

## 🛠️ Technical Details

### Data Source
- **Dataset**: nycflights13_weather
- **Period**: January - December 2013
- **Observations**: 26,130 hourly records
- **Airports**: EWR, JFK, LGA

### Data Processing
1. Extracted from compressed .gz file
2. Cleaned missing values (NaN removal)
3. Converted wind speed: mph → m/s (×0.44704)
4. Aggregated by day and month
5. Calculated statistics per airport

### Tools Used
- **Tableau Public** - Dashboard creation & hosting
- **Python/NumPy** - Data preprocessing
- **Pandas** - Data aggregation

## 📁 Project Structure

```
tableau-nyc-weather-dashboard/
├── README.md
├── documentation/
│   └── DASHBOARD_REPORT.pdf
├── data/
│   └── nycflights13_weather_processed.csv
├── images/
│   ├── dashboard_screenshot.png
│   ├── monthly_chart.png
│   └── windiest_days.png
└── preprocessing/
    └── data_preparation.py
```

## 📸 Dashboard Screenshots

### Main Dashboard View
The interactive dashboard featuring:
- Daily wind speed time series
- Monthly averages table
- Top windiest days ranking
- Multi-airport comparison chart

### Interactive Filters
- Airport selector (EWR, JFK, LGA, All)
- Date range filter
- Dynamic updates across all visualizations

## 🎓 Skills Demonstrated

| Skill | Application |
|-------|-------------|
| **Data Visualization** | Multi-chart dashboard design |
| **Tableau** | Interactive filtering, calculated fields |
| **Business Intelligence** | Actionable insights generation |
| **Data Analysis** | Pattern identification, statistical aggregation |
| **Storytelling** | Visual narrative of weather patterns |
| **Domain Knowledge** | Aviation weather impact analysis |

## 👨‍💼 Author

**Victor Prefa**
- Medical Doctor & Data Scientist
- MSc Data Science & Business Analytics, Deakin University
- Student ID: 225187913
- Email: S225187913@deakin.edu.au

## 📚 References

1. nycflights13 Weather Dataset
2. Tableau Public Documentation
3. NOAA Aviation Weather Standards
4. FAA Wind Speed Guidelines

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Quick Links

- **[Live Dashboard](https://public.tableau.com/app/profile/victor.prefa4462/viz/Dasfhboard1/NYCFlightWeatherDashboard)** - Interact with the visualization
- **[Tableau Public Profile](https://public.tableau.com/app/profile/victor.prefa4462)** - View all my dashboards

---

*This dashboard was developed as part of the Data Science coursework at Deakin University, demonstrating practical data visualization skills for business decision support.*
