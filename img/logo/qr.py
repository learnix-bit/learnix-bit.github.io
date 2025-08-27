import qrcode
from PIL import Image, ImageDraw

# --- Datos del QR ---
data = "http://learnix-bit.github.io/"

# --- Crear QR ---
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# --- Generar QR con fondo oscuro ---
img_qr = qr.make_image(fill_color="white", back_color="#0a0a0a").convert("RGBA")

# --- Abrir logo (con fondo ya preparado por ti) ---
logo = Image.open(r"C:\Modelos de Learnix\Learnix Principal\img\logo\logo-con-fondo.png").convert("RGBA")

# --- Redimensionar logo manteniendo proporción ---
logo_size = int(img_qr.size[0] * 0.23)  # 23% del tamaño del QR
logo.thumbnail((logo_size, logo_size), Image.LANCZOS)

# --- Posición centrada ---
logo_pos = ((img_qr.size[0] - logo.size[0]) // 2,
            (img_qr.size[1] - logo.size[1]) // 2)

# --- Crear espacio circular (vacío) para el logo ---
circle_size = max(logo.size) + 20  # círculo un poco más grande que el logo
mask_circle = Image.new("L", (circle_size, circle_size), 0)
draw = ImageDraw.Draw(mask_circle)
draw.ellipse((0, 0, circle_size, circle_size), fill=255)

# Crear una capa transparente
circle_space = Image.new("RGBA", img_qr.size, (0, 0, 0, 0))
circle_pos = ((img_qr.size[0] - circle_size) // 2,
              (img_qr.size[1] - circle_size) // 2)

# Pegar un círculo del color de fondo para limpiar el área del logo
draw_bg = ImageDraw.Draw(circle_space)
draw_bg.ellipse((circle_pos[0], circle_pos[1],
                 circle_pos[0] + circle_size,
                 circle_pos[1] + circle_size),
                fill="#0a0a0a")  # mismo color que el fondo del QR

# Combinar QR + círculo
img_qr = Image.alpha_composite(img_qr, circle_space)

# --- Pegar logo encima ---
img_qr.alpha_composite(logo, logo_pos)

# --- Guardar resultado ---
img_qr.save("qr_con_logo_style.png")

print("✅ QR profesional con espacio circular y logo generado correctamente.")
