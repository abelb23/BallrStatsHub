from fastapi import FastAPI;
from api.v1.routes.issues import router as issues_router
from middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(issues_router)

app.middleware("http")(timer_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)