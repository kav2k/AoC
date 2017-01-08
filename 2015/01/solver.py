"""AoC 2015.01 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""


def chars(file, chunkSize=4096):
  """
  Take a file object, read it in chuncks and iterate over it one character at a time.

  Keyword arguments:
  file      --- a file object to iterate over
  chunkSize --- buffer size for file reads (default=4096)
  """
  chunk = file.read(chunkSize)
  while chunk:
    for char in chunk:
      yield char
    chunk = file.read(chunkSize)


def solver(file):
  """
  Take a file object with input and solve AoC 2015.01 problem on the input.

  Keyword arguments:
  file      --- a file object to read input from
  """
  level = 0
  step = 0
  basement = 0

  for instruction in chars(file):
    if instruction == "(":
      step += 1
      level += 1
    elif instruction == ")":
      step += 1
      level -= 1

    if not basement and level == -1:
      basement = step

  return (level, basement)


if __name__ == "__main__":
  import sys
  solution = solver(sys.stdin)

  print("Part A: Final level is {}".format(solution[0]))

  if solution[1]:
    print("Part B: First entered basement on step {}".format(solution[1]))
  else:
    print("Part B: Never entered basement")
