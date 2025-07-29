from fastapi import APIRouter
from services.negociacoes import get_negociacoes

router = APIRouter()

@router.get("/negociacoes")
def listar_negociacoes():
    return get_negociacoes()
