def coalesce(primary: dict, defaults: dict) -> dict:
  #empty dict
  result = {}
  
  for key, value in primary.items():
    if value is None:
      result[key] = defaults.get(key)
    else:
      result[key] = value
      
  return result
