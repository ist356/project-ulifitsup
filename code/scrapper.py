import pandas as pd
from playwright.sync_api import Playwright,sync_playwright
from code.desc_clean import clean_desc

def get_jobs(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    data = []
    page.goto("https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/jobs")
    page_number = 1
    while True:
        page.wait_for_selector(f"ul[aria-label='Page {page_number} of 19']", state="visible")
        print("Page number: ", page_number)
        job_list = page.locator(f"ul[aria-label='Page {page_number} of 19'] > li")
        for i in range(job_list.count()):
            # extract jobs title from jobtitle element
            job = job_list.nth(i)
            try:
                if job.locator("h3").count() > 0 and job.locator("h3").is_visible():
                    job_title = job.locator("h3").inner_text()
                    print("job title: ", job_title)
            except Exception as e:
                print("Error: ", e)
                continue
            # extract job details
            job_button = job.locator("a")
            if job_button.count() > 0:
                with page.expect_navigation():
                    job_button.click()
                page.wait_for_selector("div[data-automation-id='jobPostingDescription']", state="visible")
                page.wait_for_load_state("domcontentloaded")
                job_detail = page.query_selector("div[data-automation-id=jobPostingDescription]")
                job_details = clean_desc(job_detail.inner_text())
                page.go_back()
                page.wait_for_selector(f"ul[aria-label='Page {page_number} of 19']", state="visible")
                page.wait_for_load_state("domcontentloaded")
                data.append({"job_title": job_title, "job_description": job_details["description"], "job_requirements": job_details["requirements"], "job_deadline": job_details["deadline"]})
        next_button = page.locator("button[aria-label='next']")
        if next_button.count() > 0:
            next_button.click()
            print("next page loaded")
            page_number += 1
        else:
            print("No more pages")
            break
    df = pd.DataFrame(data)
    df.to_csv("../cache/crowdstrike_jobs_title.csv", index=False)
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        get_jobs(p)