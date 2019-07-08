import difflib
import sys
raw = open('D:\Data\\big2data\paipai-master\cp\\1.data','rb').readlines()
new = open('D:\Data\\big2data\paipai-master\cp\\2.data', 'rb').readlines()
lraw = []
lnew = []
for l in raw:
    lraw.append(l)
for l in new:
    lnew.append(l)
print(len(lraw))
print(len(lnew))
for i in range (len(new)):
    if lraw[i]==lnew[i]:
        print('Yes')
    else:
        print('raw:',lraw[i])
        print('new:',lnew[i])

