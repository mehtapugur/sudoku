# Samurai Sudoku

  - 3. parça

```py
def uygun_mu(y, x, n):
    global samourai
    for i in range(12,21):
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
    for i in range(12,21):
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
```
