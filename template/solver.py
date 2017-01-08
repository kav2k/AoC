"""AoC 2015.XX problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""


def solver(file):
  """
  Take a file object with input and solve AoC 2015.XX problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  """
  answer_a = 0
  answer_b = 0

  return (answer_a, answer_b)


if __name__ == "__main__":
  import sys
  solution = solver(sys.stdin)

  print("Part A: Solution is {}.".format(solution[0]))
  print("Part B: Solution is {}.".format(solution[1]))
