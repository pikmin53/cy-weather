from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import Response
import time
from fastapi.middleware.cors import CORSMiddleware
from src.resources.weather_resource import router as weather_router


tags_metadata = [
    {
        "name": "Health",
        "description": "Health check endpoints",
    },
    {
        "name": "Weather",
        "description": "Endpoints pour récupérer les données météo actuelles et les prévisions",
    },
]

app = FastAPI(
    title="CY Weather API",
    description="API for CY Weather application",
    version="0.1.0",
    openapi_tags=tags_metadata,
    redoc_url="/docs",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(
    prefix="/api",
)


@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok"}


app.include_router(router)
app.include_router(weather_router, prefix="/api")



@app.get("/metrics")
async def metrics_endpoint():
    """Endpoint compatible Prometheus: récupère toutes les métriques enregistrées."""
    from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
