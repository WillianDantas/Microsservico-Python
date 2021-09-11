import time
from threading import Thread

from starlette.routing import Host

from common import Base
from lib import teste
from models import Pessoa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn

# def executa_algo(arg):
#     for val in arg:
#         if val == "i":
#             break
#         print(val)


# def multiply():
#     nums = [1, 2, 3, 4, 5]
#     for num in nums:
#         # .... geração de relatórios ....

#         yield num*num


# def multiplye():
#     yield 1*1
#     time.sleep(1)
#     yield 2*2
#     time.sleep(1)
#     yield 3*3
#     time.sleep(1)
#     yield 4*4
#     time.sleep(1)
#     yield 5*5
#     time.sleep(1)
#     yield 6*6
#     time.sleep(1)


# def power():
#     yield 1**1
#     time.sleep(1)
#     yield 2**2
#     time.sleep(1)
#     yield 3**3
#     time.sleep(1)
#     yield 4**4
#     time.sleep(1)
#     yield 5**5
#     time.sleep(1)
#     yield 6**6
#     time.sleep(1)


# def executa(function):
#     function("aaaa")


# def exec(function):
#     function()


# def printa(x):
#     print(x)


# def main():
#     nome = "Radix"

#     resultado = executa_algo(nome)
#     for value in multiply():
#         print(value)

#     print(teste().nota)

#     executa(lambda x: print(x))
#     executa(printa)
#     exec(lambda: print("teste"))

#     print("---------\n")

#     thread1 = Thread(target=itera_multiply)
#     thread2 = Thread(target=itera_power)

#     thread2.start()
#     thread1.start()


# def itera_multiply():
#     for result in multiplye():
#         print(result)


# def itera_power():
#     for result in power():
#         print(result)


app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    while True:
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")


# switch  case foi introduzido no python 3.10
# Session = sessionmaker()
# if __name__ == "__main__":
    #uvicorn.run(app, host="127.0.0.1", port=8081)
    #main()
    #engine = create_engine('sqlite:///modulo1.sqlite', echo=True)

    # print(p.__tablename__)

    #Base.metadata.create_all(engine)

    #Session.configure(bind=engine)
    #session = Session()

    #p = Pessoa(name="João", email="joão@radix.com", last_name="Miranda")

    #session.add(p)
    #session.commit()

