import os

i = 0
while i < 243:
    #os.system("python main.py -ic Newsela/level2_preprocessed/%i.txt -it Newsela/level4_preprocessed/%i.txt -o Newsela/C3G/aligned24/%i.txt  -l 'es' -s 'C3G' -a 'sentence' -t closestSimStrategy -ll line" % (i, i, i))
    os.system("python main.py -ic Newsela/level2_preprocessed/%i.txt -it Newsela/level4_preprocessed/%i.txt -o Newsela/CWASA/aligned24/%i.txt  -l 'es' -s 'CWASA' -a 'sentence' -t closestSimStrategy -ll line -e cc.es.300.vec" % (i, i, i))
    #os.system("python main.py -ic Newsela/level2_preprocessed/%i.txt -it Newsela/level4_preprocessed/%i.txt -o Newsela/WAVG/aligned24/%i.txt  -l 'es' -s 'WAVG' -a 'sentence' -t closestSimStrategy -ll line -e cc.es.300.vec" % (i, i, i))
    i += 1