"""AoC 2018.01 problem solver.

Takes input from STDIN by default.
"""
import sys

def solver(file):
  """
  Take a file object with input and solve AoC 2015.XX problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  """
  input = list(map(int, map(str.strip, file.readlines())))

  freq = 0

  for adj in input:
    freq += adj

  answer_a = freq

  print(answer_a)

  freq_set = set([0])
  freq = 0
  searching = True

  while searching:
    for adj in input:
      freq += adj
      if freq in freq_set:
        answer_b = freq
        searching = False
        break
      else:
        freq_set.add(freq)

  return (answer_a, answer_b)


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Solution is {}.".format(solution[0]))
  print("Part B: Solution is {}.".format(solution[1]))
