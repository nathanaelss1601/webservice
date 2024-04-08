from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {'Hello World'}

@app.get("/page1")
async def read_page1():
    return {'Hello World 1'}

@app.get("/page2")
async def read_page2():
    return {'Hello World 2'}