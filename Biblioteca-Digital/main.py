from fastapi import FastAPI
from api.routes.leitores import router as leitores_router
from api.routes.livros import router as livros_router

app = FastAPI(Title="Biblioteca API")

app.include_router(leitores_router)
app.include_router(livros_router)