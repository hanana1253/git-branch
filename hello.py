def print_hello():
  """
  print formatted string with i if i is odd.
  else, print hello git.
  """
  for i in range(1,10+1):
    if i%2==0:
      print('hello, git!')
    else:
      print('hello, git for {}th time(s)!'.format(i))

if __name__=='__main__':
  print_hello()
