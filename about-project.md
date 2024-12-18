# About My Project

Student Name:  Xinglai Pang
Student Email:  xpang03@syr.edu

### What it does
This project is a web scraping that reads all the open jobs on Crowdstrike, which has hundreds of open opportunity but only few are available for a graduating undergraduate students, so I intented to create a web scraping scripts and run and filter out based on the job preferences and also filter out those senior jobs that are not available for undergrads.

### How you run my project
Since I am running the project with streamlit, simply run the streamlit will do.
Also, Stremlit is having trouble running simultaneously with playwright, if possible please run seperately, or simply run streamlit with cached csv.
To run playwright scrapper, it is possible just run the scrapper.py file, it will automatically go to Crowdstrike's website and scrap all the possible and available jobs.

### Other things you need to know
The project is a bit out of scope when I am approchaing to finish, the first thing is that playwright has a hardtime running with streamlit, I couldn't run playwright with streamlit. Second, Crowdstrike has a very unstructural templates for all of their jobs open, I guess it might be a result of running in multiple sites, and they caused a hard time, especially in data cleansing section. In streamlit, the most desirable way is to run with cached csv file, and to use the filter, a good test is to filter out the senior jobs, which CrowdStrike marked "Sr." for senior jobs, simply choose job_title for "select columns to filter" "Sr." for "Enter filter value", and "not contains" for "select filter type" will give all jobs that is not senior. At the same time, we could use it to find jobs related to IT or engineering.