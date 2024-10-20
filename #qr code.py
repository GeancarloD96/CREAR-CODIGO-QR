#qr code
import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#Añadir datos al objeto QR
qr.add_data("https://www.virtualdrumming.com/drums/online-virtual-games/online-virtual-games-drums.html")
qr.make(fit=True)

#Crear la imagen del codigo QR
img = qr.make_image(fill_color="blue", back_color="white")

#Guardar imagem qr
img.save("qr.png")

print("codigo qr personalizado es generado y guardado como 'qr.png'")