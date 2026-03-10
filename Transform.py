import numpy as np
import math as m
from scipy.optimize import curve_fit as crv
from matplotlib import pyplot as plt

ob=input("Folder path: ").strip()

def txt(filename):
    return np.array(list(map(float, open(f"{ob}/{filename}.txt").read()[1:-1].split(','))))

f=open(ob+"/scan.csv",'r').readlines()
p=f[1:]
p=[list(map(float,i.strip().split(',')[0:3])) for i in p]
x = np.array([i[1] for i in p])
y = np.array([i[2] for i in p])
t = np.array([i[0] for i in p])
k = 2*m.pi/len(t)

def cos(x):
    try:
        return m.cos(x)
    except(TypeError):
        return np.array(list(map(cos, x)))


def sin(x):
    try:
        return m.sin(x)
    except(TypeError):
        return np.array(list(map(sin, x)))


def Re(x, N, *args):
    a0, a, b = float(args[0][0]), list(args[0][1:2 * N:2]), list(args[0][2:2 * N + 1:2])
    s = a0
    for i in range(N):
        s += a[i] * cos((i+1) * k * x) - b[i] * sin((i+1) * k * x)
    return s

def Im(x, N, *args):
    b0, a, b = float(args[0][0]), list(args[0][1:2 * N:2]), list(args[0][2:2 * N + 1:2])
    s = b0
    for i in range(N):
        s += a[i] * sin((i+1) * k * x) + b[i] * cos((i+1) * k * x)
    return s


def transform(n=0, cfx=None, cfy=None):
    if n==0:
        n=int((max(len(cfx),len(cfy))-1)/2)
    if type(cfx) is None:
        cfx, var = crv(lambda x, *coeff: Re(x, n, coeff), t, x, p0=[0] * (2 * n + 1))
    if type(cfy) is None:
        cfy, var = crv(lambda x, *coeff: Im(x, n, coeff), t, y, p0=[0] * (2 * n + 1))

    cfx,cfy=cfx.tolist()[1:],cfy.tolist()[1:]

    if len(cfx) != len(cfy):
        cfx, cfy = equalize(cfx, cfy)

    P = [[], [], [], []]
    for i in range(0, 2 * n, 2):
        P[0].append(cfx[i])
        P[1].append(cfx[i + 1])
        P[2].append(cfy[i])
        P[3].append(cfy[i + 1])

    P = np.array(P)

    Rep = (P[0] + P[2]) / 2
    Imp = (P[1] + P[3]) / 2
    Ren = (P[0] - P[2]) / 2
    Imn = (P[3] - P[1]) / 2

    P = [f"{Rep[i]}{'+' if Imp[i] >= 0 else ''}{Imp[i]}i{',' if i < n - 1 else ']'}" for i in range(n)]
    N = [f"{Ren[i]}{'+' if Imn[i] >= 0 else ''}{Imn[i]}i{',' if i < n - 1 else ']'}" for i in range(n)]
    print('P=[', *P)
    print('N=[', *N)


def equalize(A, B):
    n = max(len(A), len(B))
    a, b = [0] * n, [0] * n
    for i in range(n):
        if i < len(A): a[i] = A[i]
        if i < len(B): b[i] = B[i]
    return a, b


def testx(n):
    cfx, var = crv(lambda x, *coeff: Re(x, n, coeff), t, x, p0=[10] * (2 * n + 1))
    plt.plot(t, x)
    plt.plot(t, Re(t, n, cfx))
    open(f"{ob}/cfx.txt","w").write(str(cfx.tolist()))
    plt.show()


def testy(n):
    cfy, var = crv(lambda x, *coeff: Im(x, n, coeff), t, y, p0=[10] * (2 * n + 1))
    plt.plot(t, y)
    plt.plot(t, Im(t, n, cfy))
    open(f"{ob}/cfy.txt", "w").write(str(cfy.tolist()))
    plt.show()


while True:
    print(f"1) Transform the scan.\n"
          f"2) Proceed with existing coefficients.")
    prompt = int(input("Choose Your Action: "))

    if prompt == 1:
        while True:
            if prompt == 1:
                nx = int(input("Number of terms in fourier series for x-coordinate: "))
                testx(nx)
            print(f"1) Try different number of terms.\n"
                  f"2) Proceed.")
            prompt = int(input("Choose Your Action: "))
            if prompt == 1:
                continue
            elif prompt == 2:
                break
            else:
                print("Invalid Input!")

        prompt = 1
        while True:
            if prompt == 1:
                ny = int(input("Number of terms in fourier series for y-coordinate: "))
                testy(ny)
            print(f"1) Try different number of terms.\n"
                  f"2) Proceed.")
            prompt = int(input("Choose Your Action: "))
            if prompt == 1:
                continue
            elif prompt == 2:
                break
            else:
                print("Invalid Input!")
        break
    elif prompt == 2:
        break
    else:
        print("Invalid Input!")

cfx=txt('cfx')
cfy=txt('cfy')
transform(cfx=cfx,cfy=cfy)
