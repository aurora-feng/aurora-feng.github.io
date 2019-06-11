from PIL import Image
from resizeimage import resizeimage
thub_size = (400, 289)
reg_size = (600, 450)
with open('./img/portfolio/mario.jpeg', 'rb') as f_rb:
    with Image.open(f_rb) as mario_image:
        new_image = mario_image.transpose(Image.ROTATE_270)
        mario_thub = resizeimage.resize_cover(new_image, thub_size)
        mario_thub.save('mario-thumbnail.jpeg', mario_image.format)
        mario_reg = resizeimage.resize_cover(new_image, reg_size)
        mario_reg.save('mario-reg.jpeg', mario_image.format)

