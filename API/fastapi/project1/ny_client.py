#uvicorn ny_client:app --reload --port 8001
#localhost:8001
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import requests
import nj_advanced_server

ITEM_NAMES = list(nj_advanced_server.catalog.keys())

API_URL = "http://localhost:8000/warehouse"

app = FastAPI(title="API Appli")
app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static"
)

templates = Jinja2Templates(directory="templates")
#The @app.get("/") endpoint renders an HTML form (index.html) with a list of products from ITEM_NAMES, which is derived from nj_advanced_server.catalog.keys().
@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "products": ITEM_NAMES
        }
    )
#The @app.post("/") endpoint handles form submissions, extracts product and order_qty from the form data, sends a GET request to the backend server
@app.post("/", response_class=HTMLResponse)
def send(
    request: Request, 
    product: str = Form(...), 
    order_qty: int = Form(...)
):
    r = requests.get(
        f"{API_URL}/{product}", 
        params={"order_qty": order_qty}
    )
    data = r.json()
    #and renders a result page (result.html) with the response.
    return templates.TemplateResponse(
        "result.html", 
        {"request": request, "result": data}
    )
