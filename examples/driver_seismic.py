import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import rcParams
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 22, 8
rcParams["figure.subplot.hspace"] = (0.5)
from goph420_lab01 import integration
import os

def load_seismic_data(filename):
    """Loads seismic data from a text file."""
    try:
        sw = np.loadtxt(filename)
        return sw
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data from '{filename}': {e}")
        return None

def plot_raw_data(sw, filename="S wave_plot.png"):
    """Plots the raw seismic data and indicates the integration limit T."""
    t = sw[:,0]
    a = sw[:,1]
    f = a**2

    plt.figure()
    plt.plot(t, a, label="S-wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("S-wave Raw Data")
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


def plot_Swave_T_data_and_integration(sw, filename="S Wave_plot_limit_T.png", plotname="Convergence_Newton_Cotes.png"):
    """Plots the raw seismic data and indicates the integration limit T."""
    t = sw[:,0]
    a = sw[:,1]
    f = a**2
    vt = 0.005*max(abs(a))
    tper = np.where(np.isclose(abs(sw[:,1]),vt,rtol=0.003))

    if tper[0].size > 0:  # Check if any matches were found
        times = sw[tper, 0].flatten() 

    post = np.where(t==times)[0][0]
    t1 = t[0:post]
    fa1 = a[0:post]
    
    plt.figure()
    plt.plot(t1, fa1, label="S-wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("S-wave Data, with limit T")
    #plt.grid(True)
    #plt.axvline(x=T, color='r', linestyle='--', label=f'T = {T:.2f} s')

    plt.legend([f"S-wave Velocity, Period = {times[0]:.2f} s"])
    #plt.legend()

    current_dir = os.path.dirname(__file__)
    figures_dir = os.path.join(current_dir, "..", "figures")
    os.makedirs(figures_dir, exist_ok=True)
    filepath = os.path.join(figures_dir, filename)
    plt.savefig(filepath)
    print(f"Plot saved to: {filepath}")
    print(" T limit calculated [s]: ", times)
    plt.close()

    n = len(t1)

    itr1 = integration.integrate_newton(t1,fa1,"trap",n)/times
    isp1 = integration.integrate_newton(t1,fa1,"simp",n)/times
    print("Integral value of equation (14), step: 0.01, Trapezoidal Rule (Approx. true value):",itr1)
    print("Integral value of equation (14), step: 0.01, Simpson's Rule (Approx. true value):",isp1) 
    

    longT = [2,4,8,10,20]; step = [0.02,0.04,0.08,0.1,0.2]
    longS = [2,4,8,10,20]; errT = [0,0,0,0,0]; errS = [0,0,0,0,0]
    j=0

    for i in longT:
        print("Downsampling:",step[j])
        n1 = int(n/i)
        longT[j] = integration.integrate_newton(t1,fa1,"trap",n1)/times
        print("Integral value of equation (14), Trapezoidal Rule :",longT[j])
        longS[j] = integration.integrate_newton(t1,fa1,"simp",n1)/times
        print("Integral value of equation (14), Simpson's Rule:",longS[j]) 
        
        errT[j] = abs((itr1 - longT[j])) 
        errS[j] = abs((isp1 - longS[j]))
        j = j+1

    plt.plot(step, errT, 'o-', label="Trapezoidal rule ")
    plt.plot(step, errS, 's-', label="Simpson Rule")
    plt.yscale('log')
    plt.xscale('log')


    plt.xlabel("Step_size")
    plt.ylabel("Absolute Error")
    plt.title("Convergence of Newton Cotes Method")
    
    plt.legend()

    current_dir = os.path.dirname(__file__)
    figures_dir = os.path.join(current_dir, "..", "figures")
    os.makedirs(figures_dir, exist_ok=True)
    filepath = os.path.join(figures_dir, plotname)
    plt.savefig(filepath)
    print(f"Plot saved to: {filepath}")
    #print(" T limit calculated [s]: ", times)
    plt.close()
    


if __name__ == "__main__":
    
    current_dir = os.path.dirname(__file__)
    data_file = os.path.join(current_dir, "s_wave_data.txt")
    seismic_data = load_seismic_data(data_file)
    plot_name = "S_wave.png"

    plot_raw_data(seismic_data,filename=f"S wave_plot.png")
    plot_Swave_T_data_and_integration(seismic_data,filename=f"S Wave_plot_limit_T.png", plotname=f"Convergence_Newton_Cotes.png")

    




    