


def process(input_name,output_name):

  f = open(input_name,encoding="utf-8",mode="r")
  f2 = open(output_name,encoding="utf-8",mode="w")
  for i,line in enumerate(f):
    if i<200:
        f2.write(line)
    else:
        break

process("../Amazon-670K/train_raw_texts.txt","./train_raw_texts.txt")
process("../Amazon-670K/test_raw_texts.txt","./test_raw_texts.txt")
process("../Amazon-670K/train_labels.txt","./train_labels.txt")
process("../Amazon-670K/test_labels.txt","./test_labels.txt")
process("../Amazon-670K/train_v1.txt","./train_v1.txt")