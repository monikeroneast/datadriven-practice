def count_nulls(values):
 
  count = 0
  for i in range(len(values)):
    if values[i] is None:
      count = count + 1

  return count
