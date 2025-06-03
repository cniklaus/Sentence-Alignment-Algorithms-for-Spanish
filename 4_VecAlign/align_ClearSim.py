import os

i = 0
while i < 3390:
    os.system("./vecalign.py --alignment_max_size 8 --src ClearSim/fac/%i.txt --tgt ClearSim/lf/%i.txt --src_embed ClearSim/overlaps.fac ClearSim/overlaps.fac.emb     --tgt_embed ClearSim/overlaps.lf ClearSim/overlaps.lf.emb --print_aligned_text | tee ClearSim/aligned_fac_lf/%i.txt" % (i, i, i))
    i += 1
