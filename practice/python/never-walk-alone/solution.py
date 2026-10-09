def sequential_word_pairs(text: str):
   
   words = text.split()
   output = []
   for i in range(0, len(words) - 1):
     output.append([words[i], words[i+1]])
    
   return output
     
