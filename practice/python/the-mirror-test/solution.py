def the_mirror_test(s: str):
  #clean: lowercase, remove spaces, only alphanumeric
  s = ''.join(c.lower() for c in s if c.isalnum())
  left, right = 0, len(s) - 1
  while left < right:
    if s[left] != s[right]: #the chars are not same then it means that it is not a mirror image
      return False
    left = left + 1
    right = right - 1 
  return True
    
