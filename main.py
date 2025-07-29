from fastapi import FastAPI
from rdstation_api.app.routes import negociacoes
from rdstation_api.app.routes import leads

app = FastAPI()

# Registrar as rotas
app.include_router(leads.router)
app.include_router(negociacoes.router)