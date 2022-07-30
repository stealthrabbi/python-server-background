from bottle import route, run, template, WSGIRefServer
import time
import threading

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

server = WSGIRefServer(host="localhost", port=8080)

def run_server():
    run(server=server)

x = threading.Thread(target=run_server)
x.start()
print("i am doing stuff now")
time.sleep(5.0)
print("done sleeping")
server.srv.shutdown()
print("stopped server hopefully")
