import numpy as np

r = 1

with open("test.txt", "w") as f:
    for n in range(15):
        # write a list in the file
        f.write("\n\n")
        s = 0
        if n % 2 == 1:
            l = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if not (i - 1 * n // 2 == 0 and j - 1 * n // 2 == 0):
                        r = 1 / (2 * abs(i - 1 * n // 2) + 2 * abs(j - 1 * n // 2))
                    else:
                        r = 1
                    l[i][j] = r
                    f.write(f"{round(l[i][j], 3)} ")
                s += sum(l[i])
                f.write(f' | {sum(l[i])}\n')
            f.write(f'-------{s}-------')
        else:
            l = np.zeros((n+1, n+1))
            for i in range(n + 1):
                for j in range(n + 1):
                    if not ((i - 1 * n // 2 == 0) or (j - 1 * n // 2 == 0)):
                        r = 1 / (abs(i - 1 * n // 2) + abs(j - 1 * n // 2))
                        l[i][j] = r
                        f.write(f"{round(l[i][j], 3)} ")
                if not ((i - 1 * n // 2 == 0) or (j - 1 * n // 2 == 0)):
                    s += sum(l[i])
                    f.write(f' | {sum(l[i])}\n')
            print(l)
            # np.delete(np.delete(l, np.s_[l.shape[0] // 2], 1), l.shape[0] // 2, 0)
            f.write(f'-------{s}-------')
