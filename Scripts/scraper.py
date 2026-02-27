from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

roles = [
    "software developer",
    "data analyst",
    "data scientist",
    "full stack developer",
    "devops engineer"
]

jobs_data = []

for role in roles:

    print(f"Scraping role: {role}")

    for start in range(0, 60, 20):   # 3 pages (0,20,40)

        url = f"https://www.naukri.com/{role.replace(' ', '-')}-jobs?k={role.replace(' ', '%20')}&start={start}"
        driver.get(url)

        time.sleep(5)

        job_cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")

        print(f"Jobs found: {len(job_cards)}")

        for job in job_cards:

            try:
                title = job.find_element(By.CLASS_NAME, "title").text
            except:
                title = ""

            try:
                company = job.find_element(By.CLASS_NAME, "comp-name").text
            except:
                company = ""

            try:
                location = job.find_element(By.CLASS_NAME, "locWdth").text
            except:
                location = ""

            try:
                experience = job.find_element(By.CLASS_NAME, "expwdth").text
            except:
                experience = ""

            try:
                salary = job.find_element(By.CLASS_NAME, "sal-wrap").text
            except:
                salary = ""

            try:
                skills = job.find_element(By.CLASS_NAME, "tags-gt").text
            except:
                skills = ""

            jobs_data.append({
                "Role_Search": role,
                "Title": title,
                "Company": company,
                "Location": location,
                "Experience": experience,
                "Salary": salary,
                "Skills": skills
            })

df = pd.DataFrame(jobs_data)

print("Total rows scraped:", len(df))   # NEW LINE

df.to_csv("jobs_data.csv", index=False)

print("File saved successfully!")       # NEW LINE

driver.quit()