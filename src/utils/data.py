import os
import shutil

def remake_folder(path):
  if os.path.exists(path):
    shutil.rmtree(path)
  os.makedirs(path)