from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def transform_tasks():

  with TaskGroup("transformations", tooltip="Transform tasks") as group:

    transformation_a = BashOperator(
      task_id = 'transformation_a',
      bash_command = 'sleep 10'
    )
    transformation_b = BashOperator(
      task_id = 'transformation_b',
      bash_command = 'sleep 10'
    )
    transformation_c = BashOperator(
      task_id = 'transformation_c',
      bash_command = 'sleep 10'
    )

    return group
        