import os

files = os.listdir()
for file in files:
  if file.endswith(".bmp"):
    fname = file.split(".")[0]
    new_fname = "%04d.bmp" % int(fname)
    print(new_fname)
    if (new_fname != file):
      os.rename(file, new_fname)