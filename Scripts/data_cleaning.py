import pandas as pd
import re

# Load data
df = pd.read_csv("jobs_data.csv")

print("Original Rows:", len(df))

# -----------------------------
# Experience Cleaning
# -----------------------------

def extract_experience(exp):
    try:
        numbers = re.findall(r'\d+', str(exp))
        if len(numbers) >= 2:
            return int(numbers[0]), int(numbers[1])
        elif len(numbers) == 1:
            return int(numbers[0]), int(numbers[0])
    except:
        pass
    return None, None


df[['Min_Exp', 'Max_Exp']] = df['Experience'].apply(
    lambda x: pd.Series(extract_experience(x))
)

df['Avg_Exp'] = (df['Min_Exp'] + df['Max_Exp']) / 2

# -----------------------------
# Salary Cleaning
# -----------------------------

def extract_salary(sal):
    try:
        numbers = re.findall(r'\d+', str(sal))
        if len(numbers) >= 2:
            return int(numbers[0]), int(numbers[1])
    except:
        pass
    return None, None


df[['Min_Salary', 'Max_Salary']] = df['Salary'].apply(
    lambda x: pd.Series(extract_salary(x))
)

# -----------------------------
# Location Cleaning (City)
# -----------------------------

df['City'] = df['Location'].astype(str).apply(lambda x: x.split(",")[0])

# -----------------------------
# Role Category Creation
# -----------------------------

def categorize_role(title):

    title = str(title).lower()

    if "data" in title:
        return "Data"
    elif "devops" in title or "cloud" in title:
        return "DevOps/Cloud"
    elif "engineer" in title or "developer" in title:
        return "Developer"
    elif "analyst" in title:
        return "Analyst"
    else:
        return "Other"


df['Role_Category'] = df['Title'].apply(categorize_role)

# -----------------------------
# Skills Cleaning
# -----------------------------

df['Skills_List'] = df['Skills'].astype(str).apply(lambda x: x.lower())

# -----------------------------
# Save Clean Dataset
# -----------------------------

df.to_csv("jobs_cleaned.csv", index=False)

print("Cleaning completed!")
print("New file saved: jobs_cleaned.csv")
print("Final Columns:", df.columns)