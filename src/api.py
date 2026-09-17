from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "model.joblib"
CLASS_NAMES = ["cultivar_1", "cultivar_2", "cultivar_3"]

FEATURES = [
    "alcohol",
    "malic_acid",
    "color_intensity",
    "proline",
]

model = joblib.load(MODEL_PATH)
app = FastAPI()


class PredictionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    alcohol: float
    malic_acid: float
    color_intensity: float
    proline: float


class PredictionResponse(BaseModel):
    class_id: int
    class_name: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    row = pd.DataFrame(
        [
            {
                FEATURES[0]: request.alcohol,
                FEATURES[1]: request.malic_acid,
                FEATURES[2]: request.color_intensity,
                FEATURES[3]: request.proline,
            }
        ]
    )
    class_id = int(model.predict(row)[0])
    return PredictionResponse(class_id=class_id, class_name=CLASS_NAMES[class_id])
