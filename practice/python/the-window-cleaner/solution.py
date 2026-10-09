def longest_unique_substr(s):
  #create a hash map for chararcter and their latest index
  char_map = {}
  #left pointer
  left = 0
  #max_length/ window length
  max_length = 0
  
  for right in range(len(s)):
    current_char = s[right]
    #if the current char index is in the hash map and its index is inside the current window (meaning a duplicate), 
    #jump the left pointer directly past the value of the duplicates
    if current_char in char_map and char_map[current_char] >= left:
      left = char_map[current_char] + 1
    #update the character's latest position  
    char_map[current_char] = right
    #find the window size
    max_length = max(max_length, right - left + 1)
    
  return max_length
