import socket


def calculate(expression):
    try:
        result = eval(expression)
        return f"Resultatet av {expression} är {result}"
    except Exception as e:
        return str(e)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    print("Servern startad på port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Ansluten till {addr}")

        expression = client_socket.recv(1024).decode()
        response = calculate(expression)

        client_socket.send(response.encode())
        client_socket.close()


if __name__ == "__main__":
    start_server()
