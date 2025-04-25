# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="app/static"), name="static")
# templates = Jinja2Templates(directory="app/templates")


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/calculate")
# async def calculate(num1: float, num2: float, op: str):
#     print("operand is:", op)
#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "/":
#         result = num1 / num2 if num2 != 0 else "Infinity"
#     else:
#         result = "Invalid Operation"
#     return {"result": result}


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
