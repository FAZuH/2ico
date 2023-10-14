import os
from PIL import Image
import shutil
from typing import List

from modules.paint import Print
from settings import INPUT_IMAGE_DIR, OUTPUT_ICO_DIR, OUTPUT_IMAGE_DIR


class Converter:
    def __init__(self) -> None:
        self.image_paths: List[str] = []
        self.converted_image_paths: List[str] = []

    def run(self) -> None:
        self.get_image_paths()
        self.convert_to_ico()
        self.move_old_image()

    def get_image_paths(self) -> None:
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

            Print.yellow( f'Found valid file "{file_path}".')
            image_count += 1

        Print.yellow(f'Found {image_count} .jpg or .png files.')

    def convert_to_ico(self) -> None:
        Print.yellow('Converting...')

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
                Print.green(f'Converted {image_path} into .ico')

            except Exception as e:
                error_count += 1
                Print.red(f'An error occurred: {str(e)}')

        Print.green(f'Successfully converted {convert_count} images {f" with {error_count} errors" if error_count > 0 else ""}.')

    def move_old_image(self) -> None:
        try:
            for image_file in self.converted_image_paths:
                image_path = INPUT_IMAGE_DIR / image_file
                shutil.move(image_path, OUTPUT_IMAGE_DIR)

        except Exception as e:
            Print.red(f'An error occured: {e}')
