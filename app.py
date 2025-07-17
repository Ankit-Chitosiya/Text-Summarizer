from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from TextSummarizer.pipeline.prediction import PredictionPipeline
import uvicorn



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, text: str = Form(...)):
    print("Received text:", text)
    summary = PredictionPipeline().predict(text)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": summary,
        "input_text": text
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
