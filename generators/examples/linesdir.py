# linesdir.py
#
# Generate a sequence of lines from files in a directory

from pathlib import Path
import gencat
import genopen 

def lines_from_dir(filepat, dirname):
    names = Path(dirname).rglob(filepat)
    files = genopen.gen_open(names)
    lines = gencat.gen_cat(files)
    return lines

# Example use

if __name__ == '__main__':
    filepath = r"C:\Apps\davidyshuang\python3\generators\examples\www"
    loglines = lines_from_dir("access-log*",filepath)
    for line in loglines:
        print(line, end='')
