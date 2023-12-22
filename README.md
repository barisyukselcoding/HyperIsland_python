
Netflix Shows Pipeline
---
This Python script downloads the 'Netflix Shows' dataset from Kaggle, processes it using Pandas, and stores it in a SQLite database.

This Python script is a pipeline for downloading a dataset from Kaggle (specifically the 'shivamb/netflix-shows' dataset), processing it using Pandas, and storing it in a SQLite database.

Setting Kaggle Credentials: The Kaggle username and API key are set as environment variables for authentication.

Initializing Kaggle API: The Kaggle API is initialized for authentication using the provided credentials.

Downloading Dataset: The script specifies the dataset name ('shivamb/netflix-shows') and downloads its files to a temporary directory, unzipping them for access.

Loading Data into Pandas DataFrame: Once downloaded, the CSV file from the dataset is loaded into a Pandas DataFrame for data manipulation.

Creating SQLite Database: A SQLite database ('netflix_data.db') is created, and a connection is established.

Writing Data to Database: The data from the Pandas DataFrame is written into a table named 'Netflix_Shows' within the SQLite database. If the table exists, the data is replaced.

Closing Database Connection: Finally, the connection to the SQLite database is closed.

This pipeline automates the process of fetching data from Kaggle, transforming it using Pandas, and storing it in a local SQLite database for further analysis or usage. 

Requirements
---

Ensure you have Python 3.x installed along with the following libraries:

Kaggle API
Pandas
SQLite3
Usage
Set your Kaggle username and API key.
Run the script to execute the pipeline.
Note: Adjust file paths as needed for your environment.

Netflix Data Analysis using Jupyter Notebook
---
This Jupyter Notebook analyzes the 'Netflix Shows' dataset retrieved from a SQLite database. It performs several data handling and visualization operations using Pandas and Matplotlib.

Overview
The notebook conducts the following operations:

Fetches data from the 'Netflix_Shows' table in the 'netflix_data.db' SQLite database.

Handles missing values in the 'description' column.

Explores the dataset's attributes through visualizations:

Counts titles per genre using bar charts.

Represents the distribution of TV shows vs. movies with a pie chart.

Examines the count of titles per year using a line plot.

Compares title lengths between movies and TV shows with histograms.

Key Operations

Data Retrieval: Retrieves the dataset from the SQLite database.

Data Handling: Manages missing values in the 'description' column.

Visualizations: Presents insights through bar charts, pie charts, line plots, and histograms.

Requirements

The notebook requires:

Python
Pandas
Matplotlib
SQLite3
Usage
To replicate these analyses:

Ensure the 'netflix_data.db' database contains the 'Netflix_Shows' table.
Run each cell in the notebook sequentially to observe the results.
Note
The notebook assumes a 'Netflix_Shows' table exists in 'netflix_data.db'.
Modify the file paths or database connections as per your environment.
