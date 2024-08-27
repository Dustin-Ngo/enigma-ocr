def stringfunc(func1, output):
  return func1(output)

def intfunc(func1, output):
  return func1(int(output))

def intlistfunc(func1, output):
  nlist = output.split()
  for i in nlist:
    nlist[i] = int(nlist[i])
  return func1(nlist)