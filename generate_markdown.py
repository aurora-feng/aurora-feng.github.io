# https://blog.webjeda.com/jekyll-filters/#simple-jekyll-filters
import os

template = """
---
title: {title}
layout: default
modal-id: {order}
date: 2019-06-28
img: {image}
thumbnail: {thumbnail}
alt: image-alt
category: {category}
description: {description}

---
"""
image_path = '/Users/zhibin.jiang/Learning/aurora_profolio/img/{cate}/'
markdown_path = '/Users/zhibin.jiang/Learning/aurora_profolio/_posts/'
name = '2019-06-28-project-{id}.markdown'


def main():
    counter = 1
    for cate in ['cate_flower', 'cate_life', 'cate_human', 'cate_view', 'cate_painting']:
        print(cate)
        cate_path = image_path.format(cate=cate)
        for file in os.listdir(image_path.format(cate=cate)):
            if 'thumbnail' in file:
                continue
            print(file)
            raw_file = file
            thumb_file = "{}-thumbnail.{}".format(raw_file.split('.')[0], raw_file.split('.')[-1])
            if os.path.exists(cate_path + raw_file) and os.path.exists(cate_path + thumb_file):
                content = template.format(title=file, order=counter, image=raw_file, thumbnail=thumb_file, category=cate, description='.')
                md_file = name.format(id=counter)
                counter += 1
                with open(markdown_path + md_file, 'w') as fw:
                    fw.write(content)
            else:
                print("不存在的图片: ", cate_path, file)


if __name__ == '__main__':
    main()
