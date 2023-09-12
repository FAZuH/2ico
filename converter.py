import os
import colorama
import pathlib
import shutil
from PIL import Image

BASE_DIR = pathlib.Path(__file__).parent
INPUT_IMAGE_DIR = BASE_DIR / 'input_image'
OUTPUT_ICO_DIR = BASE_DIR / 'output_ico'
OUTPUT_IMAGE_DIR = BASE_DIR / 'output_image'


class Main:
    def __init__(self):
        colorama.init()
        self.image_paths: list[None | str] = []
        self.converted_image_paths : list[None | str] = []
        self.run()

    def run(self):
        self.get_image_paths()
        self.convert_to_ico()
        self.move_old_image()
        input()

    def get_image_paths(self):
        image_count: int = 0
        files = os.listdir(INPUT_IMAGE_DIR)
        for file_name in files:
            file_path = INPUT_IMAGE_DIR / file_name
            if os.path.isfile(file_path) is False:
                continue

            _, file_extension = os.path.splitext(file_path)
            if file_extension not in {'.jpg', '.png'}:
                continue

            self.image_paths.append(file_path)
            print(colorama.Fore.YELLOW + f'Found valid file "{file_path}".' + colorama.Style.RESET_ALL)
            image_count += 1

        print(colorama.Fore.YELLOW + f'Found {image_count} .jpg or .png files.' + colorama.Style.RESET_ALL)
    
    def convert_to_ico(self):
        print(colorama.Fore.YELLOW + f'Converting...' + colorama.Style.RESET_ALL)
        convert_count: int = 0
        error_count: int = 0
        for image_path in self.image_paths:
            try:
                image = Image.open(image_path)
                if image.mode != 'RGBA':
                    image = image.convert('RGBA')

                image_name = os.path.splitext(os.path.basename(image_path))[0]
                ico_path = OUTPUT_ICO_DIR / f"{image_name}.ico"
                image.save(ico_path, format='ICO', sizes=[(32, 32)])
                convert_count += 1
                self.converted_image_paths.append(image_path)
                print(colorama.Fore.GREEN + f'Converted {image_path} into .ico' + colorama.Style.RESET_ALL)
            except Exception as e:
                error_count += 1
                print(colorama.Fore.RED + f'An error occurred: {str(e)}' + colorama.Style.RESET_ALL)

        print(
            colorama.Fore.GREEN + 
            f'Successfully converted {convert_count} images'
            f'{f" with {error_count} errors" if error_count > 0 else ""}.'
            + colorama.Style.RESET_ALL
        )

    def move_old_image(self):
        try:
            for image_file in self.converted_image_paths:
                image_path = INPUT_IMAGE_DIR / image_file
                shutil.move(image_path, OUTPUT_IMAGE_DIR)
        except Exception as e:
            print(colorama.Fore.RED + f'An error occured: {e}' + colorama.Style.RESET_ALL)
