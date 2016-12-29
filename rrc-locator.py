#!/usr/bin/env python3

import sys, os

DEBUG = False

fpath = os.path.realpath(sys.argv[1])
cdir = os.path.dirname(fpath)
hdir = os.path.expanduser("~")

if hdir.starswith('/u/'): # this is UTCS
  sys.exit()

rcfiles = []

while True:
  rcfile = os.path.join(cdir, ".vimrc")
  if DEBUG: 
    print("rcfile: ",rcfile)
    print("cdir: ",cdir)
    print("hdir: ",hdir)
    print("fpath: ",fpath)
    print("----------------")
  if cdir == hdir or os.path.dirname(cdir) == cdir: break
  cdir = os.path.dirname(cdir)
  if rcfile == fpath: continue
  if os.path.exists(rcfile):
    rcfiles.append(rcfile)

if DEBUG:
  print("FINAL RC FILES:")
  for rcfile in rcfiles:
    print(rcfile)

rcfiles = rcfiles[::-1]
if not DEBUG:
  print(";".join(rcfiles),end="")
