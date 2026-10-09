def remove_dupes(items):
  
  seen = set()
  output = []
  
  for item in items:
    if item not in seen:
      seen.add(item)
      output.append(item)
    
  return output
