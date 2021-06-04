#-*- coding: utf-8 -*-
import qrcode
from PIL import Image

def getQRcode(strs):
    qr=qrcode.QRCode(
        version=1,
        box_size=10,
        border=2,
        )
    # 添加数据
    qr.add_data(strs)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="pink", back_color="white")
    img = img.convert("RGBA")  # RGBA
    # 添加logo
    icon = Image.open("GRand.jpg").convert("RGBA")
    # 获取图片的宽高
    img_w, img_h = img.size
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    print(icon)
    w=int((img_w-icon_w)/2)
    h=int((img_h-icon_h)/2)
    img.paste(icon,(w,h),icon)
    img.show()
getQRcode("520格格,G with R forever!")