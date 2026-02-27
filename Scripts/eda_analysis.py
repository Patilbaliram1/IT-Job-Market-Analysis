import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("jobs_cleaned.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nSample Data:")
print(df.head())


# -----------------------------
# 1. Jobs by Role Category
# -----------------------------
role_counts = df['Role_Category'].value_counts()
print("\nJobs by Role Category:")
print(role_counts)

role_counts.plot(kind='bar', title="Jobs by Role Category")
plt.show()


# -----------------------------
# 2. Top Cities Hiring
# -----------------------------
city_counts = df['City'].value_counts().head(10)
print("\nTop Cities:")
print(city_counts)

city_counts.plot(kind='bar', title="Top Hiring Cities")
plt.show()


# -----------------------------
# 3. Experience Distribution
# -----------------------------
df['Avg_Exp'].dropna().plot(kind='hist', bins=20, title="Experience Distribution")
plt.show()


# -----------------------------
# 4. Salary Distribution
# -----------------------------
df['Min_Salary'].dropna().plot(kind='hist', bins=20, title="Salary Distribution")
plt.show()


# -----------------------------
# 5. Top Companies Hiring
# -----------------------------
company_counts = df['Company'].value_counts().head(10)
print("\nTop Companies:")
print(company_counts)

company_counts.plot(kind='bar', title="Top Hiring Companies")
plt.show()