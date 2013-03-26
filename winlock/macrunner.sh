#!/bin/sh

# For testing only
# Need to make sure to run in 32 bit mode:

#see stackoverflow #3606964
export PYTHONPATH=.
#arch -i386 python tests/client.py 
arch -i386 python tests/server.py 
