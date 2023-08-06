from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


#(uvicorn src.fastapi_tamplete_jinja2:app --reload)

#starta o corno 
app = FastAPI()

# usar o app do fastapi para montar o template (essas pastas não podem ficar na raiz aparentimente mas por que?)
app.mount("/static", StaticFiles(directory="static"), name="static")

#usando a pasta que temos chamada de templates (essas pastas não podem ficar na raiz aparentimente mas por que?)
templates = Jinja2Templates(directory="templates")

# / decoretor (que é a roda) ,  e uma classe response (versão antiga)
# @app.get("/", response_class=HTMLResponse)
#usando o jinja 
@app.get("/{nome}", response_class=HTMLResponse)

#função assincrona (root())
#esse request recebe uma variavel request do tipo Request (import)
async def root(request: Request,nome: str):
    #documentando do que é a rota no proprio docs ( http://127.0.0.1:8000/docs )
    """
    # rota projeto
    ## projeto teste
    """  
    #retorna aquele templates que tinha antes o html cuspido aqui...    (é um dict)
    return templates.TemplateResponse("index.html",{"request": request, "nome": nome})

