from bertalign import Bertalign

i = 0
while i < 243:

    src = open("Newsela/level2_preprocessed/%i.txt" % i, "rt", encoding='utf-8').read()
    tgt = open("Newsela/level4_preprocessed/%i.txt" % i, "rt", encoding='utf-8').read()
    alg = open("Newsela/aligned_level24/%i.txt" % i, "w")

    print("Start aligning {} to {}".format(i, i))
    aligner = Bertalign(src, tgt, is_split=True)
    aligner.align_sents()
    print(aligner.result)

    lines = aligner.print_sents()

    for l in lines:
        alg.write(l)

    i += 1


