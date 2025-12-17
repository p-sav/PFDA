# Home Energy Analytics - Micro Renewable Energy System  

## Generation, Tariffs, Export & Battery Optimisation

This is a data analytics project that uses **30 minute smart meter data** to analyse residential grid electricity usage, compare different tariff structures, and evaluate the best operational strategy when using a **Micro Renewable Energy System**.

The project specifically investigates whether it is **more financially beneficial to export surplus energy to the grid** or **store it in a home battery for later use**, taking into account:

- Time of use electricity tariffs  
- Night rate EV charging  
- Export feed in tariffs  
- Household occupancy patterns  
- Battery charging and discharging strategies  

The aim is to determine the **most cost effective energy management strategy** for modern homes with solar PV, EV charging, and smart metering.

- Household occupancy patterns  
- Battery charging and discharging strategies

---

### Project Overview

This project analyses real and synthetic household electricity consumption data to:

- Compare **electricity tariff plans**
- Evaluate **export vs self-consumption**
- Assess the **financial viability of home battery storage**
- Understand how **occupancy patterns affect energy costs**

The project is designed as a **practical energy economics case study** for modern homes with:

- Smart meters  
- Solar PV  
- EV charging  
- Time-of-use electricity tariffs  

---

### Objectives

- Analyse 30 minute interval electricity data over a full year
- Compare:
  - Day / Night / Peak tariffs
  - 24-Hour flat rate tariffs
  - Night Boost EV tariffs
- Evaluate:
  - Annual electricity cost
  - Export revenue
  - Net annual spend
- Compare:
  - Battery storage vs grid export
  - Physical battery vs grid as a “virtual battery"
- Determine:
  - Battery payback period
  - ROI (Return on Investment)
  - Most cost-effective energy strategy

---

### Case Studies

#### Case Study 1 - All Day Occupancy

Case Study 1 uses real household electricity consumption data from a home that is occupied all day. The household has a solar PV system installed on the roof, generating electricity during daylight hours. This scenario represents a high daytime demand profile, where most solar generation is self-consumed, resulting in limited surplus energy for export to the grid.

- High consumption throughout the day
- Most solar generation is instantly self consumed
- Limited surplus export
- Battery value may be reduced

Used to study:

- Direct self-consumption efficiency
- Battery value when daytime usage is already high

---

### Case Study 2 - Away working 9am to 5pm (EV Household)

Case Study 2 is synthetic. It assumes the same premises and the same solar PV system as Case Study 1, but the household is unoccupied from 9am to 5pm and includes EV charging at night. This creates a realistic scenario with low daytime demand and higher solar surplus, allowing export to grid and battery storage strategies to be compared under identical PV conditions.

- Low daytime usage
- High evening peak (5:30pm–7:30pm)
- High night usage for EV charging
- Solar generation occurs when the house is empty

Used to study:

- Export vs battery storage
- Night Boost EV charging optimisation
- Load shifting strategies

---

### Data Structure

Each dataset contains:

- One full year of data  
- 48 × 30 minute data intervals per day  
- Columns:
  - `Date`
  - `00:00` → `23:30` half-hour kWh values
- Annual energy totals calculated directly from raw interval data

---

### Tariffs Analysed

- Day / Night / Peak
- 24-Hour Flat Rate
- Night Boost (2am to 4am lower rate window)
- Peak day rate (5pm to 7pm – higher rate window)
- Export CEG Feed in grid tariffs
- Annual Standing Charges

Each tariff is evaluated using:

- Import cost
- Export revenue
- Net annual electricity cost

---

### Battery vs Grid Analysis

This project evaluates:

- Charging strategies:
  - Solar charging
  - Night tariff charging

- Discharge strategies:
  - Evening peak offset

- Comparison between:
  - Owning a battery
  - Exporting energy and re importing later

The analysis determines:

- Battery payback period
- Long term savings
- Whether grid export is financially superior to battery ownership

---

### Key Questions Answered

- Is it cheaper to **store energy or sell it to the grid?**
- Do batteries make financial sense **without grants or subsidies?**
- How does **lifestyle behaviour affect electricity cost?**
- Does **Night Boost EV charging outperform standard night tariffs?**
- Which tariff is optimal for each household profile?
