import requests
import pandas as pd
from html import unescape
from bs4 import BeautifulSoup
from ftfy import fix_text


url = "https://remoteok.com/remote-jobs.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}


# 🔥 دالة تنظيف عامة
def clean_text(text):

    if not text:
        return ""

    # HTML entities مثل &amp;
    text = unescape(text)

    # إصلاح encoding الغريب
    text = fix_text(text)

    # إزالة HTML
    text = BeautifulSoup(
        text,
        "html.parser"
    ).get_text(" ", strip=True)

    # إزالة المسافات الزائدة
    text = " ".join(text.split())

    return text


response = requests.get(url, headers=headers)

jobs = response.json()

data = []

for job in jobs:

    if isinstance(job, dict) and "position" in job:

        title = clean_text(job.get("position"))
        company = clean_text(job.get("company"))

        tags = ", ".join(job.get("tags", []))
        tags = clean_text(tags)

        salary = clean_text(str(job.get("salary", "Not specified")))

        location = clean_text(job.get("location", "Remote"))

        date = clean_text(job.get("date", ""))

        description = clean_text(
            job.get("description", "")
        )

        data.append({
            "title": title,
            "company": company,
            "tags": tags,
            "salary": salary,
            "location": location,
            "date": date,
            "description": description
        })


df = pd.DataFrame(data)

df.to_csv(
    "jobs.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Clean Stage 3 completed 🚀")