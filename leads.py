from fastapi import APIRouter

router = APIRouter()

@router.get("/leads")
def listar_leads():
    return [{"id": 1, "nome": "Lead Exemplo"}]