def high_water_marks(readings: list) -> list:
  
  current_max_temp = readings[0]
  output = []
  for reading in readings:
    if reading > current_max_temp:
      current_max_temp = reading
    output.append(current_max_temp)
    
  return output
