#coding: utf-8

from PIL import Image, ImageDraw, ImageFont
from typing import Tuple
ImageFont.FreeTypeFont

class PILFont():
    def __init__(self, font_path: str, font_size: int) -> None:
        self.__font = ImageFont.FreeTypeFont(font_path, font_size)
    
    def render_text(self, text: str, offset: Tuple[int, int] = (0, 0)):
        ''' 绘制文本图片
            > text: 待绘制文本
            > offset: 偏移量
        '''
        __left, __top, right, bottom = self.__font.getbbox(text)
        img = Image.new("1", (right, bottom), color=255)
        img_draw = ImageDraw.Draw(img)
        img_draw.text(offset, text, fill=0, font=self.__font, spacing=0)
        return img

f = PILFont("guanzhi.ttf", 8)
# 渲染文本
im = f.render_text("兔兔伯爵, 出击! - 向敌人扔出一个兔兔伯爵玩偶, 并在10秒后爆炸, 对周围的敌人造成火焰伤害.")
im.save("hope.png")
# 渲染单个文字，可用于生成字体
# im = f.render_text("龙", (0, -1))
# im.show()
