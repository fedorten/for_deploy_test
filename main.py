from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Session, User


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Роут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# Роут для регистрации
@app.post("/")
async def register(username: str = Form(...), password: str = Form(...)):
    with Session() as session:
        user = User(name=username, password=password)
        session.add(user)
        session.commit()

    return RedirectResponse("/success", status_code=303)


# Роут для страницы успеха
@app.get("/success", response_class=HTMLResponse)
async def success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


if __name__ == "__main__":
    app.run()
