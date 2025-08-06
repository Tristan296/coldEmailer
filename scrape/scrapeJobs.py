import csv
from jobspy import scrape_jobs


jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "google"], # "glassdoor", "bayt", "naukri", "bdjobs"
    search_term="software engineer",
    google_search_term="software engineer jobs near Sydney Australia, since last 3 days",
    location="Sydney Australia",
    results_wanted=50,
    hours_old=72,
    country_indeed='Australia',
    country_zip_recruiter='au',
    country_linkedin='au',
    country_google='au',
    
    # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
path = "results/jobs.csv"
print(f"Saving jobs to {path}")
jobs.to_csv(path, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
