import os
import cv2


def resize_images(path='images/', shape=(600, 800)):
    """Resizes images in a given directory

    Args:
        path (str, optional): the path to the directory with images. Defaults to 'images/'.
        shape (tuple, optional): the desired shape. Defaults to (600, 800).
    """
    (x, y) = shape

    for file in os.listdir(path):
        file_path = f'{path}{file}'
        img = cv2.imread(file_path)
        if img.shape != (y, x, 3):
            img = cv2.resize(img, (x, y), interpolation=cv2.INTER_AREA)
            cv2.imwrite(file_path, img)
            print(f'File {file} has been resized.')
    print('Finished.')


def rename_images(path='images/'):
    """Renames images in a directory to 1.jpg, 2.jpg etc.

    Args:
        path (str, optional): the path to the directory with images. Defaults to 'images/'.
    """
    for i, file in enumerate(os.listdir(path), start=1):
        filename_old = f'{path}{file}'
        filename_new = f'{path}{i}.jpg'
        os.rename(filename_old, filename_new)
        print(f'Renamed {file} to {i}.jpg')
    print('Finished')


if __name__ == '__main__':
    rename_images(path='images/easy/')
    resize_images(path='images/easy/', shape=(600, 800))