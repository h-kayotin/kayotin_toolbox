"""
kayotin_main - 主程序

Author: JiangHai江海
Date： 2023/5/11
"""

import image_tools
import ttkbootstrap as ttk
import os
import base64
from image_tools.icon import img


def main(root=None):
    if root:
        root_main = root
    else:
        root_main = ttk.Window(themename="journal")

    width = 15
    root_main.title("工具箱")

    # 创建临时图标文件
    tmp = open("tmp.ico", "wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root_main.iconbitmap("tmp.ico")
    os.remove("tmp.ico")

    root_main.resizable(False, False)

    # 新建画布
    canvas_main = ttk.Canvas(root_main, width=500, height=450, bg='white')
    canvas_main.pack()
    label1 = ttk.Label(root_main, text='工具箱')
    label1.config(font=('微软雅黑', 20))
    canvas_main.create_window(250, 100, window=label1)

    # 第一个功能：转换成ICO
    func1_button = ttk.Button(root_main, text="PNG转ICO",
                              command=lambda: image_tools.png_ico.ico_main(root_main, canvas_main),
                              width=width, style="danger outline")
    canvas_main.create_window(250, 150, window=func1_button)

    # 第二个功能：jpg转png
    func2_button = ttk.Button(root_main, text="JPG转PNG",
                              command=lambda: image_tools.jpg_png.init_interface(root_main, canvas_main),
                              width=width, style="info outline")
    canvas_main.create_window(250, 200, window=func2_button)

    # 第三个功能：查找文件
    func3_button = ttk.Button(root_main, text="查找文件",
                              command=lambda: image_tools.find_new.FileSearchEngine(root_main, canvas_main),
                              width=width, style="danger outline")
    canvas_main.create_window(250, 250, window=func3_button)

    # 第四个功能：分类文件
    func4_button = ttk.Button(root_main, text="文件分类",
                              command=lambda: image_tools.file_sort.FileSortTool(root_main, canvas_main),
                              width=width, style="info outline")
    canvas_main.create_window(250, 300, window=func4_button)

    # 第五个功能：查找重复文件
    func5_button = ttk.Button(root_main, text="查找重复文件",
                              command=lambda: image_tools.clean_up.FileCleanTool(root_main, canvas_main),
                              width=width, style="danger outline")
    canvas_main.create_window(250, 350, window=func5_button)

    root_main.mainloop()


if __name__ == '__main__':
    main()
