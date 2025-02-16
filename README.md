# Indian Election Data Analysis

## Overview
This project conducts an exploratory data analysis (EDA) on the Indian election dataset. The goal is to clean, preprocess, and analyze the dataset to extract meaningful insights.

## Dataset
- **File:** `indian_election_dataset.csv`
- **Contents:** Information about election candidates, their constituencies, party affiliations, and demographic details.

## Steps Performed
1. **Loading the Dataset**
   - Used `pandas` to read the dataset.
2. **Handling Missing Values**
   - Filled missing values for certain categorical columns.
   - Dropped remaining rows with NULL values.
3. **Data Cleaning**
   - Processed categorical variables like `pc_type` and `cand_sex`.
4. **Exploratory Data Analysis (EDA)**
   - Summary statistics and distributions.
   - Visualizations to understand trends and patterns.

## Requirements
- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Indian_election_eda.ipynb
   ```

## Output & Insights
- The analysis helps understand election trends, candidate demographics, and party-wise distributions.
- Visual representations provide a clear view of key statistics.

## Author
Ronojit Shil

## License
This project is open-source under the MIT License.
