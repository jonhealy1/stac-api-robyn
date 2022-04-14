from robyn import Robyn

app = Robyn(__file__)

@app.get("/")
async def h(requests):
    return "Hello, world!"

app.start(port=5000, url="0.0.0.0")