# genfind.py
#
# A function that generates files that match a given filename pattern

from pathlib import Path

def gen_find(filepat, top):
    yield from Path(top).rglob(filepat)

# Example use

filepath = r"C:\Apps\davidyshuang\python3\generators\examples\www"
if __name__ == '__main__':
    lognames = gen_find("access-log*",filepath)
    for name in lognames:
        print(name)
