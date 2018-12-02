"""AoC 2017.01 problem solver.

Takes input from STDIN by default.
"""
import sys


def solver(file):
  captcha_a = 0
  captcha_b = 0

  input = list(map(int, str.strip(file.readline())))
  length = len(input)

  for idx, val in enumerate(input):
    
    idx_a = (idx + 1) % length
    idx_b = (idx + (length // 2)) % length
    if val == input[idx_a]:
      captcha_a += val
    if val == input[idx_b]:
      captcha_b += val

  return (captcha_a, captcha_b)


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Solution is {}.".format(solution[0]))
  print("Part B: Solution is {}.".format(solution[1]))
