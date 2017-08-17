# aquarius
基于python3极简web框架

response is a json string


# useing test

```pyrhon
from aquarius import Aquarius
from response import json_response

app = Aquarius()

@app.route("/")
def test(request):
    return json_response({"result": "aquarius is faster"})

app.start(port=8001)
```