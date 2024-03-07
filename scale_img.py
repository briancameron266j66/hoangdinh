from os.path import join,dirname, isfile
from os import listdir
from PIL import Image

SIZE = (180,180)
IMAGE_FOLDER = 'C:\\Users\\Four\\Desktop\\New folder'
SAVE_FOLDER = 'C:\\Users\\Four\\Desktop\\New folder (2)'

if __name__ == "__main__":
      onlyfiles = [f for f in listdir(IMAGE_FOLDER) if isfile(join(IMAGE_FOLDER, f))]
      for file in onlyfiles:
            img = Image.open(f'{IMAGE_FOLDER}\\{file}')
            img.resize(size=SIZE).save(f'{SAVE_FOLDER}\\{file}')
            print(f'{file} | Done')