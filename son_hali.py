import numpy as np
import os

# samorai matrisi tanimlama

samurai = np.zeros((21, 21))
dizi_bir = np.zeros((9, 9))
dizi_iki = np.zeros((9, 9))
#samurai = np.array(samourai)

#print(samurai)

#txt dosyasini okuma modunda acma
file = open("sudoku.txt", "r+")
fileBir = open("txt\\bir.txt", "a+")
fileIki = open("txt\\iki.txt", "a+")
fileUc = open("txt\\uc.txt", "a+")
fileDort = open("txt\\dort.txt", "a+")
fileBes = open("txt\\bes.txt", "a+")
#fileYaz.close()

a = 0
b = 0
c = 0
d = 0
e = 0

def dosya_oku():
    for i in range(21):
        v = 0
        veri = file.readline()
        for j in range(21):
            if(i<6):                        #ilk 6 satiri txtden cekiyor
                if(j>8 and j<12):
                    samurai[i][j]=0    #bosluk
                else:
                    if(veri[v] == "*"):
                        samurai[i][j]=0
                        v=v+1
                    elif(veri[v]=="\n"):
                        v=v+1
                    else:
                        samurai[i][j]=int(veri[v])
                        v=v+1
            elif(i>5 and i<9):              # 7. 8. 9. satirlari cekiyor
                if(veri[v]=='*'):
                    samurai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v
                else:
                    samurai[i][j]=int(veri[v])
                    v=v+1
            elif(i>8 and i<12):             #9 10 11. satirlar
                if(j<6 or j>14):
                    samurai[i][j]=0    #bosluk
                elif(j>5 and j<15):
                    if(veri[v]=="*"):
                        samurai[i][j]=0
                        v=v+1
                    elif(veri[v]=="\n"):
                        v=v+1
                    else:
                        samurai[i][j]=int(veri[v])
                        v=v+1
            elif(i>11 and i<15):            #12 13 14. satirlar
                if(veri[v]=='*'):
                    samurai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v
                else:
                    samurai[i][j]=int(veri[v])
                    v=v+1
            elif(i>14):                     #son 6 satir
                if(j>8 and j<12):
                    samurai[i][j]=0    #bosluk
                else:
                    if(veri[v]=="*"):
                        samurai[i][j]=0
                        v=v+1
                    elif(veri[v]=="\n"):
                        v=v+1
                    else:
                        samurai[i][j]=int(veri[v])
                        v=v+1

dosya_oku()

def dosya_oku1():
    for i in range(9):
        #v = 0
        veri = fileBir.readline()
        for j in range(9):
            dizi_bir[i][j] = int(veri[j])


def dosya_oku2():
    for i in range(9):
        #v = 0
        veri = fileIki.readline()
        for j in range(9):
            dizi_iki[i][j] = int(veri[j])


def dosyaya_yazdir(arr):
    fileBir = open("txt\\bir.txt", "a+")
    fileBir.seek(0)
    for i in range(9):
        data = fileBir.readline()
        for j in range(9):
            fileBir.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileBir.write("\n")
    fileBir.close()

def dosyaya_yazdir2(arr):
    #fileIki = open("sudokum.txt", "r+")
    fileIki = open("txt\\iki.txt", "a+")
    fileIki.seek(0)
    for i in range(9):
        data = fileIki.readline()
        for j in range(12, 21):
            fileIki.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileIki.write("\n")
    fileIki.close()

def dosyaya_yazdir3(arr):
    fileUc.seek(0)
    for i in range(12,21):
        data = fileUc.readline()
        for j in range(9):
            fileUc.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileUc.write("\n")

def dosyaya_yazdir4(arr):
    fileDort.seek(0)
    for i in range(12, 21):
        data = fileDort.readline()
        for j in range(12, 21):
            fileDort.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileDort.write("\n")

def dosyaya_yazdir5(arr):
    fileBes.seek(0)
    for i in range(6, 15):
        data = fileBes.readline()
        for j in range(6, 15):
            fileBes.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileBes.write("\n")

print(samurai)
print("\n\n")
print(samurai[0][18])
print(samurai[2][18])
print("\n\n")

def uygun_mu(y, x, n):
    global samurai
    #nonlocal samourai
    for i in range(9):
        if samurai[i][x] == n:
            return False

    for i in range(9):
        if samurai[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if samurai[j][i] == n:
                return False
    return True

def solve():
    global a
    if (a == 0):
        global samurai
        for i in range(9):
            for j in range(9):
                if samurai[i][j] == 0:
                    for k in range(1, 10):
                        if uygun_mu(i, j, k):
                            samurai[i][j] = k
                            solve()
                            samurai[i][j] = 0
                    return
        print(samurai)
        dosyaya_yazdir(samurai)
        a = a + 1
        #yaz(samurai)

def uygun_mu_iki(y, x, n):
    global samurai
    for i in range(9):
        if samurai[i][x] == n:
            return False

    for i in range(12,21):
        if samurai[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if samurai[j][i] == n:
                return False
    return True

def solve_iki():
    global b
    if (b == 0):
        global samurai
        for i in range(9):
            for j in range(12,21):
                if samurai[i][j] == 0:
                    for k in range(1, 10):
                        if uygun_mu_iki(i, j, k):
                            samurai[i][j] = k
                            solve_iki()
                            samurai[i][j] = 0
                    return
        print(samurai)
        dosyaya_yazdir2(samurai)
        b = b + 1

def uygun_mu_uc(y, x, n):
    global samurai
    for i in range(12,21):
        if samurai[i][x] == n:
            return False

    for i in range(9):
        if samurai[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if samurai[j][i] == n:
                return False
    return True

def solve_uc():
    global c
    if (c == 0):
        global samurai
        for i in range(12, 21):
            for j in range(9):
                if samurai[i][j] == 0:
                    for k in range(1, 10):
                        if uygun_mu_uc(i, j, k):
                            samurai[i][j] = k
                            solve_uc()
                            samurai[i][j] = 0
                    return
        print(samurai)
        dosyaya_yazdir3(samurai)
        c = c + 1

def uygun_mu_dort(y, x, n):
    global samurai
    for i in range(12,21):
        if samurai[i][x] == n:
            return False

    for i in range(12,21):
        if samurai[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if samurai[j][i] == n:
                return False
    return True

def solve_dort():
    global d
    if (d == 0):
        global samurai
        for i in range(12, 21):
            for j in range(12, 21):
                if samurai[i][j] == 0:
                    for k in range(1, 10):
                        if uygun_mu_dort(i, j, k):
                            samurai[i][j] = k
                            solve_dort()
                            samurai[i][j] = 0
                    #print("samurai[", i, "][", j, "] koordinatına ", k, " eklendi\n")
                    return
        #print("samurai[", i, "][", j, "] koordinatına ", k, " eklendi:\n", samurai)
        print(samurai)
        dosyaya_yazdir4(samurai)
        d = d + 1

# i     j      k
def uygun_mu_bes(y, x, n):
    global samurai
    for i in range(6, 15):
        if samurai[i][x] == n:
            return False

    for i in range(6,15):
        if samurai[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if samurai[j][i] == n:
                return False
    return True

def solve_bes():
        global e
        if(e == 0):
            global samurai
            for i in range(6, 15):
                for j in range(6, 15):
                    if samurai[i][j] == 0:
                        for k in range(1, 10):
                            if uygun_mu_bes(i, j, k):
                                samurai[i][j] = k
                                solve_bes()
                                samurai[i][j] = 0
                        return
            print(samurai)
            dosyaya_yazdir5(samurai)
            e = e + 1



def yaz(arr):
    global samurai
    for i in range(9):
        for j in range(9):
            samurai[i][j] = arr[i][j]
    print("bu arr: \n", arr)
    return samurai

print("solve:\n")
solve()
print("solve2:\n")
solve_iki()
print("solve3:\n")
solve_uc()
print("solve4:\n")
solve_dort()
print("solve5:\n")
solve_bes()
#dosyaya_yazdir2()

print("en dışta:\n", samurai)

print("*********************************\n")
def dosya_sil():
    if os.path.exists("txt\\bir.txt"):
        os.remove("txt\\bir.txt")
    else:
        print("Dosya mevcut değil")

#dosya_sil()
print("dosya2 ve sam \n")
dosya_oku2()
print(sam)


print("dosya1 ve dizi \n")
dosya_oku1()
print(dizi)

def samurai_olustur():
    fileBir.seek(0)


file.close()
#fileYaz.close()
fileUc.close()
fileDort.close()
fileBes.close()
