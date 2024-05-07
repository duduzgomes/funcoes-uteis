import numpy as np

def cramer(A, B):
    Ax = A.copy()
    Ay = A.copy()
    Az = A.copy()

    for i in range(A.shape[0]):
        Ax[i,0] = B[i]
        Ay[i,1] = B[i]
        # Az[i,2] = B[i]

    dta = round(np.linalg.det(A), 4)
    dtx = round(np.linalg.det(Ax), 4)
    dty = round(np.linalg.det(Ay), 4)
    # dtz = round(np.linalg.det(Az), 1)

    x = dtx / dta
    y = dty / dta

    x= round(x, 4)
    y= round(y, 4)
    # z = dtz / dta

    return [x,y]

