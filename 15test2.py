#coding=utf-8
import  xml.dom.minidom
import csv
#打开xml文档
dom = xml.dom.minidom.parse('152.xml')
#得到文档元素对象
# x.nodeName - x 的名称
# x.nodeValue - x 的值
# x.parentNode - x 的父节点
# x.childNodes - x 的子节点
# x.attributes - x 的属性节点
# root = dom.documentElement
# txt=root.getElementsByTagName("text")[0].childNodes[0].nodeValue
# 文档根元素
rootNode = dom.documentElement
count=0
# 所有句子
sentences = rootNode.getElementsByTagName("sentence")
for sentence_origin in sentences:
    if sentence_origin.hasAttribute("id"):
        # true_term_list = []
        text = sentence_origin.getElementsByTagName("text")[0].childNodes[0].data
        if sentence_origin.getElementsByTagName("Opinions"):
            aspectTerms = sentence_origin.getElementsByTagName("Opinions")[0]
            aspectTerm_list = aspectTerms.getElementsByTagName("Opinion")
            # true_term_list = []
            # polarity=[]
            for aspectTerm in aspectTerm_list:
                # true_term_list.append(aspectTerm.getAttribute("target"))
                Wtarget=aspectTerm.getAttribute("target")
                # polarity.append(aspectTerm.getAttribute("polarity"))
                Wpolarity =aspectTerm.getAttribute("polarity")
                nowTarget=Wtarget  #获取当前的target
                if Wtarget == "NULL":
                    break
                else:
                    # if Wpolarity=="negative":
                    #     Wpolarity=0
                    # if Wpolarity=="positive":
                    #     Wpolarity=1
                    # if Wpolarity=="neutral":
                    #     Wpolarity=2
                    with open(r'15Train.tsv',"a",encoding="UTF-8",newline='') as f:
                        tsv_w = csv.writer(f)
                        if Wpolarity == "negative":
                            Wpolarity = 0
                            printa = tsv_w.writerow([str(count) + '\t' + Wtarget + '\t' + text + '\t' + str(Wpolarity)])
                            print(printa)
                        if Wpolarity == "positive":
                            Wpolarity = 1
                            printa = tsv_w.writerow([str(count) + '\t' + Wtarget + '\t' + text + '\t' + str(Wpolarity)])
                            print(printa)
                        f.close()
                    with open(r'15Train.tsv', "r+", encoding="UTF-8", newline='') as f:
                        content = f.read()
                    with open(r'15Train.tsv', "w+", encoding="UTF-8", newline='') as f:
                        f.write(content.replace('"', ''))
                        f.close()
                    count=count+1



# 先取得node
# strTarget = root.getAttributes().getNamedItem("target").getNodeValue();
# print(strTarget)




# list1=root.getElementsByTagName("text")
# list2=root.getElementsByTagName("Opinion")[0]
# if root.getElementsByTagName("text") and root.getElementsByTagName("text")[0].childNodes[0]:
#         print("666666666666666666")
#
# print(list1.length)
#
#
# rootchild=root.childNodes[0]



# txt2=root.getElementsByTagName("Opinion")[5].getAttribute("target")
# txt3=root.getElementsByTagName("text")[0].childNodes[0].nodeValue
# txt4=root.getElementsByTagName("Opinions")[0].childNodes[0].nodeValue


# print("txt2:"+txt2)
# print("text:"+txt3)
# print("Opinions:"+txt3)
# print(txt2)
#
#
# txt5=root.getElementsByTagName("Opinions")[0].childNodes[0]
#
#
#
# txt3=root.getElementsByTagName("Opinion")[0].getAttribute("polarity")
# len1=len(root.getElementsByTagName("text"))
# len2=len(root.getElementsByTagName("text")[0].childNodes)



# print(len1)
# print(len2)
# print(len3)
# print(txt)
# print(txt2)
# print(txt3)


# for i in range(len1):





# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)
# print(root.ELEMENT_NODE)
