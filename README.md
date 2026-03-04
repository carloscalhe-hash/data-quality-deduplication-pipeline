# Data Quality Deduplication Pipeline

Python project for detecting duplicated contact data (emails and phone numbers) in datasets and generating a cleaned output.

This project simulates a basic data quality pipeline used in data operations and analytics environments.

---

## Project Overview

Data quality is a common challenge in organizations that manage large customer databases.  
Duplicated contact information can generate operational errors, incorrect communications, and reporting issues.

This pipeline performs:

- Detection of duplicated emails
- Detection of duplicated phone numbers
- Generation of a dataset containing duplicated records

---

## Project Structure

```
data-quality-deduplication-pipeline
│
├── data
│   └── sample_dataset.csv
│
├── src
│   └── pipeline.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Example Dataset

The dataset contains sample customer records:

| id | name  | email           | phone     |
|----|------|----------------|-----------|
| 1  | Ana  | ana@email.com  | 600111111 |
| 2  | Luis | luis@email.com | 600222222 |
| 3  | Ana  | ana@email.com  | 600111111 |

The pipeline detects duplicated values in the **email** and **phone** columns.

---

## How the Pipeline Works

1. Load dataset using pandas  
2. Identify duplicated values  
3. Merge duplicated records  
4. Export the results to a new dataset  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/data-quality-deduplication-pipeline.git
cd data-quality-deduplication-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Run the script:

```bash
python src/pipeline.py
```

The script will generate a file containing duplicated records.

---

## Technologies Used

- Python  
- pandas  
- Git  
- GitHub  

---

## Purpose

This repository is part of a **data analytics portfolio** and demonstrates a simple data quality pipeline implemented in Python.
