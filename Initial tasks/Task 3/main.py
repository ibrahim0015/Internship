import pandas as pd

def clean():
    try:
        df = pd.read_csv(r"C:\Code\Python\Intership\Initial tasks\Task 3\healthcare_messy_data.csv")
        print("rows, columns before cleaning.")
        print(df.shape)
    except FileNotFoundError:
        print("File not found")
        return
        
    # Trimming all the whitespaces
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # validating the 'Email' column
    if "Email" in df.columns:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        df = df[df['Email'].str.contains(pattern, case=False, regex=True, na=False)]
    else:
        print("'Email' column not found.")
    #	converting dates to ISO format
    if "Visit Date" in df.columns:
        df['Visit Date'] = pd.to_datetime(df['Visit Date'], errors='coerce')
        df['Visit Date'] = df['Visit Date'].dt.strftime('%Y-%m-%d')
    
    # Dropping rows with 'Nan' value in 'Condition' column
    if "Condition" in df.columns:
        df= df.dropna(subset=['Condition'])
        print("Dropped the rows with 'Nan' value in 'Condition' column.")

    # Dropping rows with none value in 'Medication' column
    if 'Medication' in df.columns:
        df = df[~df['Medication'].str.contains('NONE', na=False)]
        print("Dropped rows with none value in 'Medication' column")

    df.to_csv("Cleaned.csv")
    
    print("Saved the cleaned file to 'Cleaned.csv")
    print("rows, columns after cleaning.")
    print(df.shape)

clean()