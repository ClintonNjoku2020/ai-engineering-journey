
# AI Engineering Journey

## About This Repository

This repository documents my practical learning journey through the Refonte Learning AI Engineering Training Programme.

It contains Python programming exercises, data exploration projects, reusable functions, technical documentation, and assignments demonstrating my progress towards professional AI Engineering.

## Learning Objectives

My objectives are to:

- Strengthen my Python programming and software engineering skills.
- Develop practical experience in data analysis and machine learning.
- Build reliable, reusable, and maintainable Python applications.
- Explore prompt engineering, large language models (LLMs), and AI applications.
- Apply professional Git and GitHub workflows, testing, and documentation practices.
- Build a portfolio of reproducible AI Engineering projects.

## Repository Structure

```text
ai-engineering/
├── README.md
├── SETUP.md
├── .gitignore
├── requirements.txt
├── data/
│   └── students.csv
├── practice/
│   ├── week1_exercises.py
│   ├── week2_structures.py
│   ├── week2_functions.py
│   ├── week2_numpy.py
│   └── other practice files
└── projects/
    └── 01-data-exploration/
        ├── README.md
        ├── clean.py
        ├── penguins_analysis.py
        ├── date_parsing_experiment.py
        ├── merge_penguins.py
        ├── create_charts.py
        ├── requirements.txt
        ├── data/
        └── output/
```

## Featured Project

### 01 — Palmer Penguins: Data Exploration and Cleaning

[View Project](projects/01-data-exploration/README.md)

This project explores the Palmer Penguins dataset using Python, Pandas, NumPy, and Matplotlib.

The project demonstrates:

- Data inspection and exploratory data analysis.
- Handling missing values and duplicate records.
- Reusable data cleaning functions.
- Date parsing and data quality experiments.
- Merging datasets using reference tables.
- Data aggregation and statistical analysis.
- Data visualisation and interpretation.

### Key Findings

- Gentoo penguins have the highest average body mass, approximately 5,076 g.
- Gentoo penguins have the longest average flipper length, approximately 217 mm.
- All 61 penguins weighing more than 5,000 g in the analysed dataset belong to the Gentoo species.

Further analysis, charts, methodology, and limitations are documented in the project README.

## Current Progress

### Week 1 — Python and Environment Setup

- Configured a Python development environment using WSL Ubuntu.
- Created and activated a Python virtual environment.
- Practised Python fundamentals.
- Established the GitHub repository.
- Documented environment setup procedures.

### Week 2 — Python, Data Analysis, and Reusable Code

- Practised lists, dictionaries, functions, and NumPy operations.
- Explored and cleaned the Palmer Penguins dataset.
- Completed exploratory analysis and statistical summaries.
- Developed reusable data cleaning functions and tests.
- Investigated date parsing errors.
- Merged penguin records with species reference data.
- Created charts illustrating dataset characteristics and relationships.

### Professional Git Workflow

Session 6 focuses on:

- Repository organisation and dependency management.
- Git branching and pull requests.
- Merge conflict resolution.
- Repository security and documentation.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ClintonNjoku2020/ai-engineering-journey.git
cd ai-engineering-journey
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Explore the Projects

Open the [Palmer Penguins project README](projects/01-data-exploration/README.md) for project-specific setup instructions, analysis results, and charts.

For additional development environment guidance, see [SETUP.md](SETUP.md).

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git and GitHub
- WSL Ubuntu
- Visual Studio Code

## Future Development

Upcoming work will focus on:

- Building reusable data processing pipelines.
- Working with APIs and JSON data.
- Feature engineering for machine learning.
- Training and evaluating machine learning models.
- Developing AI applications using LLMs and prompt engineering.

## Long-Term Objective

To develop a professional portfolio of AI Engineering projects demonstrating practical problem-solving, reproducible workflows, maintainable code, and reliable AI application development.
