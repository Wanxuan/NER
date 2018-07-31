# encoding=utf-8
import thulac

fileTrainRead = []
with open('corpusfull.txt') as fileTrainRaw:
    for line in fileTrainRaw:
        fileTrainRead.append(line)
print(fileTrainRead[0])

thu1 = thulac.thulac(seg_only=True)
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([thu1.cut(fileTrainRead[i][9:-11], text=True)])
    if i % 50000 == 0 :
        print(i)

fileSegWordDonePath ='corpusSegDone.txt'
with open(fileSegWordDonePath,'wb') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0].encode('utf-8'))
        fW.write(b'\n')

def PrintListChinese(list):
    for i in range(len(list)):
        print(list[i],)
PrintListChinese(fileTrainSeg[10])
