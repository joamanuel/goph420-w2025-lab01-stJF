import numpy as np
import matplotlib.pylab as plt
from matplotlib import gridspec
from matplotlib import rcParams
from goph420_lab01 import integration
import os
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 22, 8
rcParams["figure.subplot.hspace"] = (0.5)

def standar_normal(z):
    return (1/np.sqrt(2*np.pi))*np.exp(-0.5*z**2)

def plot_data(comp,err, rre, filename="Gauss_Convergence_Case_01.png", plotname="Gauss_Convergence_Case_02.png" ):
    """Plots the raw seismic data and indicates the integration limit T."""
   
    plt.figure()
    plt.plot(comp, err, label="Gauss_Convergence_Case_01")
    plt.xlabel("Integration Points")
    plt.ylabel("Error_Relative")
    plt.title("Plot Convergence Gauss-Legendre")
    plt.yscale('log')
    plt.xscale('log')
    #plt.grid(True)
    #plt.axvline(x=T, color='r', linestyle='--', label=f'T = {T:.2f} s')
    plt.legend()

    current_dir = os.path.dirname(__file__)
    figures_dir = os.path.join(current_dir, "..", "figures")
    os.makedirs(figures_dir, exist_ok=True)
    filepath = os.path.join(figures_dir, filename)
    plt.savefig(filepath)
    print(f"Plot saved to: {filepath}")
    plt.close()

    plt.figure()
    plt.plot(comp, rre, label="Gauss_Convergence_Case_02")
    plt.xlabel("Integration Points")
    plt.ylabel("Error_Relative")
    plt.title("Plot Convergence Gauss-Legendre")
    plt.yscale('log')
    plt.xscale('log')
    #plt.grid(True)
    #plt.axvline(x=T, color='r', linestyle='--', label=f'T = {T:.2f} s')
    plt.legend()

    current_dir = os.path.dirname(__file__)
    figures_dir = os.path.join(current_dir, "..", "figures")
    os.makedirs(figures_dir, exist_ok=True)
    filepath = os.path.join(figures_dir, plotname)
    plt.savefig(filepath)
    print(f"Plot saved to: {filepath}")
    plt.close()


if __name__ == "__main__":
    mean = 1.5
    sigma = 0.5
    mag = 4

    z_high = (mag - mean)/sigma
    z_low = 0                 # consider 9 as a larger number (inf) for an event

    lims1 = [z_low,z_high]
    ntps = 5

    prob_results = np.abs(0.5 - integration.integrate_gauss(standar_normal,lims1,ntps))
    print(f"Seismic event probability >= 4 : {prob_results:.8f}")


    # For a measured distance with mean L=10.28m and standar error delta_L= 0.05 m, 
    # estimate the probability that the rule value is between 10.25 and 10.35m

    mean = 10.28
    sigma = 0.05
    low = 10.25; high = 10.35

    z_low1 = (low-mean)/sigma
    z_high1 = (high-mean)/sigma

    lims21 = [0,z_low1]
    lims22 = [0,z_high1]
    ntps = 5

    prob_results1 = 2*(np.abs(integration.integrate_gauss(standar_normal,lims22,ntps)) - np.abs(integration.integrate_gauss(standar_normal,lims21,ntps)))
    print(f"Probability event between 10.25 and 10.35 : {prob_results1:.8f} ")

    compl = [1,2,3,4,5] 
    converg2 = [0,0,0,0,0]; converg1 = [0,0,0,0,0] 
    err1 = [0,0,0,0,0]; err2 = [0,0,0,0,0] 

    for i in compl:
        converg1[i-1] = np.abs(0.5 - integration.integrate_gauss(standar_normal,lims1,i)) 
        print("Number of integration point:", i)
        print("Value of aproximation of integral Case 01:",converg1[i-1])
        converg2[i-1] =  2*(np.abs(integration.integrate_gauss(standar_normal,lims22,i)) - np.abs(integration.integrate_gauss(standar_normal,lims21,i)))
        print("Value of aproximation of integral Case 01:",converg2[i-1])
        if i == compl[-1]:
            for i in range(ntps-1):
                err1[i] = converg1[i+1] - converg1[i]
                err2[i] = converg2[i+1] - converg2[i]

    err1[4] = converg1[4]-converg1[3]
    err2[4] = converg2[4]-converg2[3]
    plot_data(compl,converg1, converg1, filename=f"Gauss_Convergence_Case_01.png", plotname=f"Gauss_Convergence_Case_02.png")
    #plot_data(compl,err1, err2, filename=f"Gauss_Convergence_Case_01.png", plotname=f"Gauss_Convergence_Case_02.png")
    
    #plot_data(comp1,err2, filename=f"Gauss_Convergence_Case_02.png")  
    
    

    

    