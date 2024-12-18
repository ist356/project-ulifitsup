import os
from unittest.mock import patch
from code.scrapper import get_jobs
from playwright.sync_api import sync_playwright
import pandas as pd

FILE = "cache\crowdstrike_jobs_title.csv"

def test_should_pass():
    print("Test should always pass!")
    assert True

def test_csv_file_exists():
    print("Test if csv file exists")
    assert os.path.exists(FILE)

def test_csv_file():
    df = pd.read_csv(FILE)
    print("csv expect to have more than 300 rows and 4 columns")
    assert df.shape[0] > 300 and df.shape[1] >= 4