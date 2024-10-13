import os
import subprocess
from google.cloud import storage

# Define paths for each script (update these if paths change)
SCRIPT_DIR = '/home/airflow/gcs/dags/scripts/'
REQUIREMENTS_FILE = os.path.join(SCRIPT_DIR, 'requirements.txt')
GENERATOR_SCRIPT = os.path.join(SCRIPT_DIR, 'Generator.py')
EDA_SCRIPT = os.path.join(SCRIPT_DIR, 'EDA.py')
CLEANING_SCRIPT = os.path.join(SCRIPT_DIR, 'Cleaning.py')
UPLOAD_TO_GCS_SCRIPT = os.path.join(SCRIPT_DIR, 'Upload_to_gcs.py')

# Step 1: Install the required packages from requirements.txt
def install_requirements():
    if os.path.exists(REQUIREMENTS_FILE):
        print("Installing required packages...")
        try:
            subprocess.check_call(["pip", "install", "-r", REQUIREMENTS_FILE])
            print("Packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing packages: {e}")
            raise
    else:
        print(f"Requirements file not found: {REQUIREMENTS_FILE}")

# Step 2: Run Generator.py
def run_generator():
    if os.path.exists(GENERATOR_SCRIPT):
        try:
            print(f"Running {GENERATOR_SCRIPT}...")
            subprocess.run(["python", GENERATOR_SCRIPT], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {GENERATOR_SCRIPT}: {e}")
            raise
    else:
        print(f"Generator script not found: {GENERATOR_SCRIPT}")

# Step 3: Run EDA.py
def run_eda():
    if os.path.exists(EDA_SCRIPT):
        try:
            print(f"Running {EDA_SCRIPT}...")
            subprocess.run(["python", EDA_SCRIPT], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {EDA_SCRIPT}: {e}")
            raise
    else:
        print(f"EDA script not found: {EDA_SCRIPT}")

# Step 4: Run Cleaning.py
def run_cleaning():
    if os.path.exists(CLEANING_SCRIPT):
        try:
            print(f"Running {CLEANING_SCRIPT}...")
            subprocess.run(["python", CLEANING_SCRIPT], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {CLEANING_SCRIPT}: {e}")
            raise
    else:
        print(f"Cleaning script not found: {CLEANING_SCRIPT}")

# Step 5: Upload CSV to Google Cloud Storage
def run_upload_to_gcs():
    if os.path.exists(UPLOAD_TO_GCS_SCRIPT):
        try:
            print(f"Running {UPLOAD_TO_GCS_SCRIPT}...")
            subprocess.run(["python", UPLOAD_TO_GCS_SCRIPT], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {UPLOAD_TO_GCS_SCRIPT}: {e}")
            raise
    else:
        print(f"Upload to GCS script not found: {UPLOAD_TO_GCS_SCRIPT}")

# Main execution flow
if __name__ == "__main__": 
    try:
        # Install required packages (if not handled by Composer environment)
        install_requirements()

        # Execute scripts in sequence
        run_generator()
        run_eda()
        run_cleaning()
        run_upload_to_gcs()

    except Exception as e:
        print(f"An error occurred during execution: {e}")
