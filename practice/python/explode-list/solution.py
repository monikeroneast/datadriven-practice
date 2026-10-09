def flatten(nested):

  output = []
  for row in nested:
    for item in row:
      output.append(item)

  return output
