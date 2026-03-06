# ../../.venv/Scripts/activate

import cv2
import os
import numpy as np
import json
import tkinter as tk

pasta = os.path.dirname(os.path.abspath(__file__))

pagina_file = os.path.join(pasta, "c - pagina.txt")
with open(pagina_file, "r", encoding="utf-8") as f:
    pagina = f.readline().strip()

print("Página carregada:", pagina)

# ==============================
# Detectar resolução da tela
# ==============================
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# ==============================
# Caminhos
# ==============================
img_path = os.path.join(pasta, f"{pagina}.jpg")
txt_path = os.path.join(pasta, f"{pagina}.txt")

print("Imagem:", img_path)

# ==============================
# Carregar imagem
# ==============================
with open(img_path, "rb") as f:
    file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
    img_original = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

if img_original is None:
    raise FileNotFoundError(f"Não foi possível carregar a imagem: {img_path}")

orig_h, orig_w = img_original.shape[:2]

# ==============================
# Escalar SOMENTE pela largura
# ==============================
margin = 20
max_w = screen_width - margin

scale = min(max_w / orig_w, 1)

new_w = int(orig_w * scale)
new_h = int(orig_h * scale)

img_resized = cv2.resize(img_original, (new_w, new_h))

print(f"Imagem redimensionada: {new_w}x{new_h} (scale={scale:.3f})")

# ==============================
# Carregar texto
# ==============================
with open(txt_path, "r", encoding="utf-8") as f:
    text_lines = [linha.strip() for linha in f.readlines() if linha.strip()]

# ==============================
# Variáveis
# ==============================
rectangles = []
drawing = False
x_start, y_start = -1, -1
current_line_index = 0

offset_y = 0
viewport_height = screen_height - 120
scroll_speed = 60


def get_viewport():
    return img_resized[offset_y:offset_y + viewport_height, :]


def draw_rectangle(event, x, y, flags, param):
    global x_start, y_start, drawing
    global rectangles, current_line_index
    global offset_y, img_resized

    y_real = y + offset_y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_start, y_start = x, y_real

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        temp = img_resized.copy()
        cv2.rectangle(temp, (x_start, y_start), (x, y_real), (0, 255, 0), 2)
        cv2.imshow("Imagem", temp[offset_y:offset_y + viewport_height, :])

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        x1, y1 = min(x_start, x), min(y_start, y_real)
        x2, y2 = max(x_start, x), max(y_start, y_real)

        # Converter para tamanho original
        x1_orig = int(x1 / scale)
        y1_orig = int(y1 / scale)
        x2_orig = int(x2 / scale)
        y2_orig = int(y2 / scale)

        if current_line_index < len(text_lines):
            en_text = text_lines[current_line_index]
        else:
            en_text = ""

        rect = {
            "x1": x1_orig,
            "y1": y1_orig,
            "x2": x2_orig,
            "y2": y2_orig,
            "en": en_text,
            "ptbr": "",
            "ptbrpp": ""
        }

        rectangles.append(rect)
        current_line_index += 1

        cv2.rectangle(img_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)

        print("Retângulo salvo:", rect)


cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Imagem", new_w, viewport_height)
cv2.setMouseCallback("Imagem", draw_rectangle)

print("\nINSTRUÇÕES:")
print(" - Clique e arraste para selecionar")
print(" - ↑ = rolar para cima")
print(" - ↓ = rolar para baixo")
print(" - S = salvar JSON")
print(" - R = resetar")
print(" - ESC = sair\n")

while True:
    cv2.imshow("Imagem", get_viewport())

    key = cv2.waitKeyEx(20)

    if key == 27:  # ESC
        break

    # ======================
    # SETAS (Windows + Linux)
    # ======================
    elif key in [2490368, 65362]:  # ↑
        offset_y = max(offset_y - scroll_speed, 0)

    elif key in [2621440, 65364]:  # ↓
        offset_y = min(offset_y + scroll_speed, new_h - viewport_height)

    # ======================
    # TECLAS NORMAIS
    # ======================
    elif key == ord("r") or key == ord("R"):
        img_resized = cv2.resize(img_original, (new_w, new_h))
        rectangles.clear()
        current_line_index = 0
        offset_y = 0
        print("Resetado.")

    elif key == ord("s") or key == ord("S"):
        json_path = os.path.join(pasta, f"{pagina}mouse.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(rectangles, f, indent=4, ensure_ascii=False)
        print("JSON salvo em:", json_path)

cv2.destroyAllWindows()