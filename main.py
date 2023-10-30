import socket

IP = 192.168.1.38   
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP,PORT))
s.listen(5)
print("Sunucu kuruldu. İstemci/İstemciler bekleniliyor.")

try:
    s.accept((istemci, adres))
    baglanti = True
    print("İstemci/İstemciler sunucuya bağlandı!")

except Exception as hata:
    print(f"Hata: {hata}")
