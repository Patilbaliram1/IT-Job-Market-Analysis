import pandas as pd
from collections import Counter

# Load cleaned data
df = pd.read_csv("jobs_cleaned.csv")

# Combine all skills text
all_skills = df['Skills_List'].dropna().str.cat(sep=" ")

# Important tech skills list
skills_keywords = [
    "python", "java", "sql", "aws", "azure", "gcp",
    "excel", "power bi", "tableau", "machine learning",
    "deep learning", "react", "node", "angular",
    "docker", "kubernetes", "spark", "hadoop",
    "linux", "c++", "javascript"
]

skill_counts = {}

for skill in skills_keywords:
    skill_counts[skill] = all_skills.count(skill)

# Convert to dataframe
skills_df = pd.DataFrame(
    skill_counts.items(),
    columns=["Skill", "Frequency"]
).sort_values(by="Frequency", ascending=False)

print(skills_df)

# Save results
skills_df.to_csv("skills_demand.csv", index=False)

print("Skills analysis completed!")