import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import sqlite3
from config import KAGGLE_USERNAME, KAGGLE_KEY

# I'm setting my Kaggle username and API key as environment variables.
os.environ["KAGGLE_USERNAME"] = "your_kaggle_username"
os.environ["KAGGLE_KEY"] = "your_kaggle_api_key"

# I'm initializing the Kaggle API for authentication.
api = KaggleApi()
api.authenticate()

# I'm specifying the dataset name I want to download.
dataset_name = 'shivamb/netflix-shows'

# I'm downloading the dataset files to a temporary directory and unzipping them.
api.dataset_download_files(dataset_name, unzip=True)

# I'm loading the CSV file into a Pandas DataFrame from the downloaded file.
file_path = 'netflix-shows.zip'  # I adjust this based on the downloaded file name
data = pd.read_csv(file_path)

# I'm creating a SQLite database and establishing a connection.
conn = sqlite3.connect('netflix_data.db')

# I'm writing the data from the DataFrame into a SQLite database table named 'Netflix_Shows'.
data.to_sql('Netflix_Shows', conn, if_exists='replace', index=False)

# I'm closing the connection to the database.
conn.close()


