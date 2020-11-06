#! /usr/bin/env python3

import subprocess
import sys
import time


MIN_CYCLE_SECS = 6.0


def log(x):
  print('<[{}] {}>'.format(time.ctime(), x))


dest = sys.argv[1:]
log('Initiating rtunnel to {}'.format(dest))
args = 'ssh -R 22:localhost:22 -N'.split(' ')
args += [
  '-o', 'ExitOnForwardFailure yes',
  ] + dest


while True:
  start = time.time()
  print('>', args)
  p = subprocess.run(args)
  diff = time.time() - start
  log('Exited after {:.3f}s'.format(diff))
  if diff < MIN_CYCLE_SECS:
    time.sleep(MIN_CYCLE_SECS - diff)
  log('Restarting')
