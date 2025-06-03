import csv
import spacy
nlp = spacy.load('es_core_news_sm')

count = 0
while count < 242:
    with open("Newsela/level0_preprocessed/%a.txt" % count, "r") as sentence_file:
        sentences = sentence_file.readlines()
        sentences_stripped = []
        for s in sentences:
            sentences_stripped.append(s.strip())
        print(sentences_stripped)

    with open("Newsela/final_aligned/final_aligned01/%a.txt" % count, "r") as aligned_sentences_file:
        aligned_sentences = aligned_sentences_file.readlines()

        for elem in aligned_sentences:
            source = elem.split("\t")[0].strip()
            target = elem.split("\t")[1].strip()


        #sentences_original = [i.text for i in nlp(text).sents]

        #with open("SimCor/preprocessed/original/%a.txt" % count, "w") as original_file:
        #    for o in sentences_original:
        #        original_file.write(o + '\n')

    count += 1
