from sanic import Sanic
from sanic.response import json
from sanic.response import text
from sanic import response
app = Sanic()

rv = {1:0,2:0,3:0,4:0}
guard = {1:1,2:1,3:1,4:1}
yourrv = 0


def rail(k,v):   # k는 html로부터 얻은 주차 위치 데이터
    k,v=int(k),int(v) # v는 guard로부터 얻어오는 가드레일 상태 데이터
    guard[k]=(v+1)%2


@app.route('/')
async def main_def(request):
    return await response.file('./payment.html') # (수정 1)

@app.route("/payment")
async def payment_def(request): # async는 아마 비동기로 만들어주는? 것이다.
    return await response.file('./',request.query_args[0][1],'.html')

@app.route("/choose")
async def payment_def(request): # async는 아마 비동기로 만들어주는? 것이다.
    return await response.file('./',request.query_args[0][1],'.html')

@app.route("/parking")
async def choose_def(request):
    yourrv = int(request.query_args[0][0])
    rv[yourrv] = int(request.query_args[0][1])
    print(rv)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


# 변수를 위와같이 만들었는데, 이 서버에 접속한 사람들이 값을 공유하는지(해야함)
# yourrv만 공유를 하면 안되는데, 이는 어떻게 해결해야하는지(리스트append pop)


#1. 결제 페이지. 누른다면 html 코드에서 ?page=choose 데이터를 보내
# (수정 1)의 내용을 '고정값' 을 '변수+고정값'으로 바꿔야 한다.
#2. html 코드에서 rv딕셔너리를 얻어와 버튼의 상태에 따라 버튼을 보여준다.
#3. html 코드에서 버튼을 눌렀을 때 ?page=(다음거) 데이터와(&) 몇번째(key)
# 버튼을 눌렀는지와 = 1 을 보내서 rv딕셔너리를 수정한다.
#4. html 코드에서 page 정보를 얻어와 이동시키고 yourrv에 따라 지도를 만들어
# 목적지의 위치를 표시해 준다.
#5. html 코드에서 가드레일 제어 버튼을 만든다.
#6. 초기 가드레일 상태는 up 이다. 
# 초기 가드레일 제어 버튼의 이름은 '주차 시작' 이다.
# 가드레일 제어 버튼을 누르면 ?yourrv값(key) = 버튼의 몇번째(value) 누름
# 값이 오면 먼저 몇번째 누름인지 확인해서 4번째 이상의 누름이면
# 주차시간 타이머를 멈추고 종료? 시킨다.
# 3번째 이하의 누름이라면 rail(yourrv, guard[yourrv])를 통해
# 가드레일을 올리거나 내린다.
# '주차시작' -> '주차완료' -> '출차시작' -> '출차완료'

# ... 위치선택으로 정상적이지 않은 방법으로 접근하여 마구잡이로 선택을 할 경우
# 어케 해결해..?