import pandas as pd
from fpdf import FPDF
import logging

# Configure logging
logging.basicConfig(filename="data_validation.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Load data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        return None

# Data validation checks
def validate_data(data):
    issues = {}
    
    # Check for missing values
    missing_values = data.isnull().sum()
    issues['Missing Values'] = missing_values[missing_values > 0]
    
    # Check for data types
    incorrect_types = {}
    for column in data.columns:
        if data[column].dtype == 'object':
            if not all(isinstance(val, str) for val in data[column].dropna()):
                incorrect_types[column] = "Expected string, found other types"
        elif data[column].dtype in ['int64', 'float64']:
            if not all(isinstance(val, (int, float)) for val in data[column].dropna()):
                incorrect_types[column] = "Expected number, found other types"
    issues['Incorrect Data Types'] = incorrect_types
    
    # Check for duplicates
    duplicate_count = data.duplicated().sum()
    issues['Duplicates'] = duplicate_count
    
    return issues

# Generate summary statistics
def generate_statistics(data):
    summary = data.describe(include='all').to_dict()
    return summary

# Generate report in PDF
def generate_pdf_report(file_name, issues, statistics):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Data Validation Report", ln=True, align="C")
    
    pdf.ln(10)
    pdf.cell(200, 10, txt="Issues Found:", ln=True, align="L")
    
    # Log issues in PDF
    for issue_type, details in issues.items():
        pdf.cell(200, 10, txt=f"{issue_type}:", ln=True)
        if isinstance(details, pd.Series):
            for col, count in details.items():
                pdf.cell(200, 10, txt=f"  - {col}: {count} issues", ln=True)
        elif isinstance(details, dict):
            for col, message in details.items():
                pdf.cell(200, 10, txt=f"  - {col}: {message}", ln=True)
        else:
            pdf.cell(200, 10, txt=f"  - {details} duplicate rows found", ln=True)

    # Summary statistics in PDF
    pdf.ln(10)
    pdf.cell(200, 10, txt="Summary Statistics:", ln=True)
    for stat, fields in statistics.items():
        pdf.cell(200, 10, txt=f"{stat}:", ln=True)
        for field, value in fields.items():
            pdf.cell(200, 10, txt=f"  - {field}: {value}", ln=True)

    pdf.output(file_name)
    logging.info(f"Report generated as {file_name}")

# Main function to run the data validation and report generation
def main():
    file_path = "F:\\Coding\\Project\\archive\\data.csv"  # Update with your actual CSV file path
    data = load_data(file_path)
    
    if data is not None:
        issues = validate_data(data)
        statistics = generate_statistics(data)
        generate_pdf_report("Data_Validation_Report.pdf", issues, statistics)
        print("Data validation completed. Check the PDF report and log file.")
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
