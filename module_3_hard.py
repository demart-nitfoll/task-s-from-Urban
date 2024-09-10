def calculate_structure_sum(data):
  total_sum = 0
  total_length = 0
  if isinstance(data, (int, float)):
    return data, 0
  elif isinstance(data, str):
    return 0, len(data)
  elif isinstance(data, (list, tuple, set)):
    for item in data:
      sum_part, length_part = calculate_structure_sum(item)
      total_sum += sum_part
      total_length += length_part
  elif isinstance(data, dict):
    for key, value in data.items():
      sum_part, length_part = calculate_structure_sum(key)
      total_sum += sum_part
      total_length += length_part
      sum_part, length_part = calculate_structure_sum(value)
      total_sum += sum_part
      total_length += length_part
  return total_sum, total_length

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result[0] + result[1])
