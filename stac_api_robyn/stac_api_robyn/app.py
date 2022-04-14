from robyn import Robyn
from stac_api_robyn.core import CoreCrudClient
from stac_api_robyn.transactions import TransactionsClient
app = Robyn(__file__)

@app.get("/")
async def h(requests):
    return "Hello, world!"

app.start(port=5000, url="0.0.0.0")