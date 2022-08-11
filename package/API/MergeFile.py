import os
from PIL import Image  # 处理图片



def ToPDF(file_name):
    path = './temp/'
    name = file_name
    img_list = []  # 创建打开后的图片列表
    filename = os.listdir(path)
    filess = sorted(filename, key=lambda x: int(x[0:-4]))
    for files in filess:
        if files.endswith('png'):
            file = os.path.join(path, files)  # 遍历所有图片，带绝对路径
            img_open = Image.open(file)  # 打开所有图片
            if img_open.mode != 'RGB':
                img_open = img_open.convert('RGB')  # 转换图像模式
            img_list.append(img_open)  # 把打开的图片放入列表
            try:
                os.remove(file)  # 删除图片
            except:
                print(file)
    pdf_name = name + '.pdf'  # pdf文件名

    img_2 = img_list[0]
    img_open_list = img_list[1:]
    img_2.save(path + pdf_name, "PDF", resolution=100.0, save_all=True, append_images=img_open_list)
    print('pdf文件已经保存在' + path + '目录下！')
    pass
