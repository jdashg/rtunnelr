#! /usr/bin/env python3

import subprocess
import sys
import time


MIN_CYCLE_SECS = 60.0


def log(x):
  print('<[{}] {}>'.format(time.ctime(), x))


dest = sys.argv[1]
log('Initiating rtunnel to {}'.format(dest))
args = 'ssh -R 22:localhost:22 -p 22000 {} -v -N'.format(dest)
args = args.split(' ')


while True:
  start = time.time()
  p = subprocess.run(args)
  diff = time.time() - start
  log('Exited after {}s'.format(diff))
  if diff < MIN_CYCLE_SECS:
    time.sleep(MIN_CYCLE_SECS - diff)
  log('Restarting')
  
