# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Allison Hai
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_in = float('nan') #input channel count
h_in = float('nan') #input height count 
w_in = float('nan') # input width count 
n_filt = float('nan') #number of filters in the covolution layer  
h_filt = float('nan') #filter height count
w_filt = float('nan') #filter width count 
s = float('nan') #stride of convolution filters 
p = float('nan') #amount of padding on each of the four input map slides 


# parse script arguments
if len(sys.argv)==9:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    n_filt = float(sys.argv[4])
    h_filt = float(sys.argv[5])
    w_filt = float(sys.argv[6])
    s = float(sys.argv[7])
    p = float(sys.argv[8])
else:
    print(\
        'Usage: '\
        'python3 c_in h_in w_in n_filt h_filt w_filt s p'\
    )
    exit()

# write script below this line
h_out = ((h_in + 2*p - h_filt)/(s))+1 
w_out = ((w_in +2*p -w_filt)/s)+1
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt 
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
c_out = n_filt 
divs = 0 #for a convolution layer 



print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed