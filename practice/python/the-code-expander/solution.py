def decode_rle(encoded: str) -> str:
  #rle: running length encoding
  #uses 2 - pointer
  #slow pointer is the start of the block like "3a"
  #fast pointer moves till it gets a char
  
  i = 0
  n = len(encoded)
  res = []
  while i < n:
    j = i
    #for a block starting at i; j moves till it gets a char
    while j < n and encoded[j].isdigit():
      j += 1
    #count and char
    count = int(encoded[i:j])
    char = encoded[j]
    res.append(count * char)
    
    i = j + 1 #i has to move to next block
  
  return "".join(res)
      





 
