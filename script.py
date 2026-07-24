from PIL import Image
#################
# 写  在  前  面 #
# 使  用  方  法 #
#################
# 1.把图片文件替换上来，改名example.jpg/png，或者把下面这个路径更改成你复制上来的图片的名称
# 2.更换自己想用的风格，把前面的#去掉就可以直接替换
# 3.适当更改width 一般70效果就比较好，100以上会更清晰
# 4.在左侧栏找到unicode_art.txt 里面的内容即为字符画

# 输入图片
image_path = "example.png"
# 注意这里要换成图片对应的文件名

# 输出文本
output_path = "unicode_art.txt"
# 可以更改输出文件名

# 字符集：从暗到亮
# 可以自己替换，字符越多，细节越丰富

chars = " ⠁⠂⠄⡀⢀⣀⣤⣶⣿"
# chars = " .:-=+*#%@"
chars = "               .,:;i1tfLCG08@"
# 三种不同的像素画风格


# 输出宽度（字符数量）
# 越大越清晰，但txt越宽
width = 128
# 这里实测70是一个比较友好的值
# 当然也可以根据实际情况更改



def image_to_ascii(image_path, output_path, width):
    img = Image.open(image_path)

    # 转灰度
    img = img.convert("L")

    # 保持比例
    w, h = img.size
    ratio = h / w

    # 终端字符通常比高度宽，所以修正
    height = int(width * ratio * 0.45)

    img = img.resize((width, height))


    pixels = img.get_flattened_data()

    ascii_str = ""

    for pixel in pixels:
        # 灰度 0-255
        index = pixel * (len(chars) - 1) // 255

        # 因为图片越亮应该越空，所以反转
        ascii_str += chars[index]


    # 换行
    lines = [
        ascii_str[i:i + width]
        for i in range(0, len(ascii_str), width)
    ]


    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


    print("生成完成:", output_path)


image_to_ascii(
    image_path,
    output_path,
    width
)
