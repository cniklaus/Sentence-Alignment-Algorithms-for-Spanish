
i = 0

while i < 3390:
    lines_doc = []
    with open("ClearSim/original/%i.txt" % i, "r") as file:
        for line in file:
            lines_doc.append(line.strip())
        lines_doc.append("\n")

    lines_doc = lines_doc[:-1]

    #with open("SimCor/original/%i.txt" % i, "a+") as file:
        #file.write(".eoa")

    with open("ClearSim/doc_level_files/docs_orig/%i.txt" % i, "w") as f_out:
        l_count = 0
        for line in lines_doc:
            if l_count == len(lines_doc) - 1:
                f_out.write(line)
            else:
                f_out.write(line + " ")
            l_count += 1

    with open("ClearSim/orig_final/%i.txt" % i, "w") as f_out2:
        for line in lines_doc:
            f_out2.write(line + "\n")
        f_out2.write(".eoa")

    i += 1
