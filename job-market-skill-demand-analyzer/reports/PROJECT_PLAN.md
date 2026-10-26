# Week 1 Project Plan

**Project:** AI-Powered Job Market and Skill Demand Analyzer  
**Purpose:** Explore a permitted job-postings dataset to identify frequently mentioned skills and compare patterns across roles and locations.

## Problem statement
Job seekers may find it difficult to compare the skills requested across many job postings. This project will organize available job-posting information and summarize skill mentions through transparent data analysis.

## Objectives
- Inspect and clean a job-postings dataset.
- Perform exploratory data analysis.
- Extract common skill mentions using a documented keyword dictionary.
- Visualize patterns by skill, role, and location where fields are available.
- Present findings and limitations in a simple dashboard and report.

## Planned workflow
Dataset selection → data quality checks → cleaning → EDA → skill extraction → validation → visualization/dashboard → report.

## Estimated effort (33 hours)
| Activity | Hours |
|---|---:|
| Define problem and scope | 3 |
| Dataset research and source review | 4 |
| Data inspection and cleaning | 5 |
| EDA and chart planning | 5 |
| Skill extraction and validation | 5 |
| Dashboard design | 4 |
| Risk review and documentation | 4 |
| Final review | 3 |
| **Total** | **33** |

## Tools
Python, Pandas, NumPy, Matplotlib, Streamlit, Jupyter Notebook/Google Colab, Git, and GitHub. Additional NLP or machine-learning tools are optional and will only be used if justified.

## Risks and mitigation
- **Missing/inconsistent data:** document cleaning rules and exclusions.
- **Synonyms and false matches:** use a reviewed dictionary and manually inspect a sample.
- **Salary ambiguity:** compare only values with clear currency and units.
- **Dataset bias:** state source, time period, geography, and coverage limitations.
- **Data-use restrictions:** follow dataset licenses and source terms.

## Evaluation
Completeness of the workflow, reproducibility, data quality, validity of charts and skill counts, clarity of communication, and honest reporting of limitations.

## Status
This is a plan and starter implementation. Do not report findings or model performance until the analysis has been run on a documented dataset and checked.
