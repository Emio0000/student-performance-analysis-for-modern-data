import pandas as pd   # Import pandas library for data analysis

print("🚀 Script started...")

# Load dataset (CSV) into a DataFrame
# Make sure the file StudentsPerformance.csv is in the same folder as this script
df = pd.read_csv("StudentsPerformance.csv")

# Preview the first 5 rows of the raw dataset
print("First 5 rows of raw data:")
print(df.head())

# 1. Remove duplicate rows (if any student data is repeated, it will be dropped)
df = df.drop_duplicates()

# 2. Handle missing values
# For numeric columns (e.g., scores) → replace missing values with the median
df = df.fillna(df.median(numeric_only=True))
# For text columns (e.g., gender, lunch) → replace missing values with the most frequent value (mode)
df = df.fillna(df.mode().iloc[0])

# 3. Standardize column names
# Convert column names to lowercase, remove extra spaces, and replace spaces with underscores
# Example: "Math Score" → "math_score"
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 4. Add new column: Average score (if all three score columns are present)
if {"math_score", "reading_score", "writing_score"}.issubset(df.columns):
    # Calculate average score across math, reading, and writing
    df["average_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1)
    # Create a Pass/Fail result column (Pass if average_score >= 50)
    df["result"] = df["average_score"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# 5. Save the cleaned dataset to a new CSV file
# This file will be used in Power BI for creating dashboards
df.to_csv("cleaned_students.csv", index=False)

print("\n✅ Cleaned dataset saved as cleaned_students.csv")
