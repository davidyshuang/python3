# nongenlog.py
#
# Sum up the number of bytes transferred in an Apache log file
# using a simple for-loop.   We're not using generators here.

filename = r"C:\Apps\davidyshuang\python3\generators\examples\access-log"
with open(filename) as wwwlog:
    total = 0
    for line in wwwlog:
        bytes_sent = line.rsplit(None,1)[1]
        if bytes_sent != '-':
            total += int(bytes_sent)
    print("Total", total)
