import socket
import os

def layout():
    _ = os.system('cls')
    print("==========================================")
    print("     APLIKASI PENGONTROL GULA DARAH")
    print("               --Dokter--")
    print("==========================================")
    print('')

def dokter_server():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Koneksi dari pasien dengan alamat IP: " + str(address))
    print('')
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        layout()
        print("Koneksi dari pasien dengan alamat IP: " + str(address))
        print("Pesan dari pasien: " + str(data))
        data = str(input('Pesan untuk pasien : '))
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    layout()
    dokter_server()
