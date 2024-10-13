from google.cloud import storage

def upload_csv_to_gcs(bucket_name, source_file_name, destination_blob_name):
    try:
        # Initialize the storage client using the default credentials
        storage_client = storage.Client()

        # Get the bucket and upload the file
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {bucket_name}/{destination_blob_name}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function without the service account key
upload_csv_to_gcs("bkt_data_10000", "ECommerce_generated_data.csv", "ECommerce_generated_data.csv")
