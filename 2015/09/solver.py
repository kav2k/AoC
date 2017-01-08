"""AoC 2015.09 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys
from math import factorial
import re


def permute(list, index):
  """
  Return index-th permutation of a list.

  Keyword arguments:
  list  --- the list to be permuted
  index --- index in range (0, factorial(len(list)))
  """
  if len(list) < 2:
    return list
  (rest, choice) = divmod(index, len(list))
  return [list[choice]] + permute(list[0:choice] + list[choice + 1:len(list)], rest)


def distance(route, graph):
  """
  Calculate total distance for a given route through a graph.

  Keyword arguments:
  route --- a list of node names that form the route
  graph --- a dictionary mapping node name pairs to distance
  """
  length = 0
  for i in range(1, len(route)):
    length += graph[(route[i - 1], route[i])]
  return length


def solver(file):
  """
  Take a file object with input and solve AoC 2015.09 problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  """
  graph = {}
  places = set()
  for line in file:
    (start, end, length) = re.match(r"(\w+) to (\w+) = (\d+)", line).groups()
    places.add(start)
    places.add(end)
    graph[(start, end)] = int(length)
    graph[(end, start)] = int(length)

  places = list(places)

  min_length = 100000000
  max_length = 0
  min_route = []
  max_route = []
  for route in [permute(places, index) for index in range(0, factorial(len(places)))]:
    length = distance(route, graph)
    if min_length > length:
      min_length = length
      min_route = route
    if max_length < length:
      max_length = length
      max_route = route

  return ((min_length, "->".join(min_route)), (max_length, "->".join(max_route)))


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: The length of minimal route {1} is {0}.".format(*solution[0]))
  print("Part B: The length of maximal route {1} is {0}.".format(*solution[1]))
