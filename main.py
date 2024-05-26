import socket
import threading


def handle_client(client_socket):
    while True:
        try:
            # Ta emot meddelande från klienten
            message = client_socket.recv(1024).decode()
            if not message:
                break

            # Dela upp meddelandet för att utföra beräkningen
            parts = message.split()
            if len(parts) != 3:
                response = "Fel format, använd ex: '1 + 2'"
            else:
                try:
                    num1 = int(parts[0])
                    operator = parts[1]
                    num2 = int(parts[2])

                    if operator == '+':
                        result = num1 + num2
                        response = f"Summan av {num1} + {num2} är {result}"
                    elif operator == '-':
                        result = num1 - num2
                        response = f"Skillnaden av {num1} - {num2} är {result}"
                    elif operator == '*':
                        result = num1 * num2
                        response = f"Produkten av {num1} * {num2} är {result}"
                    elif operator == '/':
                        result = num1 / num2
                        response = f"Kvoten av {num1} / {num2} är {result}"
                    else:
                        response = "Ogiltig operator, använd +, -, * eller /"
                except ValueError:
                    response = "Felaktiga tal, använd ex: '1 + 2'"

            # Skicka svar tillbaka till klienten
            client_socket.send(response.encode())

        except:
            break

    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    print("Servern startad på port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Ansluten till {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
