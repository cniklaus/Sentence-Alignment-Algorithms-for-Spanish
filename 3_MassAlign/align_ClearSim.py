from massalign.core import *

#Get files to align:
i = 1
while i < 3390:
    file1 = 'ClearSim/lf/%i.txt' % i
    file2 = 'ClearSim/fac/%i.txt' % i


    #Train model over them:
    model = TFIDFModel([file1, file2])

    #Get paragraph aligner:
    paragraph_aligner = VicinityDrivenParagraphAligner(similarity_model=model, acceptable_similarity=0.3)

    #Get sentence aligner:
    sentence_aligner = VicinityDrivenSentenceAligner(similarity_model=model, acceptable_similarity=0.2, similarity_slack=0.05)

    #Get MASSA aligner for convenience:
    m = MASSAligner()

    #Get paragraphs from the document:
    p1s = m.getParagraphsFromDocument(file1)
    p2s = m.getParagraphsFromDocument(file2)

    #Align paragraphs:
    alignments, aligned_paragraphs = m.getParagraphAlignments(p1s, p2s, paragraph_aligner)

    #Align sentences in each pair of aligned paragraphs:
    alignmentsl = []
    lines = []
    for a in aligned_paragraphs:
        p1 = a[0]
        p2 = a[1]
        alignments, aligned_sentences = m.getSentenceAlignments(p1, p2, sentence_aligner)

        print(aligned_sentences)
        #lines = []
        for a in aligned_sentences:
            #print(i, len(a), a[0], a[1])
            line = a[0] + "\t" + a[1] + "\n"
            #print(line)
            lines.append(line)

        with open("ClearSim/aligned_lf_fac/%i.txt" % i, "w") as file_out:
            for l in lines:
                file_out.write(l)

        #Display sentence alignments:
        #m.visualizeSentenceAlignments(p1, p2, alignments)
        #m.visualizeListOfSentenceAlignments([p1, p1], [p2, p2], [alignments, alignments])

    i += 1
