"""AoC 2015.02 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""


def parseBox(line):
  """
  Take a line of the form "NxNxN" and parse it into a sorted tuple (length, width, height).

  Keyword arguments:
  line      --- a string to be parsed as box specifications
  """
  dimensions = sorted(map(int, line.split("x")))
  return (dimensions[2], dimensions[1], dimensions[0])


def solver(file):
  """
  Take a file object with input and solve AoC 2015.02 problem on the input.

  Keyword arguments:
  file      --- a file object to read input from
  """
  paper = 0
  ribbon = 0

  for line in file:
    (length, width, height) = parseBox(line)
    paper += 2 * length * width + 2 * length * height + 3 * width * height
    ribbon += 2 * (width + height) + (length * width * height)

  return (paper, ribbon)


if __name__ == "__main__":
  import sys
  solution = solver(sys.stdin)

  print("Part A: Total wrapping paper required: {} square feet.".format(solution[0]))
  print("Part B: Total ribbon required: {} feet.".format(solution[1]))
