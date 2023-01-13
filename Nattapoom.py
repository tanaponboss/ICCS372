import sys
import numpy as np

def file_read(file):

    rfile = file.read()

    return rfile

if len(sys.argv) == 1:

    file_read(sys.stdin)

else:

    file = file_read(open(sys.argv[1], 'r'))
    
    nums = np.array(list(map(int, file.splitlines())))

    print(f'Statistics Summary\nmean: {np.mean(nums)}\nstd: {np.std(nums)}\nmin: {np.min(nums)}\nmax: {np.max(nums)}')