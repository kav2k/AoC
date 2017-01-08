"""AoC 2015.06 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import re

GRID_SIZE = 1000


def execute(lights, instruction):
  """
  Take an instruction as a string and apply it to a 2D array of boolean lights.

  Modifies the array in-place.

  Keyword arguments:
  lights      --- a flattened 2D array of boolean light states
  instruction --- an instruction formatted according to the challenge rules
  """
  (command, x1, y1, x2, y2) = re.match("(.+) (\d+),(\d+) through (\d+),(\d+)", instruction).groups()
  [x1, y1, x2, y2] = map(int, [x1, y1, x2, y2])

  for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
      if command == "turn on":
        lights[x + GRID_SIZE * y] = True
      elif command == "turn off":
        lights[x + GRID_SIZE * y] = False
      elif command == "toggle":
        lights[x + GRID_SIZE * y] = not lights[x + GRID_SIZE * y]


def execute_bright(lights, instruction):
  """
  Take an instruction as a string and apply it to a 2D array of brightness-enabled lights.

  Modifies the array in-place.

  Keyword arguments:
  lights      --- a flattened 2D array of boolean light states
  instruction --- an instruction formatted according to the challenge rules
  """
  (command, x1, y1, x2, y2) = re.match("(.+) (\d+),(\d+) through (\d+),(\d+)", instruction).groups()
  [x1, y1, x2, y2] = map(int, [x1, y1, x2, y2])

  for y in range(y1, y2 + 1):
    for x in range(x1, x2 + 1):
      if command == "turn on":
        lights[x + GRID_SIZE * y] += 1
      elif command == "turn off" and lights[x + GRID_SIZE * y]:
        lights[x + GRID_SIZE * y] -= 1
      elif command == "toggle":
        lights[x + GRID_SIZE * y] += 2


def solver(file, progress=True):
  """
  Take a file object with input and solve AoC 2015.06 problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  progress      --- boolean, whether to output progress to stderr (default=True)
  """
  number_lit = 0
  total_brightness = 0

  lights = [False for _ in range(0, GRID_SIZE * GRID_SIZE)]
  bright_lights = [0 for _ in range(0, GRID_SIZE * GRID_SIZE)]

  counter = 0
  for instruction in file:
    execute(lights, instruction)
    execute_bright(bright_lights, instruction)
    if progress:
      counter += 1
      sys.stderr.write("\rProcessed {:03d} instructions".format(counter))

  if progress:
    sys.stderr.write("\n")

  for index in range(0, GRID_SIZE * GRID_SIZE):
    if lights[index]:
      number_lit += 1
    total_brightness += bright_lights[index]

  return (number_lit, total_brightness)


if __name__ == "__main__":
  import sys
  solution = solver(sys.stdin)

  print("Part A: After following instructions, {} lights are lit.".format(solution[0]))
  print("Part B: After following instructions, total brightness is {}.".format(solution[1]))
