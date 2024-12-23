import cv2


class ImageUtils:

    @staticmethod
    def get_color_image(img):
        image = cv2.imread(img)[...,::-1]
        pixel = [int(image.shape[1] / 1.3), int(image.shape[0] / 1.3)]

        r, g, b = image[pixel[1], pixel[0]]
        return [int(r), int(g), int(b)]