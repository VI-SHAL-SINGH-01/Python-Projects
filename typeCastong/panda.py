#from multiprocessing.managers import convert_to_error
import json

import pandas as pd
d={'id':[1,2,3,4,5],'name':['a','b','c','d','e']}

#df.to_csv("f:\\this.csv")
with open('convert.txt', 'w') as convert_file:
    convert_file.write(json.dumps(details))