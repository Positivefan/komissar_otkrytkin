import PIL.ImageFont
from PIL import Image, ImageDraw, ImageFont
import textwrap

main_text = 'Всем большой привет, студент по какому-то предмету вообще не дотягивает до уровня, мда, я бы такого в универ не брал'

im = Image.open('cirno1.jpg')

#shortened_main_text
s_m_t = textwrap.wrap(main_text, width=29, drop_whitespace=True, tabsize=8, expand_tabs=True, max_lines=None)


font = ImageFont.truetype("arial.ttf", size=30, )
draw = ImageDraw.Draw(im)


margin = 163
offset = 580
for line in s_m_t:
    #print(line)
    draw.text((margin, offset), text=line, fill = ('#ffffff'), font = font)#, anchor='lt') #features='rtbd')
    offset += font.getsize(line)[1]


im.save('new_cirno.jpg')

print(im.width)
print(im.height)


im.show()
