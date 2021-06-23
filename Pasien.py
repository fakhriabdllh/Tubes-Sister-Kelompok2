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

    if guldar >= 70 and guldar <= 200: #normal via ayosurabaya.com
        print("Kadar gula darah anda normal")
        pesan = "Kadar gula darah pasien normal"
        client_socket.send(pesan.encode())
        data = client_socket.recv(1024).decode()
        print('')
        print("Pesan dari dokter : " + data)
        saran()
    
    elif guldar < 70: #rendah via ayosurabaya.com
        print("Kadar gula darah anda rendah, silahkan tunggu saran dari dokter.")
        pesan = "Kadar gula darah pasien rendah"
        client_socket.send(pesan.encode())
        data = client_socket.recv(1024).decode()
        print('')
        print('Pesan dari dokter : ' + data)
        saran()

    elif guldar > 200: #tinggi via ayosurabaya.com
        print("Kadar gula darah anda tinggi, silahkan tunggu saran dari dokter.")
        pesan = "Kadar gula darah pasien tinggi"
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

def menu():
    lanjut = str(input("Selamat datang di aplikasi pengontrol gula darah, ingin melanjutkan?(y/n)"))
    if lanjut.upper() == 'Y' or lanjut.lower() == 'y':
        pasien_client()
    elif lanjut .upper() == 'N' or lanjut.lower() == 'n':
        layout()
        print("Terima kasih telah menggunakan aplikasi kami")
        client_socket.close()
    else:
        layout()
        print('Masukan salah, coba lagi')
        menu()

if __name__ == '__main__':
    layout()
    menu()
