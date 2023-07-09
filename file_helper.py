import os
import json

def is_file_empty(file_path):
    '''Verifica si un archivo esta vacio''' 
    if os.path.exists(file_path):
        # return True
         if os.stat(file_path).st_size == 0:
              return True
         else:
              return False
    else:
         return False
    

class CustomEncoder(json.JSONEncoder): 
    def default(self, o):
            return o.__dict__