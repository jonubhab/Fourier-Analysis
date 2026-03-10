import numpy as np
from skimage.morphology import skeletonize
from skimage import img_as_bool
import cv2
import Plot as p, Arrangement as a, Extrapolation as e
import csv



inp = input("Input Image path: ")+".png"
img = cv2.imread(inp)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img = cv2.bitwise_not(img)

binary_image = img_as_bool(img > 0.5)

skeleton = skeletonize(binary_image)

sk = np.transpose(np.nonzero(skeleton))


L = [[i[0], i[1]] for i in sk]
A=a.arrange(L)
C=None
clean=False

prompt=1
while True:
    if prompt==1:p.plot(C if clean else A)
    print(f"1) {"Revert to original scan" if clean else "Clean redundant points"}\n"
          f"2) Proceed.")
    prompt=int(input("Choose Your Action: "))
    if prompt==1:
        if clean:
            print("If the cleaning was inefficient, proceed and try removing redundant points manually.")
            L=A
        else:
            if C is None: C=e.clean(A)
            L=C
        clean=not clean
    elif prompt==2:break
    else: print("Invalid Input!")

x,y,t,k=e.extrapolate(L)
o=csv.writer(open(input("output folder path: ")+"/scan.csv",'w'),lineterminator="\n")
o.writerow(['t','x','y',k])
o.writerows(zip(t,x,y))
