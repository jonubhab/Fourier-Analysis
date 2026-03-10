from math import *

#Main function
def arrange(L):
    L=list(map(Point,L))
    L = [i.copy() for i in sort(L)]
    return L

class Point:
    '''
    Defines a point in plane.
    '''
    def __init__(self,P:tuple):
        self.x=P[0]
        self.y=P[1]

    def dist(self,P):
        '''
        :param P: Point from which distance is to be found.
        :return: Distance between the points.
        '''
        return sqrt((P.x-self.x)**2 + (P.y-self.y)**2)

    def dir(self,P):
        '''
        Returns direction of a point from a point.
        :param P: Point whose direction is to be found
        :return: Direction from x-axis in radians
        '''
        x=P.x-self.x
        y=P.y - self.y
        if x>0: return atan(y/x)%(2*pi)
        elif x<0: return (atan(y/x)+pi)%(2*pi)
        elif y>0: return pi/2
        elif y<0: return 3*pi/2
        else: raise ValueError("Points are same.")

    def copy(self):
        return (self.x,self.y)


def sort(L):
    '''
    Sort the given list of points by finding the closest point to the previous point
    :param L: List of points
    :return: Sorted list
    '''
    if len(L) == 0:
        return []

    S = []  # Initialize sorted list

    # Handle first point
    P = L.pop(0)
    S.append(P)
    idir=0
    # Iteratively process remaining points
    while len(L) > 0:
        # Calculate distance factor for first point
        b=True
        while b:
            b=False
            if len(S) == 1:
                df = 1
            else:
                try:
                    df = (1 + cos(P.dir(L[0]) - idir))**2
                except ValueError:
                    L.pop(0)
                    b=True
                    if len(L)==0: break
        if len(L)==0: break

        if df == 0:
            df = 10 ** -5

        # Set initial reference distance from first point
        s, d = 0, P.dist(L[0]) / df

        # Find the closest point in the remaining list
        for i in range(1, len(L)):
            if len(S)==1:
                df=1
            else:
                try: df = (1 + cos(P.dir(L[i]) - idir))**2
                except ValueError: df=4

            if df == 0:
                df = 10 ** -5

            D = P.dist(L[i]) / df

            if D < d:
                s, d = i, D
                if D == 0.25:
                    break

        # Update direction for next iteration based on closest point found
        try: idir = P.dir(L[s])
        except ValueError:
            L.pop(s)
            continue

        # Remove closest point and add to sorted list
        P = L.pop(s)
        S.append(P)

        # Update direction

    return S


#Test
'''
L={(0.0, 1), (-1, 0.5), (0, 0.5), (2.0, 2), (1, 1.0), (1.0, -1), (-0.5, 0)}
print(arrange(L))
'''