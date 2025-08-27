import qrcode
from PIL import Image, ImageDraw

# Texto o URL del QR
data = "http://learnix-bit.github.io/"

# Crear código QR clásico (con puntitos)
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección para soportar logo
    box_size=10,  # tamaño de cada puntito
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# Convertir a imagen
qr_img = qr.make_image(fill_color="white", back_color="black").convert("RGB")

# Hacer un círculo transparente en el centro
draw = ImageDraw.Draw(qr_img)
w, h = qr_img.size
circle_size = 120  # diámetro del círculo
circle_pos = ((w - circle_size)//2, (h - circle_size)//2,
              (w + circle_size)//2, (h + circle_size)//2)

draw.ellipse(circle_pos, fill="black")  # círculo negro en el medio (fondo oscuro)

# Insertar el logo encima del círculo
logo_path = r"C:\Modelos de Learnix\Learnix Principal\img\logo\logo-con-fondo.png"
logo = Image.open(logo_path).convert("RGBA")

# Redimensionar logo al tamaño del círculo
logo = logo.resize((circle_size, circle_size))

# Pegar logo en el centro
qr_img.paste(logo, ((w - circle_size)//2, (h - circle_size)//2), logo)

# Guardar resultado
qr_img.save("learnix_qr.png")
print("✅ QR con logo generado correctamente.")
