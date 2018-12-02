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
  input = list(map(str.strip, file.readlines()))

  answer_a = 0
  answer_b = ""

  twice = 0
  thrice = 0

  for id in input:
    id_twice = 0
    id_thrice = 0
    frequencies = {}

    for letter in id:
      if letter in frequencies:
        frequencies[letter] += 1
      else:
        frequencies[letter] = 1

    for freq in frequencies:
      if frequencies[freq] == 2:
        id_twice = 1
      elif frequencies[freq] == 3:
        id_thrice = 1
    
    twice += id_twice
    thrice += id_thrice
  
  answer_a = twice * thrice

  def find_b():
    answer = ""
    for i, id in enumerate(input):
      for j in range(i):
        count = 0
        for k, letter in enumerate(id):
          if input[j][k] != letter:
            count += 1
        if count == 1:
          for k, letter in enumerate(id):
            if input[j][k] == letter:
              answer += letter
          return answer
  
  answer_b = find_b()

  return (answer_a, answer_b)


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Solution is {}.".format(solution[0]))
  print("Part B: Solution is {}.".format(solution[1]))
