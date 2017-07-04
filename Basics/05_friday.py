# Purpose: learn how to use multiple loops


def year():
    # prints out every friday in the year if the first was 3.1.
    
    k = 1
    var = 0

    while k <= 12:

        n = 31
        if k == 2:
            n -= 3
        if k == 4:
            n -= 1
        if k == 6:
            n -= 1
        if k == 9:
            n -= 1
        if k == 11:
            n -= 1

        for p in range(1, n + 1):

            if k == 1 and p < 4:
                if p == 3:
                    var += 7
                    print(p, k, "", sep=".")
            else:
                var += 1
                if var % 7 == 0:
                    print(p, k, "", sep=".")
        else:
            k += 1

year()