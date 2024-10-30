from PIL import Image, ImageFilter
from PIL.ImageFile import ImageFile

img = Image.open('PT.jpg')  # Открытие изображение
print(img.size)  # Размер изображения
img = img.resize(size=(700, 600))  # Изменение размера изображения
img = img.rotate(-45)  # Поворот по часовой стрелке на 30 градусов
img: ImageFile = img.filter(ImageFilter.GaussianBlur(radius=4))  # Применение фильтра размытия картинки

img.show()
img.save('/Users/КВА/PycharmProjects/BVV/PT_new.png')
