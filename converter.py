import os
import colorama
from PIL import Image


class Main:
    def __init__(self):
        colorama.init()
        self.image_files: list[None | str] = []
        self.run()

    def run(self):
        self.get_image_paths()
        self.convert_to_ico()
        input()

    def get_image_paths(self):
        image_count: int = 0
        files = os.listdir()
        for file_name in files:
            if os.path.isfile(file_name) is False:
                continue

            _, file_extension = os.path.splitext(file_name)
            if file_extension not in {'.jpg', '.png'}:
                continue

            self.image_files.append(file_name)
            print(colorama.Fore.YELLOW + f'Found valid file "{file_name}".' + colorama.Style.RESET_ALL)
            image_count += 1

        print(colorama.Fore.YELLOW + f'Found {image_count} .jpg or .png files.' + colorama.Style.RESET_ALL)
    
    def convert_to_ico(self):
        print(colorama.Fore.YELLOW + f'Converting...' + colorama.Style.RESET_ALL)
        convert_count: int = 0
        error_count: int = 0
        for image_file in self.image_files:
            try:
                image = Image.open(image_file)
                if image.mode != 'RGBA':
                    image = image.convert('RGBA')

                image_name, _ = os.path.splitext(image_file)
                ico_name = f"{image_name}.ico"
                image.save(ico_name, format="ICO", sizes=[(32, 32)])
                convert_count += 1
                print(colorama.Fore.GREEN + f'Converted {image_file} into .ico' + colorama.Style.RESET_ALL)
            except Exception as e:
                error_count += 1
                print(colorama.Fore.RED + f'An error occurred: {str(e)}' + colorama.Style.RESET_ALL)

        print(
            colorama.Fore.GREEN + 
            f'Successfully converted {convert_count} images'
            f'{f" with {error_count} errors" if error_count > 0 else ""}.'
            + colorama.Style.RESET_ALL
        )
