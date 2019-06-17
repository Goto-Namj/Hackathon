from sanic import Sanic
from sanic.response import json
from sanic.response import text
from sanic import response
app = Sanic()

rv = {1:0,2:0,3:0,4:0}
guard = {1:1,2:1,3:1,4:1}
number = 0

def rail(k,v):
    global guard
    k,v=int(k),int(v)
    guard[k]=(v+1)%2

@app.route('/')
async def main_def(request):
    return await response.file('./payment.html')

@app.route("/payment")
async def payment_def(request): # async는 아마 비동기로 만들어주는? 것이다.
    return await response.file('./choose.html')

@app.route("/choose")
async def choose_def(request):
    global rv
    return text(rv)

@app.route("/apnd")
async def apnd_def(request):
    global number
    global rv
    rv[int(request.query_args[0][0])] = int(request.query_args[0][1])
    number = int(request.query_args[0][0])
    return 0

@app.route("/parking")
async def parking_def(request):
    return await response.file('./parking.html')

@app.route("/pipe")
async def pipe_def(request):
    global number
    return text(number)
    
@app.route("/guardrail")
async def guardrail_def(request):
    rail(int(request.query_args[0][0]) , int(request.query_args[0][1]))
    return 0

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

    