from robyn import Robyn
import json
from stac_api_robyn.core import CoreCrudClient
from stac_api_robyn.transactions import TransactionsClient
app = Robyn(__file__)

@app.get("/")
async def h(requests):
    return "Hello, world!"

@app.post("/collections")
async def create_collection(request):
    client = TransactionsClient()
    collection = json.loads(bytearray(request["body"]).decode("utf-8"))
    client.create_collection(model=collection)

@app.get("/collections")
async def create_collection(request):
    client = CoreCrudClient()
    return json.dumps({
        "collections": client.all_collections()
    })

app.start(port=5000, url="0.0.0.0")
