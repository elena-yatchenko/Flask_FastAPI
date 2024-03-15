import multiprocessing
import os

MY_PATH = "."
MY_PATH = 'Lecture_3_SQLA, WTF'

def worker(file_):
    with open(file_, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"Слов в {file_} : {len(content.split())}")


def main(directory):
    multiprocess = []
    for root, dirs, files in os.walk(directory):
        if not dirs:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            process = multiprocessing.Process(target=worker, args=(file_path,))
            multiprocess.append(process)
            process.start()

        for process in multiprocess:
            process.join()
         


if __name__ == "__main__":
    main(MY_PATH)
