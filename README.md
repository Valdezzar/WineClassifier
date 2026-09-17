# MLOps pipeline

## Requirements

Python 3.11, Docker Desktop, and Docker Compose. On Windows, use WSL2/Linux for Airflow if native Windows is problematic.

## Dataset

Wine dataset from sklearn.datasets.load_wine.

It has 178 samples and 3 wine cultivar classes. The project uses exactly four features: alcohol, malic_acid, color_intensity, proline.

The application shows classes as cultivar_1, cultivar_2, cultivar_3.

## Setup

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Linux/WSL:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Airflow

Use the command block that matches your terminal. Bash syntax such as `export` does not work in PowerShell.

Windows PowerShell:

```powershell
$env:AIRFLOW_HOME = "$PWD\airflow"
$AIRFLOW_VERSION = "2.10.5"
$PYTHON_VERSION = "3.11"
$CONSTRAINT_URL = "https://raw.githubusercontent.com/apache/airflow/constraints-$AIRFLOW_VERSION/constraints-$PYTHON_VERSION.txt"
pip install "apache-airflow==$AIRFLOW_VERSION" --constraint "$CONSTRAINT_URL"
airflow db migrate
airflow standalone
```

If Airflow fails on native Windows with `No module named 'pwd'`, run it from WSL2/Linux instead.

Linux/WSL:

```bash
cd /mnt/c/Games/PMLDL/Assignment_1
export AIRFLOW_HOME="$(pwd)/airflow"
AIRFLOW_VERSION=2.10.5
PYTHON_VERSION=3.11
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
airflow db migrate
airflow standalone
```

Airflow UI is at http://localhost:8080. The standalone command prints the admin password.

Use another terminal from the activated environment to unpause and trigger the DAG without waiting five minutes.

PowerShell:

```powershell
$env:AIRFLOW_HOME = "$PWD\airflow"
airflow dags unpause wine_pipeline
airflow dags trigger wine_pipeline
```

Linux/WSL:

```bash
export AIRFLOW_HOME="$(pwd)/airflow"
airflow dags unpause wine_pipeline
airflow dags trigger wine_pipeline
```

## Run

Create the data files, train the model, and start both services.

```bash
python -m src.data
python -m src.train
docker compose up -d --build api app
```

## MLflow

```bash
mlflow ui --backend-store-uri ./mlruns
```

MLflow UI is at http://localhost:5000.

## Services

FastAPI docs are at http://localhost:8000/docs.

Streamlit is at http://localhost:8501.
