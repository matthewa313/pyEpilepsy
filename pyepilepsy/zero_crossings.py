import numpy as np

def zero_crossings(sig, lengthArray):
  '''
  lengthArray = range(len(sig))
  This variable was added to minimize RAM space.
  '''
  numCrossings = 0
  for i in lengthArray:
    if (sig[i] > 0 and sig[i+1] <=0 ) or (sig[i] < 0 and sig[i+1] >=0 ):
      numCrossings += 1
  
  return numCrossings
