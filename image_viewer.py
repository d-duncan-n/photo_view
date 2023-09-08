import eel
import os

eel.init("web")

@eel.expose
def load_images():
    image_folder = "images"  # Папка с изображениями
    image_urls = []

    if os.path.exists(image_folder) and os.path.isdir(image_folder):
        for filename in os.listdir(image_folder):
            if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
                image_path = os.path.join(image_folder, filename)
                image_urls.append(image_path)

    return image_urls

eel.start("index.html", size=(800, 600))
