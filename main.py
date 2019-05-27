from sanic import Sanic
from sanic.response import json
from sanic.response import text

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route('/post', methods=['POST'])
async def post_handler(request):
	return text('POST request - {}'.format(request.json))

@app.route('/get', methods=['GET'])
async def get_handler(request):
	return text('GET request - {}'.format(request.args))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)