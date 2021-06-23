import socket
import os

host = socket.gethostname()
port = 5000

client_socket = socket.socket()
client_socket.connect((host, port))

def layout():
    _ = os.system('cls')
    print("==========================================")
    print("     APLIKASI PENGONTROL GULA DARAH")
    print("               --Pasien--")
    print("==========================================")

def pasien_client():
    print('')
    guldar = int(input('Masukkan kadar gula darah anda: '))

    if guldar >= 80 and guldar <= 120:
        print("Gula darah anda normal, anda tidak perlu saran dari dokter.")
        print('')
        saran()
    
    elif guldar < 80:
        print("Kadar gula darah anda rendah, silahkan tunggu saran dari dokter.")
        pesan = "Gula darah pasien rendah"
        client_socket.send(pesan.encode())
        data = client_socket.recv(1024).decode()
        print('')
        print('Pesan dari dokter : ' + data)
        saran()

    elif guldar > 120:
        print("Kadar gula darah anda tinggi, silahkan tunggu saran dari dokter.")
        pesan = "Gula darah pasien tinggi"
        client_socket.send(pesan.encode())
        data = client_socket.recv(1024).decode()
        print('')
        print('Pesan dari dokter : ' + data)
        saran()

def saran():
    print('')
    print("Ingin meminta lagi saran dari dokter?(y/n)")
    x = input("")
    if x.upper() == 'Y' or x.lower() == 'y':
        layout()
        pasien_client()
    elif x.upper() == 'N' or x.lower() == 'n':
        layout()
        print("Terima kasih, Semoga lekas sembuh")
        client_socket.close()
    else:
        saran()

if __name__ == '__main__':
    layout()
    pasien_client()