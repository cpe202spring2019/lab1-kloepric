
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if(int_list == []):
      return None
   elif(int_list == None):
      raise ValueError
   elif(len(int_list) > 1):
      temp = int_list[0]
      for i in range(1,len(int_list)):
            if(temp < int_list[i]):
               temp = int_list[i]
      return(temp)

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if(int_list == None):
      raise ValueError
   if(len(int_list) == 1 or len(int_list) == 0):
      return int_list
   return ((reverse_rec(int_list[1:])) + [int_list[0]])
      
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if(int_list == None):
      raise ValueError
   if(target == int_list[len(int_list)//2]):
      return(int_list[len(int_list)//2])   
   elif(target < int_list[len(int_list)//2]):   
      return(bin_search(target, low, high, int_list[:(len(int_list)//2)]))
   elif(target > int_list[len(int_list)//2]):
      return(bin_search(target, low, high, int_list[(len(int_list)//2):]))
   return(None)
