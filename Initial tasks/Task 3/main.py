import pandas as pd
df = pd.read_csv("C:\Code\Python\Intership\Initial tasks\Task 3\healthcare_messy_data.csv")
print("rows, columns before cleaning.")
print(df.shape)
# Trimming all the whitespaces
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

# validating the 'Email' column
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df = df[df['Email'].str.contains(pattern, case=False, regex=True, na=False)]

#	converting dates to ISO format
df['Visit Date'] = pd.to_datetime(df['Visit Date'], errors='coerce')
df['Visit Date'] = df['Visit Date'].dt.strftime('%Y-%m-%d')

# Dropping rows with 'Nan' value in 'Condition' column
df= df.dropna(subset=['Condition'])
print("Dropped the rows with 'Nan' value in 'Condition' column.")

# Dropping rows with none value in 'Medication' column
df = df[~df['Medication'].str.contains('NONE')]
print("Dropped rows with none value in 'Medication' column")

df.to_csv("Cleaned.csv")
print("Saved the cleaned file to 'Cleaned.csv")
print("rows, columns after cleaning.")
print(df.shape)
