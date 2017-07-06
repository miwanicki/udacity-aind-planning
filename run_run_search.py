from os import system
from datetime import datetime

problems = [1,2,3]
#methods = [1,2,3,4,5,6,7]
methods = [8,9,10]

for p in problems:
    for m in methods:
        print('python3 run_search.py -p {} -s {} > result_{}_{}'.format(p,m,p,m))
        print(str(datetime.now()))
        system('python3 run_search.py -p {} -s {} > result_{}_{}'.format(p,m,p,m))
