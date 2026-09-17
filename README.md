# MLOps pipeline

Wine dataset from sklearn.datasets.load_wine: 178 samples, 3 wine cultivar classes. The model uses alcohol, malic_acid, color_intensity, and proline. The application shows cultivar_1, cultivar_2, and cultivar_3.

## Windows PowerShell

Install Python 3, Git, and Docker Desktop with Docker Compose. Run these commands in PowerShell.

First setup:

```powershell
git clone https://github.com/Valdezzar/WineClassifier.git
cd WineClassifier
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m src.data
python -m src.train
docker compose up -d --build api app
```

Later starts, from the project directory:

```powershell
docker compose up -d api app
.\.venv\Scripts\Activate.ps1
mlflow ui --backend-store-uri ./mlruns
```

The MLflow command keeps this terminal open. FastAPI docs: http://localhost:8000/docs. Streamlit: http://localhost:8501. MLflow: http://localhost:5000. Run Airflow on Linux as shown below.

## Linux terminal

Install Python 3.11 or 3.12 with venv and pip, Git, Docker Engine, and the Docker Compose plugin. Start Docker and run these commands in a Linux terminal.

First setup:

```bash
git clone https://github.com/Valdezzar/WineClassifier.git
cd WineClassifier
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export AIRFLOW_HOME="$(pwd)/airflow"
AIRFLOW_VERSION=2.10.5
PYTHON_VERSION=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
python -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
python -m src.data
python -m src.train
docker compose up -d --build api app
```

After first setup and on every later start, use two Linux terminals in the project directory. In terminal 1:

```bash
source .venv/bin/activate
export AIRFLOW_HOME="$(pwd)/airflow"
docker compose up -d api app
airflow standalone
```

In terminal 2:

```bash
source .venv/bin/activate
mlflow ui --backend-store-uri ./mlruns
```

Open Airflow at http://localhost:8080, FastAPI docs at http://localhost:8000/docs, Streamlit at http://localhost:8501, and MLflow at http://localhost:5000. The first Airflow standalone run prints the admin password. The wine_pipeline DAG prepares data, trains the model, and redeploys the Docker services every five minutes; you can also run it immediately:

```bash
airflow dags trigger wine_pipeline
```
