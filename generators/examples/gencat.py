# gencat.py
#
# Concatenate multiple generators into a single sequence

def gen_cat(sources):
    for src in sources:
        yield from src   # Pay attention to this yield from 
#or     for item in src:
#           yield item

# Example use

filepath = r"C:\Apps\davidyshuang\python3\generators\examples\www"
if __name__ == '__main__':
    from pathlib import Path
    from genopen import gen_open

    lognames = Path(filepath).rglob('access-log*')
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    for line in loglines:
        print(line,end='')
