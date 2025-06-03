i = 0
while i < 243:
    sources = []
    targets = []
    with open("Newsela/aligned02/%i.txt" % i, "r") as f:
        for line in f:
            if line.startswith("                                         SRC:"):
                sources.append(line.split("SRC:")[1].strip())
            if line.startswith("                                         TGT:"):
                targets.append(line.split("TGT:")[1].strip())
    print(sources)

    with open("Newsela/final_aligned/final_aligned02/%i.txt" % i, "w") as s_file:
        count = 0
        while count < len(sources):
            s_file.write(sources[count] + "\t" + targets[count] + "\n")
            count += 1

    i += 1