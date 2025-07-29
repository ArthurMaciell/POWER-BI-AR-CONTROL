from fastapi import FastAPI
from app.routes import negociacoes
from app.routes import leads

app = FastAPI()

# Registrar as rotas
#app.include_router(leads.router)
app.include_router(negociacoes.router)