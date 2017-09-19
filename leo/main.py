from app import Aquarius
from response import json_response

app = Aquarius(__name__)

@app.route("/")
async def test1(request):
    print(request.method)
    if request.method == "GET":
        return json_response({"name": "shihongguang"})


app.run(port=8002, host="0.0.0.0")