"""AoC 2015.07 problem solver.

Takes input from STDIN by default.

(c) Alexander Kashev, 2017
"""
import sys
import re


def parse(instruction):
  """
  Take an instruction as a string and return a tuple (output wire, input specification).

  Example input specifications:
  * ("ID", "6") for constant input
  * ("ID", "a") for direct wire input "a"
  * ("NOT", "ab") for negated wire "ab"
  * ("AND", "76", "xy") for bitwise-AND between constant and wire "ab"

  Keyword arguments:
  instruction --- an instruction formatted according to the challenge rules
  """
  match = re.search("^(.*) -> ([a-z]+)$", instruction)
  if match:
    (input_expression, output_wire) = match.groups()

    if " " not in input_expression:
      input_command = ("ID", input_expression)
    elif "NOT" in input_expression:
      submatch = re.search(r"^NOT (\w+)$", input_expression)
      if submatch:
        input_command = ("NOT", submatch.group(1))
      else:
        raise ValueError("Illegal instruction:", instruction)
    else:
      submatch = re.search(r"^(\w+) ([A-Z]+) (\w+)$", input_expression)
      if submatch:
        input_command = (submatch.group(2), submatch.group(1), submatch.group(3))
      else:
        raise ValueError("Illegal instruction:", instruction)

    return (output_wire, input_command)
  else:
    raise ValueError("Illegal instruction:", instruction)


def compute(wire_id, wire_specs):
  """
  Take a wire identifier and compute its output according to wire specification.

  Will overwrite specifications with computed values as caching.

  Keyword arguments:
  wire_id    --- string, a wire identifier
  wire_specs --- dictionary, mapping output wire to input specification
  """
  if wire_id.isdecimal():
    return int(wire_id)
  if isinstance(wire_specs[wire_id], int):
    return wire_specs[wire_id]
  else:
    command = wire_specs[wire_id][0]
    gate_input1 = compute(wire_specs[wire_id][1], wire_specs)
    if len(wire_specs[wire_id]) == 3:
      gate_input2 = compute(wire_specs[wire_id][2], wire_specs)

    if command == "ID":
      gate_output = gate_input1
    elif command == "NOT":
      gate_output = ~ gate_input1 & (2**16 - 1)
    elif command == "AND":
      gate_output = gate_input1 & gate_input2
    elif command == "OR":
      gate_output = gate_input1 | gate_input2
    elif command == "LSHIFT":
      gate_output = (gate_input1 << gate_input2) & (2**16 - 1)
    elif command == "RSHIFT":
      gate_output = (gate_input1 >> gate_input2) & (2**16 - 1)

    wire_specs[wire_id] = gate_output  # Cache the result by overwriting spec with value
    return gate_output


def solver(file):
  """
  Take a file object with input and solve AoC 2015.07 problem on the input.

  Keyword arguments:
  file          --- a file object to read input from
  """
  wire_specs_a = {}
  wire_specs_b = {}

  for instruction in file:
    (output_id, input_spec) = parse(instruction)
    wire_specs_a[output_id] = input_spec
    wire_specs_b[output_id] = input_spec

  output_a = compute("a", wire_specs_a)

  wire_specs_b["b"] = output_a  # Overwrite spec with value
  output_b = compute("a", wire_specs_b)

  return (output_a, output_b)


if __name__ == "__main__":
  solution = solver(sys.stdin)

  print("Part A: Output on wire 'a' is {}.".format(solution[0]))
  print("Part B: Output on wire 'a' after modification is {}.".format(solution[1]))
