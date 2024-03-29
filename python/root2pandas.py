#!/usr/bin/env python

import numpy as np
from numpy.lib.recfunctions import stack_arrays
from root_numpy import root2array, root2rec
import glob
import pandas as pd

def root2pandas(files_path, tree_name, **kwargs):
  '''
  Args:
  -----
  files_path: a string like './data/*.root', for example
  tree_name: a string like 'Collection_Tree' corresponding to the name of the folder inside the root 
             file that we want to open
  kwargs: arguments taken by root2array, such as branches to consider, start, stop, step, etc
  Returns:
  --------    
  output_panda: a pandas dataframe like allbkg_df in which all the info from the root file will be stored
  Note:
  -----
  if you are working with .root files that contain different branches, you might have to mask your data
  in that case, return pd.DataFrame(ss.data)
  '''
  # -- create list of .root files to process
  files = glob.glob(files_path)

  # -- process ntuples into rec arrays
  ss = stack_arrays([root2rec(fpath, tree_name, **kwargs) for fpath in files])

  try:
    return pd.DataFrame(ss)
  except Exception:
    return pd.DataFrame(ss.data)

