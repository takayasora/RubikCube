class Color:
    WHITE  = "\033[48;2;247;247;247m　\033[0m"
    YELLOW = "\033[48;2;253;254;0m　\033[0m"
    BLUE   = "\033[48;2;41;94;224m　\033[0m"
    GREEN  = "\033[48;2;36;244;13m　\033[0m"
    RED    = "\033[48;2;243;16;14m　\033[0m"
    ORANGE = "\033[48;2;243;156;14m　\033[0m"

def print_color_corner(color_codeA,color_codeB,color_codeC):
    print(color_codeA, end="")
    print(color_codeB, end="")
    print(color_codeC, end="")

color_index_corner = {
    1 : ["あ", Color.WHITE, Color.BLUE, Color.ORANGE],
    2 : ["い", Color.YELLOW, Color.ORANGE, Color.BLUE],
    3 : ["う", Color.YELLOW, Color.GREEN, Color.ORANGE],
    4 : ["え", Color.WHITE, Color.ORANGE, Color.GREEN],
    5 : ["か", Color.BLUE, Color.ORANGE, Color.WHITE],
    6 : ["き", Color.BLUE, Color.YELLOW, Color.ORANGE],
    7 : ["く", Color.GREEN, Color.ORANGE, Color.YELLOW],
    8 : ["け", Color.GREEN, Color.WHITE, Color.ORANGE],
    9 : ["さ", Color.BLUE, Color.WHITE, Color.RED],
    10 : ["し", Color.BLUE, Color.RED, Color.YELLOW],
    11 : ["す", Color.GREEN, Color.YELLOW, Color.RED],
    12 : ["せ", Color.GREEN, Color.RED, Color.WHITE],
    13 : ["た", Color.WHITE, Color.RED, Color.BLUE],
    14 : ["ち", Color.YELLOW, Color.BLUE, Color.RED],
    15 : ["つ", Color.YELLOW, Color.RED, Color.GREEN],
    16 : ["て", Color.WHITE, Color.GREEN, Color.RED],
    17 : ["な", Color.ORANGE, Color.WHITE, Color.BLUE],
    18 : ["に", Color.ORANGE, Color.BLUE, Color.YELLOW],
    19 : ["ぬ", Color.ORANGE, Color.YELLOW, Color.GREEN],
    20 : ["ね", Color.ORANGE, Color.GREEN, Color.WHITE],
    21 : ["ら", Color.RED, Color.BLUE, Color.WHITE],
    22 : ["り", Color.RED, Color.YELLOW, Color.BLUE],
    23 : ["る", Color.RED, Color.GREEN, Color.YELLOW],
    24 : ["れ", Color.RED, Color.WHITE, Color.GREEN]
}

import random

import romkan

def roma_to_hiragana(roma_string):
    try:
        hiragana_string = romkan.to_hiragana(roma_string)
        return hiragana_string
    except:
        return roma_string
    
for i in range(1, 10):
    rand_num = random.randint(1, 24)
    name, colorA, colorB, colorC = color_index_corner[rand_num]
    print_color_corner(colorA, colorB, colorC)
    roma_input = input()
    hiragana_output = roma_to_hiragana(roma_input)
    if hiragana_output == name:
        print("OK")
    else:
        print("NG", name)