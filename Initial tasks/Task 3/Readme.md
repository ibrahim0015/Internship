# Healthcare Data Cleaning Script (Pandas)

This script cleans a messy healthcare dataset using **Python and Pandas** by applying common real-world data cleaning steps such as trimming whitespace, validating emails, fixing date formats, and removing invalid records.

## What This Script Does

- Reads a CSV file containing messy healthcare data
- Removes leading and trailing whitespace from all text columns
- Validates and keeps only correctly formatted email addresses
- Converts visit dates to ISO format (`YYYY-MM-DD`)
- Drops rows with missing values in critical columns
- Removes records with invalid medication values
- Saves the cleaned dataset to a new CSV file

## Cleaning Steps Performed

1. **Whitespace Removal**  
   Trims extra spaces from all string (object) columns.

2. **Email Validation**  
   Keeps only rows with valid email addresses using regex.

3. **Date Standardization**  
   Converts the `Visit Date` column to ISO format. Invalid dates are removed.

4. **Missing Data Handling**  
   - Drops rows with `NaN` values in the `Condition` column.
   - Removes rows where `Medication` contains `NONE`.

5. **Export Clean Data**  
   Saves the cleaned dataset as `Cleaned.csv`.

## Requirements

- Python 3.x
- pandas

Install dependency:
pip install pandas

css
Copy code

## How to Run

1. Place the script and the CSV file in the correct path
2. Update the input file path if needed:
healthcare_messy_data.csv

markdown
Copy code
3. Run the script:
python script_name.py

csharp
Copy code

## Output

- A cleaned dataset saved as:
Cleaned.csv

markdown
Copy code
- Console logs showing:
- Rows and columns before cleaning
- Rows and columns after cleaning
- Summary of cleaning actions

## Notes

- Invalid or malformed rows are removed automatically
- Designed as a beginner-friendly data cleaning task
