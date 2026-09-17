from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.bash import BashOperator


REPO_ROOT = Path(__file__).resolve().parents[2]
CD_REPO = f'cd "{REPO_ROOT}"'


with DAG(
    dag_id="wine_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
    max_active_runs=1,
    is_paused_upon_creation=False,
) as dag:
    prepare_data = BashOperator(
        task_id="prepare_data",
        bash_command=f"{CD_REPO} && python -m src.data",
    )

    train_model = BashOperator(
        task_id="train_model",
        bash_command=f"{CD_REPO} && python -m src.train",
    )

    deploy = BashOperator(
        task_id="deploy",
        bash_command=(
            f"{CD_REPO} && "
            "docker compose up -d --build --force-recreate api app"
        ),
    )

    prepare_data >> train_model >> deploy
