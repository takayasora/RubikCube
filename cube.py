import csv
import time
import playsound
import random
import romajitable

class Color:
    WHITE  = "\033[48;2;247;247;247m　\033[0m"
    YELLOW = "\033[48;2;253;254;0m　\033[0m"
    BLUE   = "\033[48;2;41;94;224m　\033[0m"
    GREEN  = "\033[48;2;36;244;13m　\033[0m"
    RED    = "\033[48;2;243;16;14m　\033[0m"
    ORANGE = "\033[48;2;243;156;14m　\033[0m"
        
def corner_exam(qestion_num):
    # 開始時刻を記録
    start_time = time.time()
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

    def print_color_corner(color_codeA,color_codeB,color_codeC):
        print(color_codeA, end="")
        print(color_codeB, end="")
        print(color_codeC, end="")
        
    def roma_to_hiragana(roma_string):
        try:
            result = romajitable.to_kana(roma_string)
            hiraganed = result.hiragana
            return hiraganed
        except:
            return roma_string
    
    def playmp3_ok():
        playsound.playsound("./resource/Quiz-Correct.mp3")
    
    def addcsv_corner(text):
        csv_file_path = "score_corner.csv"
        # CSVファイルを開いてデータを追加
        with open(csv_file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([text])  # データをリストに包む

    flag=0
    for i in range(qestion_num):
        rand_num = random.randint(1, 24)
        name, colorA, colorB, colorC = color_index_corner[rand_num]
        print_color_corner(colorA, colorB, colorC)
        ans = roma_to_hiragana(input())    
        if ans == name:
            print("OK", name)
            flag=flag+1
            #playmp3_ok()
        else:
            print("NG", name)
    if flag==qestion_num:
        #全問正解の時にここに来る。
        end_time = time.time()
        execution_time = end_time - start_time
        ave = execution_time / int(qestion_num)
        addcsv_corner(ave)
        print("Ans/Sec",ave)
    else:
        print("ミスがありました。")


def edge_exam(qestion_num):
    start_time = time.time()
    def print_color_edge(color_codeA,color_codeB):
        print(color_codeA, end="")
        print(color_codeB, end="")
    
    color_index_edge = {
        1 : ["あ", Color.WHITE, Color.BLUE],
        2 : ["い", Color.YELLOW, Color.BLUE],
        3 : ["う", Color.YELLOW, Color.GREEN],
        4 : ["え", Color.WHITE, Color.GREEN],
        5 : ["か", Color.WHITE, Color.ORANGE],
        6 : ["き", Color.BLUE, Color.ORANGE],
        7 : ["く", Color.YELLOW, Color.ORANGE],
        8 : ["け", Color.GREEN, Color.ORANGE],
        9 : ["さ", Color.WHITE, Color.RED],
        10 : ["し", Color.BLUE, Color.RED],
        11 : ["す", Color.YELLOW, Color.RED],
        12 : ["せ", Color.GREEN, Color.RED],
        13 : ["た", Color.BLUE, Color.WHITE],
        14 : ["ち", Color.BLUE, Color.YELLOW],
        15 : ["つ", Color.GREEN, Color.YELLOW],
        16 : ["て", Color.GREEN, Color.WHITE],
        17 : ["な", Color.ORANGE, Color.WHITE],
        18 : ["に", Color.ORANGE, Color.BLUE],
        19 : ["ぬ", Color.ORANGE, Color.YELLOW],
        20 : ["ね", Color.ORANGE, Color.GREEN],
        21 : ["ら", Color.RED, Color.WHITE],
        22 : ["り", Color.RED, Color.BLUE],
        23 : ["る", Color.RED, Color.YELLOW],
        24 : ["れ", Color.RED, Color.GREEN]
    }
    
    def roma_to_hiragana(roma_string):
        try:
            result = romajitable.to_kana(roma_string)
            hiraganed = result.hiragana
            return hiraganed
        except:
            return roma_string
    
    def playmp3_ok():
        playsound.playsound("./resource/Quiz-Correct.mp3")
    
    def addcsv_edge(text):
        csv_file_path = "score_edge.csv"
        # CSVファイルを開いてデータを追加
        with open(csv_file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([text])  # データをリストに包む
          
    flag=0
    for i in range(qestion_num):
        rand_num = random.randint(1, 24)
        name, colorA, colorB = color_index_edge[rand_num]
        print_color_edge(colorA, colorB)
        ans = roma_to_hiragana(input())    
        if ans == name:
            print("OK", name)
            flag=flag+1
            #playmp3_ok()
        else:
            print("NG", name)
    if flag==qestion_num:
        #全問正解の時にここに来る。
        end_time = time.time()
        execution_time = end_time - start_time
        ave = execution_time / int(qestion_num)
        addcsv_edge(ave)
        print("Ans/Sec",ave)
    else:
        print("ミスがありました。")

def score_view():
    import csv
    import matplotlib.pyplot as plt

    # CSVファイル名
    filename_edge = "score_edge.csv"
    filename_corner = "score_corner.csv"

    # score_edge.csvからデータを読み込む
    with open(filename_edge, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data_edge = [float(row[0]) for row in reader]

    # score_corner.csvからデータを読み込む
    with open(filename_corner, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data_corner = [float(row[0]) for row in reader]

    # データのインデックスを作成（X軸のラベルとして使用）
    indexes_edge = range(1, len(data_edge) + 1)
    indexes_corner = range(1, len(data_corner) + 1)

    # 図のサイズを設定 (幅, 高さ)
    plt.figure(figsize=(10, 8))  # 変更点: 図のサイズを指定

    # サブプロットを設定（2行1列の1番目）
    plt.subplot(2, 1, 1)
    plt.plot(indexes_edge, data_edge, marker='o', color='blue')
    plt.title('Edge Scores')
    plt.xlabel('Index')
    plt.ylabel('Score')
    plt.grid(True)

    # サブプロットを設定（2行1列の2番目）
    plt.subplot(2, 1, 2)
    plt.plot(indexes_corner, data_corner, marker='x', color='red')
    plt.title('Corner Scores')
    plt.xlabel('Index')
    plt.ylabel('Score')
    plt.grid(True)

    # サブプロット間の余白を調整
    plt.tight_layout()

    # グラフを表示
    plt.show()
