**Automated Data Validation and Report Generation**
This Python script performs automated data validation checks on a CSV file, including identifying missing values, incorrect data types, and duplicate rows. It then generates a PDF report summarizing the findings and key statistics.

**Features**
Data Loading: Reads a CSV file for analysis.
**Data Validation Checks:**
Identifies columns with missing values.
Verifies data types for each column.
Checks for duplicate rows.
**Summary Statistics:** Generates key statistical summaries.
PDF Report Generation: Compiles issues and summary statistics into a PDF report.
**Dataset**
This project utilizes a dataset sourced from **Kaggle**. Make sure to download the dataset and place it in the designated directory before running the script.
**Requirements**
Python 3.x: Ensure Python is installed on your system.
Required Libraries:
pandas: For data manipulation and validation.
fpdf: To generate the PDF report.
logging: To log events and errors.
**Example Output**
The PDF report will contain:

**Issues Found:**

List of columns with missing values and their counts.
Columns with incorrect data types.
Count of duplicate rows.****
**Summary Statistics:**

Descriptive statistics for numerical and categorical columns.

**Example console output when running the script:**
Data validation completed. Check the PDF report and log file.
