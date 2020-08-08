from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 按http协议解析数据environ
    # 按http协议组装数据start_response



    # 当前请求路径
    path = environ.get("PATH_INFO")
    start_response('200 OK', [])
    print(path)
    if path == "/login":
        with open("login.html", "r") as f:
            data = f.read()

    elif path == "/index":
        with open("index.html", "r") as f:
            data = f.read()

    return [data.encode("utf8")]


# 封装socket
httped = make_server("127.0.0.1", 8000, application)

# 等待用户连接
httped.serve_forever()
