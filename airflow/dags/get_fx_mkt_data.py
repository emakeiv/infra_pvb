from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from app.sal.etl.main import main

DAG_DEFAULT_ARGS={
    'owner': 'airflow',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
      default_args = DAG_DEFAULT_ARGS,
      dag_id='24_01_02_fx_mkt_data',
      start_date=datetime(2024, 1, 1),
      schedule_interval='@daily'
) as dag:
      task1 = PythonOperator(
            task_id='first_attempt',
            python_callable=main
      )

      task1