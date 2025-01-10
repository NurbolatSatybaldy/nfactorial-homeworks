from wsgiref.simple_server import make_server

def app(environ, start_response):
    path = environ["PATH_INFO"]  # Путь из запроса
    if path == "/ping":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"pong"]
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Not Found"]

if __name__ == "__main__":
    with make_server("127.0.0.1", 8000, app) as server:
        print("Сервер запущен на http://127.0.0.1:8000")
        server.serve_forever()

