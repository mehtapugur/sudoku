########### baştaki sudoku kodu
import numpy as np
import threading

sudoku = [
    [0, 0, 2, 0, 0, 0, 4, 0, 0],
    [0, 6, 0, 7, 0, 5, 0, 8, 0],
    [0, 0, 9, 0, 3, 0, 2, 0, 0],
    [0, 8, 0, 5, 0, 9, 0, 4, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 5, 0, 3, 0, 1, 0, 7, 0],
    [0, 0, 1, 0, 9, 0, 8, 0, 0],
    [0, 3, 0, 1, 0, 2, 0, 9, 0],
    [0, 0, 8, 0, 0, 0, 3, 0, 0]]

sudoku = np.array(sudoku)


def uygun_mu(y, x, n):
    global sudoku
    for i in range(9):
        if sudoku[i][x] == n:
            return False

    for i in range(9):
        if sudoku[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if sudoku[j][i] == n:
                return False
    return True


def solve():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if uygun_mu(i, j, k):
                        sudoku[i][j] = k
                        solve()
                        sudoku[i][j] = 0
                return
    print(sudoku)

solve()


def bir():
    for i in range(1,1000):
        print("aaa ", end="")


def iki():
    for i in range(1,1000):
        print("bbb ", end="")

t1 = threading.Thread(target=bir)
t2 = threading.Thread(target=iki)

t1.start()
t2.start()

############# nisa samurai okutup yazdırma
import numpy as np 

# samourai matrisi tanimlama
samourai = np.zeros((21,21))

#print(samourai)

#txt dosyasini okuma modunda acma
file = open("sudoku.txt","r")


for i in range (21):
    v=0
    veri=file.readline()
    for j in range (21):
        if(i<6):                        #ilk 6 satiri txtden cekiyor
            if(j>8 and j<12):
                samourai[i][j]=0    #bosluk
            else:
                if(veri[v]=="*"):
                    samourai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v+1
                else:
                    samourai[i][j]=int(veri[v])
                    v=v+1
        elif(i>5 and i<9):              # 7. 8. 9. satirlari cekiyor
            if(veri[v]=='*'):
                samourai[i][j]=0
                v=v+1
            elif(veri[v]=="\n"):
                v=v
            else:
                samourai[i][j]=int(veri[v])
                v=v+1
        elif(i>8 and i<12):             #9 10 11. satirlar 
            if(j<6 or j>14):
                samourai[i][j]=0    #bosluk
            elif(j>5 and j<15):
                if(veri[v]=="*"):
                    samourai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v+1
                else:
                    samourai[i][j]=int(veri[v])
                    v=v+1
        elif(i>11 and i<15):            #12 13 14. satirlar
            if(veri[v]=='*'):
                samourai[i][j]=0
                v=v+1
            elif(veri[v]=="\n"):
                v=v
            else:
                samourai[i][j]=int(veri[v])
                v=v+1          
        elif(i>14):                     #son 6 satir 
            if(j>8 and j<12):
                samourai[i][j]=0    #bosluk
            else:
                if(veri[v]=="*"):
                    samourai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v+1
                else:
                    samourai[i][j]=int(veri[v])
                    v=v+1


print(samourai)

file.close()

#################### samurai 1. parçanın çözümü

import numpy as np

# samourai matrisi tanimlama
samourai = np.zeros((21,21))
#samourai = np.array(samourai)

#print(samourai)

#txt dosyasini okuma modunda acma
file = open("sudoku.txt","r")


for i in range (21):
    v=0
    veri=file.readline()
    for j in range (21):
        if(i<6):                        #ilk 6 satiri txtden cekiyor
            if(j>8 and j<12):
                samourai[i][j]=0    #bosluk
            else:
                if(veri[v]=="*"):
                    samourai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v+1
                else:
                    samourai[i][j]=int(veri[v])
                    v=v+1
        elif(i>5 and i<9):              # 7. 8. 9. satirlari cekiyor
            if(veri[v]=='*'):
                samourai[i][j]=0
                v=v+1
            elif(veri[v]=="\n"):
                v=v
            else:
                samourai[i][j]=int(veri[v])
                v=v+1
        elif(i>8 and i<12):             #9 10 11. satirlar
            if(j<6 or j>14):
                samourai[i][j]=0    #bosluk
            elif(j>5 and j<15):
                if(veri[v]=="*"):
                    samourai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v+1
                else:
                    samourai[i][j]=int(veri[v])
                    v=v+1
        elif(i>11 and i<15):            #12 13 14. satirlar
            if(veri[v]=='*'):
                samourai[i][j]=0
                v=v+1
            elif(veri[v]=="\n"):
                v=v
            else:
                samourai[i][j]=int(veri[v])
                v=v+1
        elif(i>14):                     #son 6 satir
            if(j>8 and j<12):
                samourai[i][j]=0    #bosluk
            else:
                if(veri[v]=="*"):
                    samourai[i][j]=0
                    v=v+1
                elif(veri[v]=="\n"):
                    v=v+1
                else:
                    samourai[i][j]=int(veri[v])
                    v=v+1


print(samourai)
print("\n\n")
print(samourai[0][18])
print(samourai[2][18])

def uygun_mu(y, x, n):
    global samourai
    for i in range(9):
        if samourai[i][x] == n:
            return False

    for i in range(9):
        if samourai[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if samourai[j][i] == n:
                return False
    return True


def solve():
    global samourai
    for i in range(9):
        for j in range(9):
            if samourai[i][j] == 0:
                for k in range(1, 10):
                    if uygun_mu(i, j, k):
                        samourai[i][j] = k
                        solve()
                        samourai[i][j] = 0
                return
    print(samourai)

solve()

file.close()


#################### okuma yazma

import numpy as np

# samorai matrisi tanimlama

samurai = np.zeros((21, 21))

#samurai = np.array(samourai)

#print(samurai)

#txt dosyasini okuma modunda acma
file = open("sudoku.txt", "r+")
fileYaz = open("sudokum.txt", "r+")
#fileYaz.close()

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

def dosyaya_yazdir(arr):
    fileYaz.seek(0)
    for i in range(9):
        data = fileYaz.readline()
        for j in range(9):
            fileYaz.write(str(int(arr[i][j])))
            fileYaz.write(" ")
            #data[j] = arr[i][j]
        fileYaz.write("\n")
    fileYaz.close()

def dosyaya_yazdir2():
    fileYaz = open("sudokum.txt", "r+")
    fileYaz.seek(0)
    for i in range(9):
        data = fileYaz.readline()
        for j in range(9, 18):
            fileYaz.write("a")
            fileYaz.write(" ")
            #data[j] = arr[i][j]
        fileYaz.write("\n")

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
    #yaz(samurai)


def yaz(arr):
    global samurai
    for i in range(9):
        for j in range(9):
            samurai[i][j] = arr[i][j]
    print("bu arr: \n", arr)
    return samurai



print("solve:\n")
solve()

dosyaya_yazdir2()

print("en dışta:\n", samurai)

file.close()
#fileYaz.close()
