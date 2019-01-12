# genlog.py
#
# Sum up the bytes transferred in an Apache server log using
# generator expressions

filename = r"C:\Apps\davidyshuang\python3\generators\examples\access-log"
with open(filename) as wwwlog:
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
    bytes_sent = (int(x) for x in bytecolumn if x != '-')
    print("Total", sum(bytes_sent))
