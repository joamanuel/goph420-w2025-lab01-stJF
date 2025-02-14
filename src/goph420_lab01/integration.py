import numpy as np


def integrate_newton(x, f, alg,n):
    #Function for estimation of numerical integration using Trapezoidal rule and
    #Simpson's Rule 1/3.

    x = np.asarray(x)
    f = np.asarray(f)
    

    alg = alg.strip().lower()
    if alg == "trap":
        t = ((x[-1] - x[0]) / (n - 1))
        trapI = (t/2)*(f[0] + 2 * sum(f[1:n-1]) + f[-1])
        
        return trapI
        
    elif alg == "simp":
        u = ((x[-1] - x[0]) / (n - 1))/3
        simp13 = u*(f[0] + 4*np.sum(f[1:-1:2]) + 2*np.sum(f[2:-1:2]) + f[-1])
        return simp13
        
                    
    else:
        raise ValueError

    if x.shape != f.shape:
        raise ValuerError("x and f do not haver the same shape")
    if x.ndim != f.ndim:
        raise ValueError("Only 1-dimensional arrays is accepted")



def integrate_gauss(f, lims, ntps):
    #Function for estimation of numerical integration using Gauss-Legendre Quadrature
    
    if not callable(f):
        raise TypeError("F must be callable")

    if len(lims)!=2:
        raise ValueError("lims must have lenght 2")

    try:
        s = float(lims[0])
        d = float(lims[1])
    except ValueError:
        raise ValueError("lims must be convertible to float")

    if ntps not in [1,2,3,4,5]:
        raise ValueError("ntps must be in [1,2,3,4,5]")

    coef,weight = np.polynomial.legendre.leggauss(ntps)
    x_t = 0.5 * (lims[1] - lims[0]) * coef + 0.5 * (lims[1] + lims[0])
    w_t = 0.5 * (lims[1] - lims[0]) * weight
    result = sum(w_t*f(x_t))

    return result
    



