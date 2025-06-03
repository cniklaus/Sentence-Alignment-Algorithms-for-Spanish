import os
import shutil

os.system(
    "python german_aligner.py   -out_dir ClearSim/alignFACLF_full -batch_size 32 -w2v_model_path models/cc.es.300.vec -vec_size 300 -rolling_thresholds 0.5")
