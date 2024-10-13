from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
from  airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['bhavanadaripalli@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('orders_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

with dag:
    run_script_task = BashOperator(
        task_id='extract_data_gcs',
        bash_command='python /home/airflow/gcs/dags/scripts/main.py',
    )

gcs_to_bq_load = GoogleCloudStorageToBigQueryOperator (
                task_id ='gcs_to_bq_load',
                bucket ='bkt_data_10000',
                source_objects =['ECommerce_generated_data.csv'],
                destination_project_dataset_table ='projectp2-437205.customers.orders_table',
                schema_fields =[
                            {'name':'order_id','type':'STRING','mode':'NULLABLE'},
                            {'name':'customer_id','type':'STRING','mode':'NULLABLE'},
                            {'name':'customer_name','type':'STRING','mode':'NULLABLE'},
                            {'name':'product_id','type':'STRING','mode':'NULLABLE'},
                            {'name':'product_name','type':'STRING','mode':'NULLABLE'},
                            {'name':'product_category','type':'STRING','mode':'NULLABLE'},
                            {'name':'payment_type','type':'STRING','mode':'NULLABLE'},
                            {'name':'qty','type':'INTEGER','mode':'NULLABLE'},
                            {'name':'price','type':'FLOAT','mode':'NULLABLE'},
                            {'name':'datetime','type':'TIMESTAMP','mode':'NULLABLE'},
                            {'name':'country','type':'STRING','mode':'NULLABLE'},
                            {'name':'city','type':'STRING','mode':'NULLABLE'},
                            {'name':'ecommerce_website_name','type':'STRING','mode':'NULLABLE'},
                            {'name':'payment_txn_id','type':'STRING','mode':'NULLABLE'},
                            {'name':'payment_txn_success','type':'BOOLEAN','mode':'NULLABLE'},
                            {'name':'failure_reason','type':'STRING','mode':'NULLABLE'}
                            
                ],
                skip_leading_rows=1,
                create_disposition='CREATE_IF_NEEDED',
                write_disposition='WRITE_TRUNCATE',
                dag=dag)

    

run_script_task >> gcs_to_bq_load


