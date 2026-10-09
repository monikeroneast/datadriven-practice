def dedup_preserve_order(items: list) -> list:
    
    seen = set()
    output = []
    
    for item in items:
      if item not in seen:
        seen.add(item)
        output.append(item)
    
    return output
