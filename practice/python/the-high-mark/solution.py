def running_peak(nums: list[int]) -> list[int]:
  
  #empty list
  if not nums:
    return []
  
  max_seen = nums[0]
  output = []
  
  for num in nums:
    if num > max_seen:
      max_seen = num
    output.append(max_seen)
    
  return output
