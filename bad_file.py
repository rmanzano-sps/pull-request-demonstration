boolValue = True  
def Is_Boolean(checkval):
   is_bool = True
   try:
      bool(checkval)
   except TypeError:
      is_bool = False
   return is_bool



