import csv

with open(r'15Train.tsv',"w",encoding="UTF-8",newline='') as f:
    tsv_w=csv.writer(f)
    qid="qid"
    text_a="text_a"
    text_b="text_b"
    label="label"
    # text = "pastas"
    # target = "The pastas are incredible, the risottos (particularly the sepia) are fantastic and the braised rabbit is amazing."
    # polarity = "positive"
    # label = "1"

    tsv_w.writerow([qid+'\t'+text_a+'\t'+text_b+'\t'+label])

    f.close()