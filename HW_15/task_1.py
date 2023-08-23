# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
from collections import namedtuple
import logging


def file_data(path: str):
    path = path.split("\\")
    count = len(path)
    if count >= 3:
        *_, dir_1, dir_2, temp = path
    elif count == 2:
        dir_1 = "not indicated"
        dir_2, temp = path
    else:
        dir_1 = "not indicated"
        dir_2 = "not indicated"
        temp = path
    try:
        name, ext = str(temp).split(".")
    except ValueError:
        name = temp
        ext = "this is a directory"
    return name, ext, dir_2, dir_1


parser = argparse.ArgumentParser(description='Information about the file from its path')
parser.add_argument('path', type=str, help='Input file path')
args = parser.parse_args()

File = namedtuple('File', ['name', 'extension', 'directory', 'directory_parent'])
f1 = File(*file_data(args.path))

logging.basicConfig(filename="log.log", level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f1)