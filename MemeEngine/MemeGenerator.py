from PIL import Image, ImageDraw, ImageFont
import random


class Meme():

    def __init__(self, output_dir  ='./_data/photos/dog'):
        self.output_dir = output_dir


    def make_meme(self, img_path, text, author, width=500) -> str:
        pic = Image.open(img_path, mode='r', formats=None)

        if width > 500:
            width = 500
        ratio = width/float(pic.size[0])
        height = int(ratio*float(pic.size[1]))
        pic = pic.resize((width, height), Image.NEAREST)

        message = f' {text} -- {author}'
        draw = ImageDraw.Draw(pic)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((random.randint(1, height), random.randint(1, width-len(message))), message, font=font, fill='white')

        out_path = img_path.split('.')[-2] + '_meme.' + img_path.split('.')[-1]
        pic.save(out_path)
        return out_path
