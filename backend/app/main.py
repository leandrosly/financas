from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Finanças API",
    description="API para controle financeiro pessoal",
    version="1.0.0",
)

# Permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Na produção, ajustar para o domínio certo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API do Finanças está rodando"}
