# from https://stackoverflow.com/questions/12643079/b%C3%A9zier-curve-fitting-with-scipy

import random

import numpy as np
from scipy.misc import comb
from tqdm import tqdm 

def bernstein_poly(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i


def bezier_curve(points, nTimes=1000):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1], 
                 [2,3], 
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000

        See http://processingjs.nihongoresources.com/bezierinfo/
    """

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals

def line_line_intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    """
    https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    Line 1 point 1 = (x1,y1)
    Line 1 point 2 = (x2,y2)
    Line 2 point 1 = (x3,y3)
    Line 2 point 2 = (x4,y4)
    """
    intersection_x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    intersection_y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    return intersection_x,intersection_y

def make_squiggle(plotit=False):
    if plotit:
        from matplotlib import pyplot as plt
    # np.random.seed(8)
    all_xs = []
    all_ys = []
    lastPoint = None
    for i in range(5):
        points = np.random.rand(4,2)*200
        if lastPoint is not None:
            points[0] = lastPoint
        xvals, yvals = bezier_curve(points, nTimes=50)
        all_xs += list(reversed(xvals))
        all_ys += list(reversed(yvals))
        lastPoint = points[-1]
    if plotit:
        # plt.scatter(all_xs, all_ys,c=list(range(len(all_xs))))
        plt.plot(all_xs,all_ys)

    num = 0
    for i, _ in enumerate(all_xs):
        if i < 2:
            continue
        for j, _ in enumerate(all_xs):
            if j<=i: 
                continue
            x1 = all_xs[i-1]
            y1 = all_ys[i-1]
            x2 = all_xs[i]
            y2 = all_ys[i]
            x3 = all_xs[j-1]
            y3 = all_ys[j-1]
            x4 = all_xs[j]
            y4 = all_ys[j]
            intersection_x,intersection_y = line_line_intersection(x1,y1,x2,y2,x3,y3,x4,y4)
            minx = x1
            maxx = x2
            if x2 < x1:
                minx = x2
                maxx = x1
            if not (intersection_x > minx and intersection_x < maxx):
                continue
            miny = y1 
            maxy = y2
            if y2 < y1:
                miny = y2
                maxy = y1
            if not (intersection_y > miny and intersection_y < maxy):
                continue
            minx = x3
            maxx = x4
            if x4 < x3:
                minx = x4
                maxx = x3
            if not (intersection_x > minx and intersection_x < maxx):
                continue
            miny = y3 
            maxy = y4
            if y4 < y3:
                miny = y4
                maxy = y3
            if not (intersection_y > miny and intersection_y < maxy):
                continue
            num += 1
            if plotit:
                plt.plot(intersection_x, intersection_y, "ro")
            # if num == 3:
            #     print(i,j,len(all_xs))
            #     plt.plot(intersection_x, intersection_y, "ro")
            #     plt.plot(x1, y1, "go")
            #     plt.plot(x2, y2, "yo")
            #     plt.plot(x3, y3, "mo")
            #     plt.plot(x4, y4, "bo")


    # plt.plot(xpoints, ypoints, "ro")
    # for nr in range(len(points)):
    #     plt.text(points[nr][0], points[nr][1], nr)
    if plotit:
        plt.show()

    return num 
if __name__ == "__main__":
    with open('random.txt','w') as f:
        for i in tqdm(range(3000)):
            f.write('{}\n'.format(make_squiggle() % 6))
    print("""Now run

    dieharder -f random.txt -a""")
