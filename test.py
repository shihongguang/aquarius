from aquarius import Aquarius
from response import to_json_response

app = Aquarius()

@app.route("/")
def test(request):
    return to_json_response({"result": "aquarius is faster"})

app.start(port=8001)