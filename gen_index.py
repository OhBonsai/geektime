#!/bin/python3



import os


#for dirpath, dirnames, filenames in os.walk("./build"):
#    print(dirpath, dirnames, filenames)

base = "./build"

for f in os.listdir(base):
    #print(f)
    p = os.path.join(base,f)
    if os.path.isdir(p):
        print('''<h1>{}<h1/>'''.format(f))
        for ff in sorted(os.listdir(p)):
            print('''<a href="{}">{}</a> '''.format("./build/"+f+"/"+ff, ff))


