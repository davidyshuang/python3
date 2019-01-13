# redict.py
#
# Read a sequence of log lines and parse them into a sequence of dictionaries

filename = r"C:\Apps\davidyshuang\python3\generators\examples\access-log"
loglines = open(filename)

import re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

groups   = (logpat.match(line) for line in loglines)
tuples   = (g.groups() for g in groups if g)

colnames = ('host','referrer','user','datetime',
            'method', 'request','proto','status','bytes')

log      = (dict(zip(colnames, t)) for t in tuples)

if __name__ == '__main__':
    for x in log:
        print(x)
