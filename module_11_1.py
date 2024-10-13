from PIL import Image
from PIL import ImageDraw, ImageFont
from random import randint
url = None
while url != '0':
    url = input('Дайте мне адрес картинки на вашем ПК и я с ней поколдую) \n')
    image_for_magic = Image.open(url)
    match randint(1, 5):
        case 1:
            print('Вам выпало 1')
            print('Я его чуть-чуть помял')
            w_h = image_for_magic.size
            image_for_magic = image_for_magic.resize((randint(50, w_h[0]), randint(50, w_h[1])))
        case 2:
            print('Вам выпало 2')
            print('Я его чуть-чуть порезал')
            w_h = image_for_magic.size
            box = (10, 10, min(w_h[0], 100), min(w_h[1], 100))
            image_for_magic = image_for_magic.crop(box)
        case 3:
            print('Вам выпало 3')
            print('Я его чуть-чуть повернул')
            image_for_magic = image_for_magic.rotate(randint(1, 359))
        case 4:
            print('Вам выпало 4')
            print('"Всмысле мы не в нуарном фильме?"')
            image_for_magic = image_for_magic.convert('L')
        case 5:
            print('Вам выпало 5')
            print('Радуйся, не всем я роспись ставлю')
            w_h = image_for_magic.size
            draw = ImageDraw.Draw(image_for_magic)
            font = ImageFont.truetype('arial.ttf', size=20)
            draw.text((randint(1, w_h[0]), randint(1, w_h[1])), 'i was here', fill='white', font=font)
    image_for_magic.save(url)



