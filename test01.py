import csv

with open(r'16Train.tsv',"w",encoding="UTF-8",newline='') as f:
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


# with open(,"a",encoding="UTF-8",newline='') as f:
with open(r'./old/16Train.tsv','r',encoding="utf8",newline='') as tsvin, open(r'16Train.tsv','a',encoding='utf-8',newline='') as csvout:
    qid=[]
    text_a=[]
    text_b=[]
    label=[]
    newrow=[]

    tsvin = csv.reader(tsvin, delimiter='\t')
    number=0
    oldTarget=None
    a=0
    index=0
    for row in tsvin:
        if(a==0):
            a=a+1
            continue
        try:
            nowTarget=row[1]
        except:
            print("发生异常")
            break
        # print(row[1])
        # print(nowTarget)
        if(oldTarget==nowTarget):
            continue
        row[0]=index
        newrow.append(row)

        # qid.append(index)
        # text_a.append(row[1])
        # text_b.append(row[2])
        # label.append(row[3])
        index=index+1
        a=a+1
        oldTarget=nowTarget

    i=0
    for row in newrow:
        if(i==0):
            qid0 = "qid"
            text_a0 = "text_a"
            text_b0 = "text_b"
            label0 = "label"
            csvout = csv.writer(csvout,delimiter='\t')
            csvout.writerow(row)
            i=i+1
            continue
        i = i + 1
        csvout.writerow(row)




        # newtemp=a-number
        # row[0]=str(newtemp)
        # oldTarget=row[1]
        # a=a+1


    print(a)