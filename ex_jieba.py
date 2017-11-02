#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lamplight'
import os
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


content = ''
def read_content(content_path):
    '''
    read the text
    :param content_path:
    :return:
    '''
    # 初始化content
    content = ''



    #使用os模块的listdir 枚举文件夹下的所有文件

    for f in os.listdir(content_path):
        #拼接文件完整路径
        file_fullpath = os.path.join(content_path, f )

        #判断是否是文件
        if os.path.isfile(file_fullpath):
            print('loading {}'.format(file_fullpath))
            #将文件内容进行拼接
            content += open(file_fullpath, 'r').read()
            #每首歌词之间用换行符分隔
            content += '\n'
    print('done loading')
    return content


content = read_content('/home/lamplight/Desktop/b/')
#print('\n显示内容的前面部分...\n')
#print(content[:99])


# 这里使用jieba的textrank提取出1000个关键词及其比重
result = jieba.analyse.textrank(content, topK=1000, withWeight=True)
# 生成关键词比重字典
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)

#初始化关键字
image = Image.open('/home/lamplight/Desktop/timg.jpeg')
graph = np.array(image)

#生成云图， wordcloud 不支持中文 ，加载中文黑体
wc = WordCloud(font_path='/home/lamplight/Desktop/苹方黑体-极细-简.ttf', background_color='white', max_words=1000, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)

#显示图片
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off") #关闭图像坐标
plt.show()
