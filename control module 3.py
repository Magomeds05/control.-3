data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_sum(data_structure):
    summa = 0
    if isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (int, float)):
        return data_structure
    elif isinstance(data_structure, (list, set, tuple)):
        for i in data_structure:
            summa += calculate_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure. items():
            summa += calculate_sum(key)
            summa += calculate_sum(value)
    return summa


print(calculate_sum(data_structure))

