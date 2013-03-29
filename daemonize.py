#encoding: utf-8

import os
import sys
import atexit

def daemonize(pidfile=None):
    if os.fork() > 0:
        sys.exit(0)
    os.chdir("/")
    os.setsid()
    os.umask(0)
    if os.fork() > 0:
        sys.exit(0)
    sys.stdout.flush()
    sys.stderr.flush()
    si = open("/dev/null", 'r')
    so = open("/dev/null", 'a+')
    se = open("/dev/null", 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    if pidfile:
        pid = str(os.getpid())
        with open(pidfile, 'w+') as fp:
            fp.write(pid+"\n")
        atexit.register(lambda: os.remove(pidfile))
