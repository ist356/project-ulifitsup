import pandas as pd
import streamlit as st
from datetime import datetime

def main():
    if st.checkbox("Load data from cache"):
        data = pd.read_csv("../cache/crowdstrike_jobs_title.csv", header=0)
        for column in data.columns:
            data[column] = data[column].astype(str).fillna("N/A")
        if "job_deadline" in data.columns:
            data["job_deadline"] = pd.to_datetime(data["job_deadline"], errors="coerce")

        # options to select columns
        columns = ["job_title", "job_description", "job_requirements", "job_deadline"]
        # select columns to display
        selected_columns = st.multiselect("Select columns to display", columns, default=columns)
        # additional options for select columns
        add_cols = ["Filter senior jobs", "Filter engineering jobs"]
        # filter the data
        if st.checkbox("Filter"):
            stcols = st.columns(len(selected_columns))
            text_cols = ["string","string","list","string"]
            selected_columns = stcols[0].selectbox("Select columns to filter", ["job_title", "job_deadline"])
            if selected_columns:
                if selected_columns == "job_title":
                    filter_cols = stcols[0].selectbox("Select filter type", ["contains", "equals", "not contains"])
                    filter_value = stcols[1].text_input("Enter filter value", type="default")
                    if filter_cols == "contains" and not data.empty:
                        data = data[data[selected_columns].str.contains(filter_value)]
                    elif filter_cols == "equals" and not data.empty:
                        data = data[data[selected_columns] == filter_value]
                    elif filter_cols == "not contains" and not data.empty:
                        data = data[~data[selected_columns].str.contains(filter_value)]
                    df_show = data[[selected_columns, "job_deadline"]]
                elif selected_columns == "job_deadline":
                    filter_cols = stcols[0].selectbox("Select filter type", ["expired soon", "not expired", "expired"])
                    if filter_cols == "expired soon" and not data.empty:
                        data = data[(data[selected_columns] - datetime.now()).dt.days.between(0, 30)]
                    elif filter_cols == "not expired" and not data.empty:
                        data = data[(data[selected_columns] - datetime.now()).dt.days > 30]
                    elif filter_cols == "expired"  and not data.empty:
                        data = data[(data[selected_columns] - datetime.now()).dt.days < 0]
                    df_show = data[[selected_columns, "job_title"]]
                values = data[selected_columns].unique().tolist()
                st.write(f"writing~~")
                
        else:
            df_show = data[selected_columns]

        st.dataframe(df_show)
        st.dataframe(df_show.describe())
    else:
        st.error("Cache file not found, scraping data from website")

if __name__ == "__main__":
    st.write("This is a Streamlit app for scraping CrowdStrike job listings.")
    st.write("It displays the job listings in a table and allows users to filter the data.")
    st.write("The app also provides summary statistics for the data.")
    st.write("To run the app, use the following command: streamlit run cs_jobs.py")
    st.title("CrowdStrike Jobs")
    st.caption("This app scrapes CrowdStrike job listings and displays them in a table")
    main()