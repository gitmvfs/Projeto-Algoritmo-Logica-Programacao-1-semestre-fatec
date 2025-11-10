from fastapi import FastAPI
from routes.routes import user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")  #Rota padrão da api para testar conexão
def root():
    return{"Message":"Api running"}
