# AI-Powered Job Market and Skill Demand Analyzer

A beginner-friendly Data Science project that explores job-posting data to identify frequently requested skills, compare job roles, and visualize hiring patterns.

> **Project status:** Starter repository / planning stage. Results and model performance will be added only after the analysis is implemented and validated.

## Objectives
- Inspect and clean a permitted job-postings dataset.
- Explore job titles, locations, experience levels, and salary fields when available.
- Identify commonly mentioned technical skills using a transparent keyword dictionary.
- Visualize skill demand and compare patterns across roles.
- Present findings in a simple Streamlit dashboard (planned next stage).

## Project workflow
1. Define the analysis questions.
2. Obtain a public or openly licensed dataset and document its source.
3. Clean missing values, duplicates, and inconsistent fields.
4. Perform exploratory data analysis (EDA).
5. Extract and validate skill mentions.
6. Build charts and a dashboard.
7. Document findings, limitations, and reproducibility steps.

## Repository structure
```text
job-market-skill-demand-analyzer/
├── data/                 # Put permitted dataset files here; avoid committing large/private data
├── notebooks/            # Jupyter notebooks for exploration
├── src/
│   └── analyze_jobs.py   # Starter analysis functions
├── visuals/              # Exported charts
├── reports/              # Project plan and final report
├── app.py                # Streamlit dashboard
├── requirements.txt
└── README.md
```

## Setup
Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Dataset format
The starter code expects a CSV file with at least a `description` column. Optional columns include `title`, `location`, `company`, and `salary`. You can update the column names in `src/analyze_jobs.py` to match the dataset you choose.

Place the dataset at `data/job_postings.csv`. Check the source's license and terms before using or sharing it. Do not scrape sites in ways that violate their terms or access restrictions.

## Run the starter analysis
```bash
python src/analyze_jobs.py --input data/job_postings.csv --output visuals
```

If the dataset is not available yet, run the app with its built-in demo sample:
```bash
streamlit run app.py
```

## Limitations
- Skill counts indicate mentions in the selected dataset, not the entire job market.
- Keyword matching can miss synonyms or create false matches; review a sample manually.
- Salary comparisons are meaningful only when currency, period, and units are clear.
- This project is for learning and career exploration, not hiring decisions or guaranteed job outcomes.

## Planned deliverables
- Documented dataset source and cleaning decisions
- EDA charts
- Skill frequency analysis
- Interactive Streamlit dashboard
- Final report with methods, findings, and limitations

## Author
Add your name and internship details here before publishing.
