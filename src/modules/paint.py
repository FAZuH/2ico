from colorama import Fore, Style, init

init()


class Print:
    @staticmethod
    def blue(string: str) -> None:
        print(Fore.LIGHTBLUE_EX + string + Style.RESET_ALL)

    @staticmethod
    def green(string: str) -> None:
        print(Fore.LIGHTGREEN_EX + string + Style.RESET_ALL)

    @staticmethod
    def red(string: str) -> None:
        print(Fore.LIGHTRED_EX + string + Style.RESET_ALL)

    @staticmethod
    def yellow(string: str) -> None:
        print(Fore.LIGHTYELLOW_EX + string + Style.RESET_ALL)
