from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Geminis saubere CORS-Einstellungen
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Daten-Modell für TypeScript-Kompatibilität
class CompanyMetric(BaseModel):
    name: str
    revenue: str
    changeValue: str
    changePercent: str
    isPositive: bool

# Kombinierte Routen
@app.get("/api/ping")
async def ping():
    return {"status": "ok", "message": "FastAPI is connected"}

@app.get("/api/metrics", response_model=List[CompanyMetric])
async def get_metrics():
    # Hier kommen die Daten für dein Vue-Dashboard rein
    return [
        {"name": "Apple", "revenue": "38.52", "changeValue": "1.06", "changePercent": "2.83", "isPositive": True},
        {"name": "Meta", "revenue": "435.57", "changeValue": "5.81", "changePercent": "1.32", "isPositive": False},
        # ... die restlichen Firmen
    ]