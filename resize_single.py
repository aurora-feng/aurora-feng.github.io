import sys
from PIL import Image
from resizeimage import resizeimage
thub_size = (400, 289)
# thub_size = (200, 200)
reg_size = (600, 450)
path = './'


def main(file_name, rotate=None):
    origin_name = '{}.{}'.format(file_name.split('.')[0], file_name.split('.')[-1])
    thumbnail_name = '{}-thumbnail.{}'.format(file_name.split('.')[0], file_name.split('.')[-1])
    with open(path + file_name, 'rb') as f_rb:
        with Image.open(f_rb) as mario_image:
            new_image = mario_image.transpose(rotate) if rotate else mario_image
            new_image.save(path + origin_name, mario_image.format)
            thumb = resizeimage.resize_cover(new_image, thub_size, Image.ANTIALIAS)
            thumb.save(path + thumbnail_name, mario_image.format)


if __name__ == '__main__':
    print(sys.argv)
    file_name = sys.argv[1]
    d = {'90': Image.ROTATE_90, '180': Image.ROTATE_180, '270': Image.ROTATE_270}
    rotate = d.get(sys.argv[2]) if len(sys.argv) == 3 else None
    print(file_name, rotate)
    main(file_name, rotate)

