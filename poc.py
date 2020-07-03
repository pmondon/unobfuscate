import subprocess
import sys
from nm_output import *

def treat_nm_output(funs):
    tab = []
    for i in funs:
        if i:
            tmp = Nm_output(i)
            tab.append(tmp)
    return tab

function_names = open('./function_names', 'r').read().split('\n')[0:-1]
if len(sys.argv) < 2:
    print('please provide the path to the binary to analyse')
    sys.exit(0)


out = treat_nm_output(subprocess.Popen('nm ' + binary, shell=True, stdout=subprocess.PIPE).stdout.read().split('\n'))

print('these functions are possibly used to deobfuscate strings whithin the binary:')
for f in function_names:
    for o in out:
        if f in o.name:
            print '------------'
            print 'function name : ' + f
            print 'matched with this rule : ' + o.name
            print 'the adress of the function is : ' + str(o.address)
            print '------------'
