from PIL import ImageFont, Image, ImageDraw
import argparse
from fontTools.ttLib.ttFont import TTFont
import os

parse = argparse.ArgumentParser(description="将ttf字体文件转为图片")
parse.add_argument('-f', required=True,help="输入字体文件地址")
parse.add_argument('-o', help="输出目录,默认为当前目录下imgs", default="imgs")
parse.add_argument('-s', '--size', type=int, help="输出图片的像素大小", default=512)

args = parse.parse_args()
os.makedirs(args.o, exist_ok=True)


def uni_2_png(txt,name, font=args.f, img_size=512):
    img = Image.new('1', (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, int(img_size * 0.7))

    txt = chr(txt)
    x, y = draw.textsize(txt, font=font)
    draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
    # draw.text((0,0), txt, font=font, fill=0)
    file_name = '%s/%s.png' % (args.o, name)
    img.save(file_name)


if __name__ == '__main__':

    f = TTFont(args.f)
    print(args.f)
    # all_num = []
    # for i in f.getBestCmap():
    #
    #     all_num.append(i)
        # uni_2_png(i)
    # all_name = []
    all_item = [item for item in f["cmap"].tables]
    all_key_values = all_item[0].cmap
    for key,value in all_key_values.items():
        print(key,value)
        uni_2_png(key,value.strip("uni"))
        # for y in item.cmap.items():
        #     name = y[1].strip("uni")
        #     print(name)
            # all_name.append(name)

    # print(len(all_num),len(all_name))
