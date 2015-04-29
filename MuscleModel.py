# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:12:28 2015

@author: Palo
"""
from pylab import *;
import random;

l = 0; # length contracted (nm)
t = 0; # time (s)
#v = 0; # contraction speed (nm/s)
f = 0; # Force of contraction (pN)
n = 10000; #myosin heads
alpha = 14; #prob attach/t, s^-1
beta = 126; #prob detach/t, s^-1
#A = 5; # displacement of each myosin head (nm)
dt = 0.01/(alpha+beta); # time step (s)
dx = 0; # movement of head (nm)
tEnd = 3000; # Simulation duration (iterations)
a = [0]*n; # stores state of each myosin head (1 attached, 0 detached)
x = [0]*n; # stores position of each myosin head (nm)
k = 1; # Constant used in calculation of force (assume Hooke model, F=kx)

T = [0]; #stores time vector
F = [0]; #stores fraction of fibers attached
TF = [0]; #stores total force exerted by all fibers

def vel(time):
    v = 500;
    #if (time>1000):
    #    v = 500; # nm/s
    return v;

def force(d):
    f = k*d;    
    return f;

def run():
    for j in range(1,tEnd):                 #main loop. For every second...
        t = j*dt;                           #set time
        dx = vel(t)*dt;                     #set head movement
    
        for i in range(1,n):                #for every head...
            if(a[i] == 1):                  #if head is attached,
                x[i] = x[i]+dx;             #move the head.
                if (random.random() < beta*dt):   #If head detaches,
                    a[i]=0;                 #Set head to detached
                    x[i]=0;                 #Set movement to 0.
            elif j>700 and j<(tEnd-700):                          #Else if head detached and inside stimulus region 1/3 of simulation time:                               #If head was detached
                if (random.random() < alpha*dt):    #If head attaches,
                    a[i]=1;                  #Set head to attached
                    x[i]=dx;                 #Move head
        
        l = sum(x);                         #calculates movement in this iteration
        f = float(sum(a))/n;                #Calculates fraction of heads attached in this iteration
        T.append(t);                        #Add this time to time vector
        F.append(f);                   #Add this time's fraction of myosin heads to fraction vector
        TF.append(force(l));           #Add this time's total force to total force vector

def graph():     #Graphs:
    plot(T,F, 'r');
    xlabel('Time (s)');
    ylabel('Fraction of myosin heads attached');
    show();
    
    plot(T,TF, 'r');
    xlabel('Time (s)');
    ylabel('Total force exerted (pN)');
    show();

print("Thinking... muscling muscle...");
run();
print("graphing");
graph();
print("Done!");