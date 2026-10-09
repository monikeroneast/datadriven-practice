def filter_records(records, criteria):
  #empty list
  result = []
  for record in records:
    match = True
    for key, value in criteria.items():
      if key not in record or record[key] != value:
        match = False
        break;
    if match:
      result.append(record)
      
  return result
