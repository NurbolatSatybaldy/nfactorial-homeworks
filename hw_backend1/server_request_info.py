from wsgiref.simple_server import make_server
import json

def app(environ, start_response):
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    protocol = environ["SERVER_PROTOCOL"]
    if path == "/info":
        response_data = {
            "method": method,
            "url": environ["PATH_INFO"],
            "protocol": protocol
        }
        start_response("200 OK", [("Content-Type", "application/json")])
        return [json.dumps(response_data).encode()]
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Not Found"]

if __name__ == "__main__":
    with make_server("127.0.0.1", 8000, app) as server:
        print("Сервер запущен на http://127.0.0.1:8000")
        server.serve_forever()

