def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a ,c))
        hanoi(n-1, b, a, c)

## 0 plate >> 0 step
hanoi(0, "A","B","C")

## 2 plates >> 3 steps
hanoi(2, "A","B","C")

## 3 plates >> 7 steps
hanoi(3, "A","B","C")


