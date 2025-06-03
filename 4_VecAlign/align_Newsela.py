import os

i = 0
while i < 243:
    os.system("./vecalign.py --alignment_max_size 8 --src Newsela/level2_preprocessed/%i.txt --tgt Newsela/level4_preprocessed/%i.txt --src_embed Newsela/overlaps.level2 Newsela/overlaps.level2.emb     --tgt_embed Newsela/overlaps.level4 Newsela/overlaps.level4.emb --print_aligned_text | tee Newsela/aligned24/%i.txt" % (i, i, i))
    i += 1