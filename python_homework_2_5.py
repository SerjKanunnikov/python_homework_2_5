import sys
import subprocess
import os

# print((os.path.join(os.getcwd(), "Source")))


def convert():
    if os.path.exists(os.path.join(os.getcwd(), "Result")):
        print("Папка существует, конвертируем")
        pass
    else:
        subprocess.call(["mkdir", "Result"])
        if os.path.exists(os.path.join(os.getcwd(), "Result")):
            print("Создана папка Result, конвертируем")
    file_list = os.listdir(os.path.join(os.getcwd(), "Source"))
    for file in file_list:
        file_to_copy = (os.path.join(os.getcwd(), "Source", file))
        subprocess.call(["cp", file_to_copy, "Result"])
        print("Скопирован файл:", file)
    for file in os.listdir("Result"):
        file_to_convert = (os.path.join(os.getcwd(), "Result", file))
        subprocess.call(["magick", file_to_convert, "-resize", "200", file_to_convert])


convert()