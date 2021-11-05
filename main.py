
from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.config import settings
import data.ids_data as ids_data
import os
import json
import datetime
import asyncio
from aiohttp import ClientSession

templates = Jinja2Templates(directory="templates")

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

id_cities = ids_data.location_list()
dict_requests = {}
#json_directory = os.path.join(os.path.dirname(__file__) + "data/"


# Criando dicionário com dados de requisições realizadas do arquivo JSON
if os.path.exists('data/data.json'):
    try:
        temp = json.load(open('data/data.json'))
        for key in temp.keys():
            dict_requests[key] = len(temp.get(key))
    except:
        pass
else:
    print("Arquivo não encontrado!!")


# Página inicial
@app.get("/home", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})


# Cria ID da requisição e faz chamada a função que coleta os dados por meio climáticos
@app.post("/getWeather")
async def post_request(background_tasks: BackgroundTasks, request: Request, id_post: str = Form(...), ):
    if os.path.exists('data/data.json'):
        try:
            dict_data = json.load(open('data/data.json'))
        except:
            pass
    else:
        dict_data = {}
    check_id = dict_requests.get(id_post)
    if check_id:
        return templates.TemplateResponse("home.html", context={"request":request, "msg": "ID já esta sendo utilizado!"})
    else:
        templates.TemplateResponse("home.html", context={"request":request, "msg":"ID aceito, requisição sendo executada!"})        
        dict_requests[id_post] = 0
        background_tasks.add_task(await weather_api(dict_data, id_post))
        return templates.TemplateResponse("home.html", context={"request":request, "msg":"Requisiçaõ Finalizada!"})


# Verifica a porcentagem das requisições
@app.post("/status")
async def get_request(request: Request, id_verifiy: str = Form(...)):
    try:
        number_requests = dict_requests.get(id_verifiy)
        porcent = str(round(((number_requests*100)/167), 1)) + "%"
        return templates.TemplateResponse("home.html", context={"request":request, "msg": porcent})
    except:
        return templates.TemplateResponse("home.html", context={"request":request, "msg": "ID não encontrado!"})    


# Função que faz as requisições na api e armazena o resultado
async def weather_api(dict_data: dict, id_post: str, units="metric") -> dict:
    dtime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    city_data = {}
    for city in id_cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?id={city}&units={units}&appid={settings.API_KEY}"
        async with ClientSession() as session:
            async with session.request(method='GET', url=url) as response:
                if response.status == 200:
                    response = await response.json()
                    city_data[city] = {
                                        'temp': response['main']['temp'], 
                                        'humidity': response['main']['humidity'], 
                                        'datetime': dtime
                                    }
                else:
                    pass
        dict_requests[id_post] += 1
        await asyncio.sleep(1)
    dict_data[id_post] = city_data
    json_data = json.dumps(dict_data)
    with open('data/data.json', 'w') as f:
        f.write(json_data)
        f.close()
    return dict_data

