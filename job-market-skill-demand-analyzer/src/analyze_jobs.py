"""Starter analysis for the Job Market and Skill Demand Analyzer."""
from __future__ import annotations

import argparse
import os
import re
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

SKILL_KEYWORDS = {
    "Python": ["python"],
    "SQL": ["sql", "structured query language"],
    "Excel": ["excel", "spreadsheets"],
    "Power BI": ["power bi"],
    "Tableau": ["tableau"],
    "Machine Learning": ["machine learning", "scikit-learn", "sklearn"],
    "Data Analysis": ["data analysis", "data analytics", "data analyst"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Statistics": ["statistics", "statistical analysis"],
    "NLP": ["natural language processing", "nlp"],
    "Cloud": ["aws", "azure", "google cloud"],
    "Git": ["git", "github"],
    "Communication": ["communication skills", "communication"],
}


def extract_skills(text: str) -> list[str]:
    """Return skill categories mentioned in a job description using simple keyword matching."""
    normalized = str(text).lower()
    found = []
    for skill, terms in SKILL_KEYWORDS.items():
        if any(re.search(r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)", normalized) for term in terms):
            found.append(skill)
    return found


def analyze(input_csv: str, output_dir: str) -> pd.DataFrame:
    """Load a CSV, summarize skill mentions, and save a chart."""
    df = pd.read_csv(input_csv)
    if "description" not in df.columns:
        raise ValueError("Input CSV must contain a 'description' column.")
    df = df.drop_duplicates().copy()
    df["description"] = df["description"].fillna("").astype(str)
    counts = Counter(skill for description in df["description"] for skill in extract_skills(description))
    summary = pd.DataFrame(counts.items(), columns=["skill", "job_postings_with_skill"])
    if not summary.empty:
        summary = summary.sort_values("job_postings_with_skill", ascending=False)
    os.makedirs(output_dir, exist_ok=True)
    summary.to_csv(os.path.join(output_dir, "skill_frequency.csv"), index=False)
    if not summary.empty:
        plt.figure(figsize=(10, 6))
        plot_df = summary.head(12).sort_values("job_postings_with_skill")
        plt.barh(plot_df["skill"], plot_df["job_postings_with_skill"])
        plt.xlabel("Number of job descriptions mentioning skill")
        plt.title("Frequently Mentioned Skills in Selected Job Postings")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "skill_frequency.png"), dpi=160)
        plt.close()
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/job_postings.csv", help="Path to job-postings CSV")
    parser.add_argument("--output", default="visuals", help="Directory for output files")
    args = parser.parse_args()
    result = analyze(args.input, args.output)
    print(result.to_string(index=False) if not result.empty else "No skill mentions found.")


if __name__ == "__main__":
    main()
