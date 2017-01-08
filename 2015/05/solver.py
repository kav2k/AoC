"""AoC 2015.05 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys
import re


def nice1(string):
  """Check a string for being nice under 'old' rules."""
  vowels = 0
  twice = False
  last = ""

  for character in string:
    if character in ["a", "e", "i", "o", "u"]:
      vowels += 1
    if last == character:
      twice = True
    if (last + character) in ["ab", "cd", "pq", "xy"]:
      return False
    last = character

  return (vowels >= 3 and twice)


def nice2(string):
  """Check a string for being nice under 'new' rules."""
  return re.search(r"(..).*\1", string) and re.search(r"(.).\1", string)


def solver(file):
  """
  Take a file object with input and solve AoC 2015.05 problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  """
  nice_a = 0
  nice_b = 0

  for string in file:
    if nice1(string):
      nice_a += 1
    if nice2(string):
      nice_b += 1

  return (nice_a, nice_b)


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: {} string(s) are nice.".format(solution[0]))
  print("Part B: {} string(s) are nice under new rules.".format(solution[1]))
