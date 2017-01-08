"""AoC 2015.03 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys


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


def move(position, instruction):
  """
  Take a position and offset it based on instuction, or raise an error on invalid instruction.

  Keyword arguments:
  position    --- current position as a tuple (x,y)
  Instruction --- single-character instruction to move in ["^", "v", ">", "<"]
  """
  if instruction == "^":
    return (position[0], position[1] + 1)
  elif instruction == "v":
    return (position[0], position[1] - 1)
  elif instruction == ">":
    return (position[0] + 1, position[1])
  elif instruction == "<":
    return (position[0] - 1, position[1])
  else:
    raise ValueError("Instruction '{}' not recognized".format(instruction))


def solver(file):
  """
  Take a file object with input and solve AoC 2015.03 problem on the input.

  Keyword arguments:
  file      --- a file object to read input from
  """
  alone = set([(0, 0)])
  alone_position = (0, 0)

  together = set([(0, 0)])
  santa_position = (0, 0)
  robot_position = (0, 0)
  robot_turn = False

  for instruction in chars(file):
    alone_position = move(alone_position, instruction)
    alone.add(alone_position)

    if robot_turn:
      robot_position = move(robot_position, instruction)
      together.add(robot_position)
    else:
      santa_position = move(santa_position, instruction)
      together.add(santa_position)

    robot_turn = not robot_turn

  return (len(alone), len(together))


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Santa alone will deliver presents to {} houses.".format(solution[0]))
  print("Part B: Santa and Robo-Santa will deliver presents to {} houses.".format(solution[1]))
