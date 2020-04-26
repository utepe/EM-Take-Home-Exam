"""
Note: if you do not have the matplotlib or numpy APIs installed
In the command prompt of this folder directory, type:
pip install -r requirements.txt
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

'''
Program which solves for Inductance, and Capacitance of a Coaxial Cable
Author: Uygur Tepe
Student ID: 105006877
'''

mu = (4*m.pi*1e-7)      #value of Mu
ep = (1e-9)/(36*m.pi)   #value of Eplison

def COAX_C(l, b_div_a):
    '''Calculates the capacitance of the coaxial cable
    
    Args:
        l (float):length of coaxial cable
        b_div_a (array-like): ratio of b/a ranging from 0.1 to 10

    Returns:
        float: a float of the calculated capactiance at the current length, and b/a ratio
    '''
    # equation of the capacitance of the coaxial cable
    return (2*m.pi*ep*l)/(np.log(b_div_a))  #eqaution of the capacitance of the coaxial cable

def COAX_L_ext(l, b_div_a):
    '''Calculates the external inductance of the coaxial cable
    
    Args:
        l (float): length of coaxial cable
        b_div_a (array-like): ratio of b/a ranging from 0.1 to 10

    Returns:
        float: a float of the calculated external inductance at the current length, and b/a ratio
    '''
    # equation of the external inductance of the coaxial cable
    return (mu*l/(2*m.pi))*np.log(b_div_a)  

def COAX_L_in(l):
    '''Calculates the internal inductance of the coaxial cable
    
    Args:
        l (float): length of coaxial cable
    
    Returns:
        float: a float of the calculated internal inductance at the current length, and b/a ratio
    '''
    # equation of the internal inductance of the coaxial cable
    return (mu*l)/(8*m.pi)  

def COAX_L_tot(l, b_div_a):
    '''Calculates the total inductance of the coaxial cable
    
    Args:
        l (float): length of coaxial cable
        b_div_a (array-like): ratio of b/a ranging from 0.1 to 10
    
    Returns:
    float: a float of the calculated total inductance at the current length, and b/a ratio
    '''
    # equation of the total inductance of the coaxial cable
    # calls both external and interal inductance functions and adds them together
    L_tot = COAX_L_ext(l, b_div_a) + COAX_L_in(l)   
    return L_tot

def constLengthPlot():
    '''
    Creates plots for internal inductance, capacitance, as a function of b/a
    Using a constant length of 1
    Graphically proves L_ext*Cap == Mu*Ep
    ''' 
    
    # creating subplot so all graphs display on the same window
    fig, a = plt.subplots(2,2)       
    
    # creating an array of equally spaced elemnts for the range of 1.1 <= b/a <= 10    
    b_div_a = np.arange(1.1, 10.1, 0.1)
    
    # setting length of cable to 1
    # therefore can calculate inductance and capacitance per unit length
    l = 1
    
    # calling COAX_L_ext fucntion to set variable L_ext to the external inductance of the Coax Cable
    L_ext = COAX_L_ext(l, b_div_a)   # External Inductance per Unit Length
    a[0][0].plot(b_div_a, L_ext, color = "blue", label = "External Inductance")
    a[0][0].legend()
    a[0][0].set_title("External Inductance per length of Coaxial Cable")
    a[0][0].set_xlabel("b/a")
    a[0][0].set_ylabel("Inductance per Meter (H/m) (1E-7)")
    a[0][0].grid(True, which = 'both')
    
    # calling COAX_C fucntion to set variable Cap to the Capacitance of the Coax Cable
    Cap = COAX_C(l, b_div_a)     # Capacitance per Unit Length
    a[0][1].plot(b_div_a, Cap, color = "blue", label = "Capacitance")
    a[0][1].legend()
    a[0][1].set_title("Capacitance per legnth of Coaxial Cable")
    a[0][1].set_xlabel("b/a")
    a[0][1].set_ylabel("Capacitance per Meter (F/m) (1E-10)")
    a[0][1].grid(which = 'both')
    
    # multiplying mu and epsilon and filling this values to an array of the length of b/a array
    MuEp = np.full(len(b_div_a), mu*ep)
    a[1][0].plot(b_div_a, MuEp, color = "blue", label = (f"µε = {MuEp[0]}"))
    a[1][0].legend()
    a[1][0].set_title("Value of Mu*Ep")
    a[1][0].set_xlabel("b/a")
    a[1][0].set_ylabel("Mu * Ep (1E-17)")
    a[1][0].grid(which = 'both')
    
    # multiplying external inductance and capacitance and plotting
    a[1][1].plot(b_div_a, L_ext*Cap, color = "blue", label = (f"L_ext*Cap = {L_ext[0]*Cap[0]}"))
    a[1][1].legend()
    a[1][1].set_title("Value of L_ext*Cap")
    a[1][1].set_xlabel("b/a")
    a[1][1].set_ylabel("L_ext * Cap (H*F) (1E-17)")
    a[1][1].grid(which = 'both')
    
    print(f"MuEp = {MuEp[0]}, L_ext*Cap = {L_ext[0]*Cap[0]}")
    print("Therefore, L_ext*Cap == Mu*Ep, proven graphically and analytically")
    
    # showing all plots specifically how L_ext*Cap == Mu*Ep
    plt.show() 
    
def changingLengthsPlot():
    '''
    Creates plots for internal inductance, and capacitance 
    As a function of b/a and as length of the coax cable changes
    '''
    # creating an array of equally spaced elemnts for the range of 1.1 <= b/a <= 10    
    b_div_a = np.arange(1.1, 10.1, 0.1)
    
    # creating subplot so all graphs display on the same window
    fig, a = plt.subplots(2, 1, squeeze = False)
    
    # loop to plot internal and external inductance while length is changing
    for l in np.arange(1.0, 2.0, 0.20):
            
        # calling COAX_L_ext fucntion to set variable L_ext to the external inductance of the Coax Cable
        L_ext = COAX_L_ext(l, b_div_a)   # External Inductance based on length
        a[0][0].plot(b_div_a, L_ext, c = np.random.rand(3, ), label = (f"External Inductance l={l}"))
        a[0][0].legend()
        a[0][0].set_title("External Inductance of Coaxial Cable")
        a[0][0].set_xlabel("b/a")
        a[0][0].set_ylabel("Inductance (H) (1E-7)")
        a[0][0].grid(True, which = 'both')
        
        # calling COAX_C fucntion to set variable Cap to the Capacitance of the Coax Cable
        Cap = COAX_C(l, b_div_a)     # Capacitance based on legnth 
        a[1][0].plot(b_div_a, Cap, c = np.random.rand(3, ), label = (f"External Inductance l={l}"))
        a[1][0].legend()
        a[1][0].set_title("Capacitance of Coaxial Cable")
        a[1][0].set_xlabel("b/a")
        a[1][0].set_ylabel("Capacitance (F) (1E-9)")
        a[1][0].grid(which = 'both')
    
    # showing all plots of varying inductance and capacticance on one graph to show the difference
    plt.show()
    
if __name__ == "__main__":
    constLengthPlot()
    changingLengthsPlot()