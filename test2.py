from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route("/")
async def test(request):
    return json({"result": "aquarius is faster"})

app.run(host="0.0.0.0", port=8001)