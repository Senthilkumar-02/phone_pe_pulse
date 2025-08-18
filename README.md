# PhonePe Pulse Data Analysis Dashboard

An end-to-end data analytics and visualization project leveraging the PhonePe Pulse dataset, MySQL, and Streamlit. The system extracts, stores, processes, and analyzes transaction, user, and insurance data to generate interactive dashboards and insightful visualizations, enabling a deeper understanding of India’s digital payment trends.

## Overview

The PhonePe Pulse Data Analysis Dashboard converts raw data from PhonePe’s public repository into actionable insights by integrating multiple technologies: Python for data extraction and processing, MySQL for structured data storage, and Streamlit for building an interactive and user-friendly dashboard.

Key features include:

Transaction analysis across states, districts, and time periods (quarterly trends)

Device usage and user engagement monitoring

Visualization of insurance adoption patterns

GeoJSON-powered India map for regional insights

Scenario-based analysis to support strategic decision-making

## Use Cases Handled

Which states are growing in transaction volumes?
				
				* Top 10 device brands are dominant?
				
				* Top 10 State-level insurance insights
				
				* States With Highest Transaction Amount?
				
				* Top 10 States With Phonepe users?
				
				* 10 States High and low insurance adoption—indicating untapped potential for expanding insurance services?
				
				* Which states, districts contribute the highest to overall transaction volume and value on PhonePe?
				
				* Which states, districts, and pin codes recorded the highest number of user registrations on year and quarter?
				
				* What are the top 10 regions (by district or pin code) contributing to overall insurance transaction volume?

## Dataset Overview

Data for this project is sourced directly from the official PhonePe Pulse GitHub repository, comprising three primary components:

* Aggregated Data: Comprehensive statistics on transactions, user activity, and insurance, summarized across various categories.

* Map Data: State and district-level performance metrics for detailed geographic analysis.

* Top Data: Rankings of the most popular categories, brands, and regions based on key indicators.

This structured dataset enables in-depth exploration of digital payments trends at national, regional, and local levels.

## Tech Stack

	* Programming Language: Python
	
	* Database: MySQL
	
	* Core Libraries: Pandas, Plotly Express, Streamlit, Requests
	
	* Geospatial Mapping: GeoJSON (for Indian state and district boundaries)

This combination enables robust data extraction, efficient storage, interactive analysis, and engaging visualizations tailored to Indian digital payment trends.

## Project Structure

PHONE_PE/                      # Root project folder
│
├── pulse/                     
│   └── data/                  # Data directory 
│
├── .gitignore                 # Git ignore file 
├── LICENSE                    # License file for the project
├── Phone_pay.py               # Main script 
├── Phonepe_data_insert.py     # Script to insert/load PhonePe data into database
├── preset_phonepe_data.py     # Script to Table creation into database
└── README.md     

## Contribution

	## Exploratory Data Analysis & Visualization

		* Main script (Phone_pay.py) likely builds interactive visualizations (possibly using Streamlit, Plotly, or Matplotlib).

		* Helps analyze transactions, users, and growth trends across states, districts, and brands.







## LICENSE

[Community Data License Agreement – Permissive – Version 2.0](https://github.com/PhonePe/pulse/blob/master/LICENSE)






