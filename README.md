# MLOps pipeline

Wine dataset from sklearn.datasets.load_wine.

It has 178 samples and 3 wine cultivar classes. The project uses exactly four features: alcohol, malic_acid, color_intensity, proline.

The application shows classes as cultivar_1, cultivar_2, cultivar_3.

## Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```powershell
$env:AIRFLOW_HOME = "$PWD\airflow"
$AIRFLOW_VERSION = "2.10.5"
$PYTHON_VERSION = "3.11"
$CONSTRAINT_URL = "https://raw.githubusercontent.com/apache/airflow/constraints-$AIRFLOW_VERSION/constraints-$PYTHON_VERSION.txt"
pip install "apache-airflow==$AIRFLOW_VERSION" --constraint "$CONSTRAINT_URL"
airflow db migrate
airflow standalone
```

Airflow UI is at http://localhost:8080. The standalone command prints the admin password.

Use another terminal from the activated environment to unpause and trigger the DAG without waiting five minutes.

```powershell
$env:AIRFLOW_HOME = "$PWD\airflow"
airflow dags unpause wine_pipeline
airflow dags trigger wine_pipeline
```

```powershell
python -m src.data
python -m src.train
docker compose up -d --build api app
```

```powershell
mlflow ui --backend-store-uri ./mlruns
```

MLflow UI is at http://localhost:5000.

FastAPI docs are at http://localhost:8000/docs.

Streamlit is at http://localhost:8501.

## Linux terminal

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```bash
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

```bash
source .venv/bin/activate
export AIRFLOW_HOME="$(pwd)/airflow"
airflow dags unpause wine_pipeline
airflow dags trigger wine_pipeline
```

```bash
source .venv/bin/activate
python -m src.data
python -m src.train
docker compose up -d --build api app
```

```bash
source .venv/bin/activate
mlflow ui --backend-store-uri ./mlruns
```

MLflow UI is at http://localhost:5000.

FastAPI docs are at http://localhost:8000/docs.

Streamlit is at http://localhost:8501.
