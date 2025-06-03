from bertalign import Bertalign

i = 3363
while i < 3390:

    src = open("ClearSim/original/%i.txt" % i, "rt", encoding='utf-8').read()
    tgt = open("ClearSim/lf/%i.txt" % i, "rt", encoding='utf-8').read()
    alg = open("ClearSim/aligned/aligned_orig_lf/%i.txt" % i, "w")

    print("Start aligning {} to {}".format(i, i))
    aligner = Bertalign(src, tgt, is_split=True)
    aligner.align_sents()
    print(aligner.result)

    lines = aligner.print_sents()

    for l in lines:
        alg.write(l)

    i += 1


