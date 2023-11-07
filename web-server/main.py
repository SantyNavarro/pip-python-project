import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def getList():
    return [1, 2, 3]


@app.get("/contact", response_class=HTMLResponse)
def getList():
    return """
        <h1>Hello mates!!</h1>
        <p>How is it going?!</p>
    """


def run():
    store.getCategories()


if __name__ == "__main__":
    run()
