"""The MemeEngine generates a meme."""

from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine():
    """The MemeEngine has three main purposes.

    Loading an image, transforming the image,
    adding a caption to the image
    """

    def __init__(self, output_dir):
        """Create a new meme.

        :param output_dir: path to created / saved meme
        """
        self.output_dir = output_dir

        # create a folder for generated memes
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme by loading + transforming an image and add a caption.

        :param img_path: Path to image
        :param text: Text for meme
        :param author: Author of text
        :param width: target width of picture
        """
        pic = Image.open(img_path, mode='r', formats=None)

        # max-wigth sould be 500
        if width > 500:
            width = 500
        ratio = width/float(pic.size[0])
        height = int(ratio*float(pic.size[1]))
        pic = pic.resize((width, height), Image.NEAREST)
        pic_width = pic.size[0]

        message = f' "{text}" - {author}'
        draw = ImageDraw.Draw(pic)
        font = ImageFont.truetype('./MemeEngine/fonts/LilitaOne-Regular.ttf',
                                  size=20)
        font_width = font.getsize(message)[0]

        # calculate text position which fits into the size of the pic
        # assumption: text_width < pic_width
        # hard coded offsets for not drawing on the edge
        text_pos_x_min = 0
        text_pos_x_max = pic_width - (font_width + 10)
        text_pos_y_min = font.getsize(message)[1]
        text_pos_y_max = pic.size[1] - font.getsize(message)[1]
        text_pos_x, text_pos_y = [random.randint(text_pos_x_min,
                                                 text_pos_x_max),
                                  random.randint(text_pos_y_min,
                                                 text_pos_y_max)]

        draw.text((text_pos_x, text_pos_y), message, font=font, fill='white')

        if '/' in img_path:
            outpic_name = img_path.split('.')[-2].split('/')[-1] + '_meme.'
        else:
            outpic_name = img_path.split('.')[-2].split('\\')[-1] + '_meme.'

        out_path = self.output_dir+'/'+outpic_name+img_path.split('.')[-1]
        pic.save(out_path)
        return out_path
