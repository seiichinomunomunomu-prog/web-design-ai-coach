from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi import Form


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )   

    
@app.post("/review")                                                                  
def review(
    html_code: str = Form(...),
    css_code: str = Form(...),
    question: str = Form(...)
):

    return {
        "html": html_code,
        "css": css_code,
        "question": question
    }