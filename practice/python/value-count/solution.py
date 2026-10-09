def count_occur(items: list, target) -> int:
  
  count = 0
  for i in range(len(items)):
    if items[i] == target:
      count = count + 1
      
  return count
