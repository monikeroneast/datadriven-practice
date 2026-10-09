def sum_list(counts: list) -> int:
  
  prefix = [0]
  total = 0
  
  for events in counts:
    total = total + events
    prefix.append(total)

  return prefix[-1]
