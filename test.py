from PIL import Image

def resize_gif(input_path, output_path, new_size):
    # Открываем GIF
    with Image.open(input_path) as img:
        # Получаем список кадров
        frames = []
        for frame in range(img.n_frames):
            img.seek(frame)
            # Изменяем размер каждого кадра
            resized_frame = img.resize(new_size, Image.LANCZOS)
            frames.append(resized_frame)

        # Сохраняем измененные кадры в новый GIF
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)

# Пример использования функции
input_gif = 'images/screemer.gif'  # Замените на путь к вашему GIF
output_gif = 'images/screem.gif'  # Замените на путь для сохранения
new_size = (1200, 800)  # Новый размер (ширина, высота)

resize_gif(input_gif, output_gif, new_size)

print("GIF успешно изменен!")
