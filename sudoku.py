import numpy as np
import os
import threading
import time

start = time.time()
# samorai matrisi tanimlama
samurai = np.zeros((21, 21))
dizi_bir = np.zeros((9, 9))
dizi_iki = np.zeros((9, 9))
dizi_uc = np.zeros((9, 9))
dizi_dort = np.zeros((9, 9))
dizi_bes = np.zeros((9, 9))

#txt dosyasini okuma modunda acma
file = open("sudoku.txt", "r+")
fileBir = open("txt\\bir.txt", "a+")
fileIki = open("txt\\iki.txt", "a+")
fileUc = open("txt\\uc.txt", "a+")
fileDort = open("txt\\dort.txt", "a+")
fileBes = open("txt\\bes.txt", "a+")
databaseFile = open("database.txt", "a+")

a = 0
b = 0
c = 0
d = 0
e = 0

#sudoku.txt okutup samurai sudoku oluştur
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

def dosya_oku3():
    for i in range(9):
        #v = 0
        veri = fileUc.readline()
        for j in range(9):
            dizi_uc[i][j] = int(veri[j])

def dosya_oku4():
    for i in range(9):
        #v = 0
        veri = fileDort.readline()
        for j in range(9):
            dizi_dort[i][j] = int(veri[j])

def dosya_oku5():
    for i in range(9):
        #v = 0
        veri = fileBes.readline()
        for j in range(9):
            dizi_bes[i][j] = int(veri[j])

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
    fileUc = open("txt\\uc.txt", "a+")
    fileUc.seek(0)
    for i in range(12,21):
        data = fileUc.readline()
        for j in range(9):
            fileUc.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileUc.write("\n")
    fileUc.close()

def dosyaya_yazdir4(arr):
    fileDort = open("txt\\dort.txt", "a+")
    fileDort.seek(0)
    for i in range(12, 21):
        data = fileDort.readline()
        for j in range(12, 21):
            fileDort.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileDort.write("\n")
    fileDort.close()

def dosyaya_yazdir5(arr):
    fileBes = open("txt\\bes.txt", "a+")
    fileBes.seek(0)
    for i in range(6, 15):
        data = fileBes.readline()
        for j in range(6, 15):
            fileBes.write(str(int(arr[i][j])))
            #data[j] = arr[i][j]
        fileBes.write("\n")
    fileBes.close()

print("Samurai Sudoku'nun ilk hali: \n", samurai)
print("\n")

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
    bir_basla = time.time()
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
                            bilgi = "samurai[" + str(i) +"]["+ str(j)  +"] noktasına " + str(k) +" değeri verildi\n"
                            databaseFile.write(bilgi)
                    return
        dosyaya_yazdir(samurai)
        a = a + 1
        bir_bitir = time.time()
        print("Birinci kare çözüldü: ", bir_bitir - bir_basla)
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
    iki_basla = time.time()
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
                            bilgi = "samurai[" + str(i) + "][" + str(j) + "] noktasına " + str(k) + " değeri verildi\n"
                            databaseFile.write(bilgi)
                    return
        dosyaya_yazdir2(samurai)
        b = b + 1
        iki_bitir = time.time()
        print("İkinci kare çözüldü: ", iki_bitir - iki_basla)

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
    uc_basla = time.time()
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
                            bilgi = "samurai[" + str(i) + "][" + str(j) + "] noktasına " + str(k) + " değeri verildi\n"
                            databaseFile.write(bilgi)
                    return
        dosyaya_yazdir3(samurai)
        c = c + 1
        uc_bitir = time.time()
        print("Üçüncü kare çözüldü: ", uc_bitir - uc_basla)

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
    dort_basla = time.time()
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
                            bilgi = "samurai[" + str(i) + "][" + str(j) + "] noktasına " + str(k) + " değeri verildi\n"
                            databaseFile.write(bilgi)
                    return
        dosyaya_yazdir4(samurai)
        d = d + 1
        dort_bitir = time.time()
        print("Dördüncü kare çözüldü: ", dort_bitir - dort_basla)

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
    bes_basla = time.time()
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
                            bilgi = "samurai[" + str(i) + "][" + str(j) + "] noktasına " + str(k) + " değeri verildi\n"
                            databaseFile.write(bilgi)
                    return
        dosyaya_yazdir5(samurai)
        e = e + 1
        bes_bitir = time.time()
        print("Beşinci kare çözüldü: ", bes_bitir - bes_basla)

t1 = threading.Thread(target=solve())
t2 = threading.Thread(target=solve_iki())
t3 = threading.Thread(target=solve_uc())
t4 = threading.Thread(target=solve_dort())
t5 = threading.Thread(target=solve_bes())

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

dosya_oku2()
dosya_oku1()
dosya_oku3()
dosya_oku4()
dosya_oku5()

def samurai_olustur():
    global samurai
    global dizi_bir
    global dizi_iki
    global dizi_uc
    global dizi_dort
    global dizi_bes
    for i in range(21):
        for j in range(21):
            if(i < 6):                        #ilk 6 satir
                if(j > 8 and j < 12):
                    samurai[i][j] = 0     #bosluk
                else:
                    if(j < 9):
                        samurai[i][j] = dizi_bir[i][j]
                    elif(j > 11):
                        samurai[i][j] = dizi_iki[i][j-12]
            elif(i > 5 and i < 9):              # 7. 8. 9. satirlari cekiyor
                if(j < 6):
                    samurai[i][j] = dizi_bir[i][j]
                elif(j > 5 and j < 15):
                    samurai[i][j] = dizi_bes[i-6][j-6]
                else:
                    samurai[i][j] = dizi_iki[i][j-12]
            elif(i > 8 and i < 12):             #9 10 11. satirlar
                if(j < 6 or j > 14):
                    samurai[i][j] = 0    #bosluk
                elif(j > 5 and j < 15):
                    samurai[i][j] = dizi_bes[i-6][j-6]
            elif(i > 11 and i < 15):              # 13 14 15. satirlar
                if(j < 6):
                    samurai[i][j] = dizi_uc[i-12][j]
                elif(j > 5 and j < 15):
                    samurai[i][j] = dizi_bes[i-6][j-6]
                else:
                    samurai[i][j] = dizi_dort[i-12][j-12]
            elif(i > 14):              # 16 - 21 satirlari
                if(j < 9):
                    samurai[i][j] = dizi_uc[i-12][j]
                elif(j > 8 and j < 12):
                    samurai[i][j] = 0
                else:
                    samurai[i][j] = dizi_dort[i-12][j-12]
    print(samurai)

print("\nSamurai Sudoku'nun çözümü: \n")
samurai_olustur()

file.close()
fileUc.close()
fileDort.close()
fileBes.close()
databaseFile.close()
end = time.time()
print("Programın çalışma süresi: ", end - start)