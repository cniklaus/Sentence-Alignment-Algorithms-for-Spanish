import os
import shutil
from gensim.models.keyedvectors import KeyedVectors

#nums = [0, 3, 5, 11, 32, 37, 42, 52, 53, 57, 61, 69, 78, 79, 81, 85, 86, 87, 89, 90, 91, 93, 98, 99, 101, 102, 103, 104, 113, 114, 116, 118, 123, 125, 126, 130, 131, 137, 142, 150, 153, 155, 157, 161, 167, 170, 174, 178, 185, 192, 193, 194, 195, 199, 201, 204, 206, 209, 212, 221, 226, 229, 232, 238, 241, 242]

#for i in nums:
 #   shutil.copyfile(f'Newsela/doc_level_files/docs0/{i}.txt', f'Newsela/doc_level_files/docs0_sample/{i}.txt')
  #  shutil.copyfile(f'Newsela/doc_level_files/docs2/{i}.txt', f'Newsela/doc_level_files/docs2_sample/{i}.txt')
   # shutil.copyfile(f'Newsela/doc_level_files/docs4/{i}.txt', f'Newsela/doc_level_files/docs4_sample/{i}.txt')




#i = 0
#while i < 2:
   #for i in nums:
   #os.system("python german_aligner.py -src Newsela/doc_level_files/docs0/%i.txt -tgt Newsela/doc_level_files/docs2/%i.txt -src_sents Newsela/level0_final/%i.txt -tgt_sents Newsela/level2_final/%i.txt  -out_dir Newsela/align02_full -batch_size 1 -w2v_model_path models/cc.es.300.vec -vec_size 300 -rolling_thresholds 0.5" % (i, i, i, i))
   #i += 1

os.system(
      "python german_aligner.py -out_dir Newsela/align24_full -batch_size 1 -w2v_model_path models/cc.es.300.vec -vec_size 300 -rolling_thresholds 0.5")
   #i += 1

#for i in nums:
   #os.system("python german_aligner.py -src Newsela/doc_level_files/docs0_sample/%i.txt -tgt Newsela/doc_level_files/docs4_sample/%i.txt -src_sents Newsela/level0_final/%i.txt -tgt_sents Newsela/level4_final/%i.txt  -out_dir Newsela/align04 -batch_size 512 -w2v_model_path models/cc.es.300.vec -vec_size 300 -rolling_thresholds 0.5" % (i, i, i, i))

#for i in nums:
   #os.system("python german_aligner.py -src Newsela/doc_level_files/docs2_sample/%i.txt -tgt Newsela/doc_level_files/docs4_sample/%i.txt -src_sents Newsela/level2_final/%i.txt -tgt_sents Newsela/level4_final/%i.txt  -out_dir Newsela/align24 -batch_size 512 -w2v_model_path models/cc.es.300.vec -vec_size 300 -rolling_thresholds 0.5" % (i, i, i, i))