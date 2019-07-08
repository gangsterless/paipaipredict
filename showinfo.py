with open('D:\Data\\big2data\paipai-master\data\cache\\train.csv') as f:
    i = 0
    l = []
    for line in f:
        print(line)
        l = line.strip('\n').split(',')
        i+=1
        if i>=2:
            break
f.close()