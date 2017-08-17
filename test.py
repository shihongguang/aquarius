from aquarius import Aquarius
from response import json_response

app = Aquarius()

@app.route("/")
def test(request):
    return json_response({"result": "aquarius is faster"})

app.start(port=8001)