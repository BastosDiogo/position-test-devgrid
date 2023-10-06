from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rotas import clima
from rotas import basedados


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clima.router)
app.include_router(basedados.router)
