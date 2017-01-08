"""AoC 2015.04 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys
from hashlib import md5


def solver(file, progress=True, progress_step=10000):
  """
  Take a file object with input and solve AoC 2015.04 problem on the input.

  Outputs progress to STDERR unless silenced.

  Keyword arguments:
  file          --- a file object to read input from
  progress      --- boolean, whether to output progress to stderr (default=True)
  progress_step --- integer, steps to output as progress (default=10000)
  """
  key = file.readline()

  solution_five = -1
  solution_six = -1

  index = 0

  while True:
    string = (key + str(index)).encode('ascii')
    hashed = md5(string).hexdigest()

    if (solution_five < 0 and hashed[0:5] == "00000"):
      solution_five = index
      if progress:
        print("Found solution for 5", file=sys.stderr)

    if (solution_six < 0 and hashed[0:6] == "000000"):
      solution_six = index
      if progress:
        print("Found solution for 6", file=sys.stderr)

    if (solution_five >= 0 and solution_six >= 0):
      return (solution_five, solution_six)

    if(progress and index > 0 and (index % progress_step == 0)):
      sys.stderr.write("\rHashed up to {}.. ".format(index))

    index += 1


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Smallest AdventCoin solution for 5 is {}.".format(solution[0]))
  print("Part B: Smallest AdventCoin solution for 6 is {}.".format(solution[1]))
