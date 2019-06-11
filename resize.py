import sys
from PIL import Image
from resizeimage import resizeimage
thub_size = (400, 289)
reg_size = (600, 450)
path = './img/portfolio/'


def main(file_name, rotate):
    thumbnail_name = '{}-thumbnail.{}'.format(*file_name.split('.'))
    reg_name = '{}-reg.{}'.format(*file_name.split('.'))
    with open(path + file_name, 'rb') as f_rb:
        with Image.open(f_rb) as mario_image:
            if rotate:
                new_image = mario_image.transpose(rotate)
                # new_image.save(path + file_name, mario_image.format)
            else:
                new_image = mario_image
            mario_thub = resizeimage.resize_cover(new_image, thub_size)
            mario_thub.save(path + thumbnail_name, mario_image.format)
            mario_reg = resizeimage.resize_cover(new_image, reg_size)
            mario_reg.save(path + reg_name, mario_image.format)


if __name__ == '__main__':
    print(sys.argv)
    file_name = sys.argv[1]
    d = {'90': Image.ROTATE_90, '180': Image.ROTATE_180, '270': Image.ROTATE_270}
    rotate = d.get(sys.argv[2]) if len(sys.argv) == 3 else None
    print(file_name, rotate)
    main(file_name, rotate)

