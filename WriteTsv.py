import csv

# with open(,"a",encoding="UTF-8",newline='') as f:
with open(r'./new/15Test.tsv','r+',encoding="utf8",newline='') as tsvin, open(r'./new/15Test.tsv','a',encoding='utf-8',newline='') as csvout:


    tsvin = csv.reader(tsvin, delimiter='\t')
    number=0
    oldTarget=None
    a=0
    for row in tsvin:
        if(row==0):
            csvout = csv.writer(csvout)
            qid = "qid"
            text_a = "text_a"
            text_b = "text_b"
            label = "label"
            csvout.writerow([qid + '\t' + text_a + '\t' + text_b + '\t' + label])
            break
        nowTarget=row[1]
        if(oldTarget==nowTarget):
            number=number+1
        newtemp=a-number
        row[0]=str(newtemp)
        oldTarget=row[1]
        a=a+1
        qid = row[0]
        text_a = row[1]
        text_b = row[2]
        label = row[3]
        with open(r'./new/15Test.tsv', 'a', encoding='utf-8', newline='') as csvout:
            csvout = csv.writer(csvout)
            csvout.writerow([qid + '\t' + text_a + '\t' + text_b + '\t' + label])
        print(row)






# with open(r'file.tsv',"r+",encoding="UTF-8",newline='') as f:
#     content=f.read()
# with open(r'file.tsv',"w+",encoding="UTF-8",newline='') as f:
#     f.write(content.replace('"',''))
