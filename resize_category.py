import os
import shutil
from PIL import Image
from resizeimage import resizeimage
thub_size = (400, 289)
reg_size = (600, 450)
_origin_path = '/Users/zhibin.jiang/Downloads/temp/{cate}/'
new_path = '/Users/zhibin.jiang/Learning/aurora_profolio/img/{cate}/'


def main():
    for cate in ['cate_flower', 'cate_life', 'cate_human', 'cate_view', 'cate_painting']:
        origin_path = _origin_path.format(cate=cate)
        if not os.path.exists(new_path.format(cate=cate)):
            os.mkdir(new_path.format(cate=cate))
        for image_name in os.listdir(origin_path):
            if not image_name.endswith('g'):
                continue
            image_path = origin_path + image_name
            print("Processing: ", image_path)
            with open(image_path, 'rb') as f_rb:
                with Image.open(f_rb) as image:
                    prefix, postfix = image_name.split('.')[0].strip('_'), image_name.split('.')[-1]
                    reg = new_path.format(cate=cate) + '{}.{}'.format(prefix, postfix)
                    shutil.copy(image_path, reg)
                    thum = new_path.format(cate=cate) + '{}-thumbnail.{}'.format(prefix, postfix)
                    thumb = resizeimage.resize_cover(image, thub_size)
                    thumb.save(thum, image.format)


if __name__ == '__main__':
    main()
