from django.http import HttpResponse
from mysite.main.solver.grid import grid

import json

initial_grid = grid()
json_data = json.dumps(initial_grid.tolist())

import json
from json import JSONEncoder
import numpy
import numpy as np
import codecs, json

a = np.arange(10).reshape(2,5) # a 2 by 5 array
b = a.tolist() # nested lists with same data, indices
file_path = "path.json" ## your path variable
json.dump(b, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) #