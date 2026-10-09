def chunk_list(lst, n):
  
  output = []
  for i in range(0, len(lst), n):
      output.append(lst[i : i+n])

  return output
