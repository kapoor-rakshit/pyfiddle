# Reference : https://pypi.org/project/colorama/

from colorama import init, Fore, Back, Style

init(autoreset=True)                                # (autoreset=True) - automate turn off color changes at the end of every print

print(Fore.RED + 'some red text')                                    # text color
print(Fore.GREEN + Back.GREEN + 'and with a green background')       # bgcolor and usage of multiple args
print(Style.DIM + 'and in dim text')                                 # style arg

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print(Style.RESET_ALL)                                               # resets foreground, background, and brightness. 
                                                                     # Colorama will perform this reset automatically on program exit
print("Hello world")