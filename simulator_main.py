import random
import csv
ces = []
serv = []
srS = []
srC = []
result = []


def inp():
    with open('CEs-en.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            cck = row[3]
            if cck >= '3':
                ces.append([row[0], cck])
                if cck >= '4':
                    srC.append([row[0], cck])

    with open('Servants.csv') as cfile:
        rCSV = csv.reader(cfile, delimiter=',')
        for rw in rCSV:
            ck = rw[2]
            if ck >= '3':
                serv.append([rw[0], ck])
                if ck >= '4':
                    srS.append([rw[0], ck])


def summon(sumo):
    result.clear()
    n_roll = sumo
    i = 0
    rs = 0
    chk = True
    summon_all= merge(ces,serv)
    summon_r= merge(srC,srS)
    random.shuffle(summon_all)
    random.shuffle(summon_r)
    while i < n_roll:
        ran = random.choice(list(summon_all))
        result.append(ran)
        i += 1
    if n_roll == 10:
        for h in result:
            if int(h[1]) >= 4:
                chk = False
                rs += 1
        if chk:
            print("\n\nFail Safe", "\n")
            rans = random.choice(list(summon_r))
            ind = random.randint(0, (n_roll - 1))
            print("Adding", rans, "at ", ind, "removing ", result[ind], "\n\n")
            result[ind] = rans
    print(result, "\n Number of SR or SSR are: ", rs, "in ", result.__len__(), "rolls")


def merge(list1, list2):
    return list1+list2


inp()
print("\t\t\t\t\tSummon Simulator")
roll = int(input("Enter number of Rolls:\t"))
while roll > 10:
    summon(10)
    roll = roll - 10
summon(roll)
