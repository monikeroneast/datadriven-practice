def missing_keys(record: dict, required: list) -> list:
 #empty list
  result = []
   
  for key in required: 
    if key not in record:
      result.append(key)
       
  return sorted(result)
