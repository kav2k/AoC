"""AoC 2015.10 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys


def look_and_say(string):
  """
  Expand a string of digits according to look-and-say process in the problem.

  Keyword arguments:
  string --- a string to be processed
  """
  result = ""
  last = ""
  count = 0

  for digit in string:
    if digit != last:
      if(count):
        result += str(count) + last
      last = digit
      count = 1
    else:
      count += 1

  if(count):
    result += str(count) + last

  return result


def solver(file, progress=True):
  """
  Take a file object with input and solve AoC 2015.10 problem on the input.

  Outputs progress to STDERR unless silenced.

  Keyword arguments:
  file          --- a file object to read input from
  progress      --- boolean, whether to output progress to STDERR
  """
  seed = file.readline()
  result = seed

  for i in range(0, 50):
    result = look_and_say(result)
    if i == 39:
      result40 = result
    if progress:
      sys.stderr.write("\rProcessed {}/{} steps..".format(i + 1, 50))

  if progress:
      sys.stderr.write("\n")

  return (len(result40), len(result))


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Length after 40 steps is {}.".format(solution[0]))
  print("Part B: Length after 50 steps is {}.".format(solution[1]))
