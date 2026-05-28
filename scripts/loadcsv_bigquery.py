from google.cloud import bigquery
import os

# Set up your Google Cloud credentials and project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your-service-account-file.json"

# Initialize the BigQuery client
client = bigquery.Client()

# Define your dataset and table
dataset_id = 'your_project.your_dataset'
table_id = f'{dataset_id}.your_table'

# Path to the CSV file to be loaded
csv_file_path = '/path_to_output_file.csv'

# Configure the job
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,  # Skip header row
    autodetect=True       # Automatically infer schema from the data
)

# Load the CSV into BigQuery
with open(csv_file_path, "rb") as source_file:
    load_job = client.load_table_from_file(source_file, table_id, job_config=job_config)

# Wait for the job to complete
load_job.result()

# Check if the job has loaded the data correctly
table = client.get_table(table_id)
print(f"Loaded {table.num_rows} rows into {table_id}")
