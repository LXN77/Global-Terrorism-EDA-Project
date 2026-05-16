# Global Terrorism Data Analysis (Asia Focus)

This project performs a comprehensive, end-to-end Exploratory Data Analysis (EDA) and Statistical Hypothesis Testing on the Global Terrorism Database (GTD). The analysis focuses deeply on the volatility, tactical preferences, and casualty trends across Asian regions between 1970 and 2017.

## Project Executive Summary
* **The 2014 Conflict Peak:** Terrorist incidents in Asia experienced a massive surge during 2010–2014, peaking at 13,071 attacks in 2014. This correlates directly with intense geopolitical instability in the Middle East and South Asia.
* **Tactical Lethality Distribution:** High-impact mass-casualty events heavily skew terrorism data. While 75% of incidents result in 2 or fewer fatalities, rare catastrophic attacks dominate the total human toll.
* **Suicide vs. Non-Suicide Metrics:** Statistical modeling and violin plot visualizations confirm that suicide attacks consistently achieve far higher average operational casualty rates than non-suicide tactics.

## Repository Structure
* `data/processed data/`: Contains the cleaned, filtered macro-features (`gtd_asia_cleaned.csv` and `gtd_log.csv`) for the Asian continent.
* `notebooks/01_data_cleaning.ipynb`: Pipeline for data transformation, column mappings, and missing/invalid entry imputations.
* `notebooks/02_eda_asia.ipynb`: Deep-dive data visualization (univariate, bivariate, multivariate) and downstream statistical verification.

## Statistical Validation (Hypothesis Testing)
The project utilizes robust inference testing directly within the EDA flow to prove that tactical trends are mathematically non-random:
1. **Attack Type vs. Success Rate (Chi-Square Test):** Rejected the null hypothesis ($p \approx 0.0$), confirming that tactical choice significantly determines operational reliability (${\chi}^2 = 5036.78$).
2. **Impact of Attack Strategy on Human Casualties (One-Way ANOVA):** Evaluated via log-transformed metrics ($F\text{-statistic} = 965.59, p \approx 0.0$), validating that explosive-based methods produce statistically superior lethality patterns compared to facility attacks or hostage-taking.

## How to Run this Project Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/Global-Terrorism-EDA-Project-Final.git](https://github.com/your-username/Global-Terrorism-EDA-Project-Final.git)
cd Global-Terrorism-EDA-Project-Final
```

### 2. Download the Dataset Safely

Due to the strict End-User License Agreement of the Global Terrorism Database, the raw data cannot be hosted publicly in this repository.

* Download the raw source data file from [Kaggle's Global Terrorism Dataset](https://www.kaggle.com/datasets/START-UMD/gtd).
* Place the file inside your local `data/raw data/` directory as `global_terrorism.csv`.

### 3. Install Dependencies

Ensure your environment (`.myenv`) is active, then run:

```bash
pip install -r requirements.txt

```

## Legal & Citation Attribution

Data sourced via the National Consortium for the Study of Terrorism and Responses to Terrorism (START).

> *National Consortium for the Study of Terrorism and Responses to Terrorism (START), University of Maryland. (2018). The Global Terrorism Database (GTD) [Data file]. Retrieved from https://www.start.umd.edu/gtd*

```

```