def forward_fill(values: list) -> list:
    
  last_seen = None
  output = []
  
  for value in values:
    if value is not None:
      last_seen = value
    
    output.append(last_seen)
  
  return output
    
