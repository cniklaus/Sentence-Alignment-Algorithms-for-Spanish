import os

i = 0
while i < 3390:
    os.system("python main.py -ic ClearSim/fac/%i.txt -it ClearSim/lf/%i.txt -o ClearSim/WAVG/aligned_fac_lf/%i.txt  -l 'es' -s 'WAVG' -a 'sentence' -t closestSimStrategy -ll line -e cc.es.300.vec" % (i, i, i))
    i += 1
