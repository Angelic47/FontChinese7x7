#coding: utf-8

import ctypes
import struct
import win32con
import win32gui
import win32ui

from PIL import Image


def RGB(r, g, b):    
    return r | (g << 8) | (b << 16)

def native_bmp_to_pil(hdc, bitmap_handle, width, height):
    bmpheader = struct.pack("LHHHH", struct.calcsize("LHHHH"),
                            width, height, 1, 24) #w,h, planes=1, bitcount)
    c_bmpheader = ctypes.c_buffer(bmpheader)

    #3 bytes per pixel, pad lines to 4 bytes    
    c_bits = ctypes.c_buffer(" " * (height * ((width*3 + 3) & -4)))

    res = ctypes.windll.gdi32.GetDIBits(
        hdc, bitmap_handle, 0, height,
        c_bits, c_bmpheader,
        win32con.DIB_RGB_COLORS)
    if not res:
        raise IOError("native_bmp_to_pil failed: GetDIBits")

    im = Image.frombuffer(
        "RGB", (width, height), c_bits,
        "raw", "BGR", (width*3 + 3) & -4, -1)
    return im    


class Win32Font:
    def __init__(self, name, height, weight=win32con.FW_NORMAL,
                 italic=False, underline=False):
        self.font = win32ui.CreateFont({
            'name': name, 'height': height,
            'weight': weight, 'italic': italic, 'underline': underline})

        #create a compatible DC we can use to draw:
        self.desktopHwnd = win32gui.GetDesktopWindow()
        self.desktopDC = win32gui.GetWindowDC(self.desktopHwnd)
        self.mfcDC = win32ui.CreateDCFromHandle(self.desktopDC)         
        self.drawDC = self.mfcDC.CreateCompatibleDC()

        #initialize it
        self.drawDC.SelectObject(self.font)

    def renderText(self, text):
        text = text.encode('gb2312')
        """render text to a PIL image using the windows API."""
        self.drawDC.SetTextColor(RGB(0,0,0))

        #create the compatible bitmap:
        w,h = self.drawDC.GetTextExtent(text)
        
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(self.mfcDC, w, h)        
        self.drawDC.SelectObject(saveBitMap)

        #draw it
        self.drawDC.DrawText(text, (0, 0, w, h), win32con.DT_LEFT)

        #convert to PIL image
        im = native_bmp_to_pil(self.drawDC.GetSafeHdc(), saveBitMap.GetHandle(), w, h)

        #clean-up
        win32gui.DeleteObject(saveBitMap.GetHandle())

        return im        

    def __del__(self):
        self.mfcDC.DeleteDC()
        self.drawDC.DeleteDC()
        win32gui.ReleaseDC(self.desktopHwnd, self.desktopDC)
        win32gui.DeleteObject(self.font.GetSafeHandle())

    def __del__(self):
        win32gui.DeleteObject(self.font.GetSafeHandle())

f = Win32Font("JiZhi", 8)
im = f.renderText("兔兔伯爵, 出击! - 向敌人扔出一个兔兔伯爵玩偶, 并在10秒后爆炸, 对周围的敌人造成火焰伤害.".decode("utf-8"))
im.save("hope.png")
