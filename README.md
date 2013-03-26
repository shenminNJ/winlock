winlock
=======

utility for locking a windows desktop

Testing
-------
I have been doing development with the following setup:

Dev Machine: Linux box with source code checked out.  Guardfile that pushes code to windows box and triggers test run.

Windows Machine: Windows box that is running rsync server through cygwin 
* Source code location: c:\Development\projects\winlock
* Rsync Server Command: rsync -v --config=rsyncd.conf --daemon --no-detach
* Running the go.bat file (a simple loop that waits for an nc connection, then runs tests)
* rsyncd.conf file: 

    use chroot = no
    strict modes = no
    max connections = 1
    hosts allow *

    [projects]
    list = no
    lock file = rsyncd.lockfile
    log file = rsyncd.log
    read only = no 
    path = /cygdrive/c/Development/projects

