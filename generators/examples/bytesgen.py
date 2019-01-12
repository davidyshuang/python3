# bytesgen.py
#
# An example of chaining together different generators into a processing
# pipeline.    

import genfind
import genopen
import gencat
import gengrep

pat    = r'ply-.*\.gz'
logdir = r"C:\Apps\davidyshuang\python3\generators\examples\www"

filenames = genfind.gen_find("access-log*",logdir)
logfiles  = genopen.gen_open(filenames)
loglines  = gencat.gen_cat(logfiles)
patlines  = gengrep.gen_grep(pat,loglines)
bytecol   = (line.rsplit(None,1)[1] for line in patlines)
bytes_sent= (int(x) for x in bytecol if x != '-')

print("Total", sum(bytes_sent))

