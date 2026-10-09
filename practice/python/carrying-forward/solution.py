def running_total(deposits):
 
  prefix = [0]
  total = 0 
  
  for i in deposits:
    total = total + i 
    prefix.append(total)
    
  return prefix[1:]
