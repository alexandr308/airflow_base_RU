from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.ssh_operator import SSHOperator

import datetime


default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime.datetime(2021, 1, 1, 0, 0),
	'retries': 0,
	'retry_delay': datetime.timedelta(minutes=5)
}

name = 'spark_etl'

dag = DAG(
	name,
	default_args=default_args,
	tags=['etl', 'spark_etl'],
	schedule_interval='00 5 10 * *',
	max_active_runs=1,
	catchup=False
)

dummy_operator = DummyOperator(task_id='dummy_task', dag=dag)

cmd = """
	cd /home/your_code_path/
	export PYSPARK_DRIVER_PYTHON=/home/envs/your_env/bin/python && \
	export PYSPARK_PYTHON=./your_env/bin/python && \
	spark-submit \
	--master yarn (or other) \
	--deploy-mode client \
	--num_executors 20 \
	--executors-cores 5 \
	--driver-memory 5G \
	--executor-memory 10G \
	--conf spark.executor.memoryOverhead=4G \
	--conf spark.driver.memoryOverhead=4G \
	--archives /home/envs/your_env/env.tar.gz \
	--jars '/opt/packages/terajdbc4.jar,/opt/packages/tdgssconfig.jar' \
	--py-files /home/your_code_path/pyspark_teradata_connection.py
"""

ssh_operator = SSHOperator(
	task_id='etl_teradata',
	command=cmd,
	dag=dag
)

dummy_operator >> ssh_operator
