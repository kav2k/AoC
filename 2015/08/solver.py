"""AoC 2015.08 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys


def unescape(string):
  """
  Take a string according to challenge specifications, and perform unescape.

  Keyword arguments:
  string --- a string to unescape
  """
  result = ""
  index = 0
  while index < len(string):
    if string[index] == "\\":
      if string[index + 1] == "\\":
        result += "\\"
        index += 2
      elif string[index + 1] == "\"":
        result += "\""
        index += 2
      elif string[index + 1] == "x":
        result += chr(int(string[index + 2: index + 4], base=16))
        index += 4
      else:
        raise ValueError("Unexpected escape string:", "\\" + string[index + 1])
    else:
      result += string[index]
      index += 1

  return result


def escape(string):
  """
  Take a string according to challenge specifications, and perform escape.

  Keyword arguments:
  string --- a string to escape
  """
  result = ""
  for character in string:
    if character == "\"":
      result += "\\\""
    elif character == "\\":
      result += "\\\\"
    else:
      result += character

  return result


def solver(file):
  """
  Take a file object with input and solve AoC 2015.08 problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  """
  code_length = 0
  unescaped_length = 0
  escaped_length = 0

  for line in file:
    code_length += len(line)
    unescaped_length += len(unescape(line[1:-1]))
    escaped_length += len(escape(line)) + 2

  return (code_length - unescaped_length, escaped_length - code_length)


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Length difference between code and data is {} characters.".format(solution[0]))
  print("Part B: Length difference between escaped code and code is {} characters.".format(solution[1]))
