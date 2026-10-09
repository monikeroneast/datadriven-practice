def fix_running_average(nums: list) -> list:
  # BUG(S) BELOW - find and fix them
  result = []
  total = 0
  for i in range(len(nums)):
    total = total + nums[i]
    avg = total / (i + 1)
    result.append(avg)
  return result
