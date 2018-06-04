from visual import *
import numpy as np

#define dimensions for the MeArm
l1 = 17 #length of link 1 in cm
l2 = 5 #length of link 2 in cm
l3=3
l4=3
l5=3
l6=5
l7=3
l8=3
l9=3
l10=5
l11=5

#Create virtual environment:
scene = display(title='Robot movements', width=600, height=600, center=(0,4,0),color=color.white) #set up the scene
#To improve clarity, create a set of x, y and z axis
x_axis= arrow(pos=(0,0,0), axis=(20,0,0), shaftwidth=0.1, headwidth=0.3)
y_axis= arrow(pos=(0,0,0), axis=(0,15,0), shaftwidth=0.1, headwidth=0.3)
pos_x_axis= arrow(pos=(0,0,0), axis=(-15,0,0), shaftwidth=0.1, headwidth=0.3)
pos_y_axis= arrow(pos=(0,0,0), axis=(0,-15,0), shaftwidth=0.1, headwidth=0.3)
pos_z_axis= arrow(pos=(0,0,0), axis=(0,0,-15), shaftwidth=0.1, headwidth=0.3)
neg_z_axis= arrow(pos=(0,0,0), axis=(0,0,15), shaftwidth=0.1, headwidth=0.3)

#Indicators for the target, link 1 and link 2 respectively
fa=sphere(pos=(0,17,0),radius=3)
fa1=points(pos=[(-0,17,0), (0,17,0)], size=50, color=color.red)
l1_ind = arrow(pos=(0,0,0),axis=(0,17,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.red)
l2_ind = arrow(pos=(0,12,0), axis=(5,0,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.green)
l3_ind = arrow(pos=(5,12,0), axis=(0,-3,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.cyan)
l4_ind = arrow(pos=(5,9,0), axis=(0,-3,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.red)
l5_ind = arrow(pos=(5,6,0), axis=(0,-3,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.yellow)
l6_ind = arrow(pos=(0,12,0), axis=(-5,0,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.green)
l7_ind = arrow(pos=(-5,12,0), axis=(0,-3,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.cyan)
l8_ind = arrow(pos=(-5,9,0), axis=(0,-3,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.blue)
l9_ind = arrow(pos=(-5,6,0), axis=(-0,-3,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.yellow)
l10_ind = arrow(pos=(0,0,0), axis=(-5,-5,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.cyan)
l11_ind = arrow(pos=(0,0,0), axis=(5,-5,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.cyan)
l12_ind = arrow(pos=(0,0,0), axis=(0,0,0), shaftwidth=0.8,headlength=1, headwidth=0.8, color=color.yellow)
#indicators
indicator1 = arrow(pos=(0,12,0), axis=(5,-3,0), shaftwidth=0.05, headwidth=0.03, color=color.yellow)
indicator2 = arrow(pos=(0,12,0), axis=(5,-6,0), shaftwidth=0.05, headwidth=0.03, color=color.yellow)
indicator3 = arrow(pos=(0,12,0), axis=(5,-9,0), shaftwidth=0.05, headwidth=0.03, color=color.yellow)
indicator4 = arrow(pos=(0,12,0), axis=(-5,-3,0), shaftwidth=0.05, headwidth=0.03, color=color.yellow)
indicator5 = arrow(pos=(0,12,0), axis=(-5,-6,0), shaftwidth=0.05, headwidth=0.03, color=color.yellow)
indicator6 = arrow(pos=(0,12,0), axis=(-5,-9,0), shaftwidth=0.05, headwidth=0.03, color=color.yellow)
#indicator8 = arrow(pos=(0,12,0), axis=(10,10,0), shaftwidth=0.2, headwidth=0.3, color=color.yellow)

#Labels to improve the visualization of the position of the arm
in_x_plane=arrow(pos=(0,0,0), axis=(15,0,0), shaftwidth=0.1, headwidth=0.1, color=color.orange, opacity=0.3)
in_y_plane=arrow(pos=(0,0,0), axis=(0,15,0), shaftwidth=0.1, headwidth=0.1, color=color.orange, opacity=0.3)
in_z_plane=arrow(pos=(0,0,0), axis=(0,0,15), shaftwidth=0.1, headwidth=0.1, color=color.orange, opacity=0.3)

#Initial position
x=5
y=9
phi=0 #angle for base rotation
clamp = 'Close' #Clamp is close

#now we made an infinite while loop to keep the program running
while (1==1):
    rate(20) #refresh rate required for VPython
    ev = scene.waitfor('keydown')
    if ev.key == 'up':
        y = y+0.25
    elif ev.key == 'down':
        y = y-0.25
    elif ev.key == 'right':
        x = x+0.25
    elif ev.key == 'left':
        x = x-0.25
    elif ev.key == 'a':
        phi = phi-5
        if phi <= -90:
            print 'Minimum angle reached'
            phi = -90
    elif ev.key == 'd':
        phi = phi+5
        if phi >= 90:
            print 'Maximum angle reached'
            phi = 90
    elif ev.key == 'q':
        print 'Going to initial position...'
        x=10
        y=10
        phi=0
    elif ev.key == 'w':
        print 'Opening clamp...'
        clamp = 'Open'
    elif ev.key == 's':
        print 'Closing clamp...'
        clamp = 'Close'

#Calculate the distance to the target and the angle to the x axis
    T = np.sqrt(x*x+y*y) #Distance to target
    if l1+l2<T+0.5: #Loop to prevent targets out of range
        print 'Position cannot be reached, reseting...'
        x=10
        y=10
        T = np.sqrt(x*x+y*y)
    theta = np.arctan2(y,x)

    #Calculate the Area of the triangle using Heron's formula
    s=(l1+l2+T)/2 #Calculate the semiperimeter
    A= np.sqrt(s*(s-l1)*(s-l2)*(s-T)) #Area of the triangle 2-link arm
    
    #Now we calculate the angles
    alpha = np.arcsin((2*A)/(l1*T))
    gamma = np.arcsin((2*A)/(T*l2))
    beta = np.arcsin((2*A)/(l1*l2))
    if beta>0.5:
        beta = np.pi-alpha-gamma     
    ang=3.141592+alpha+theta+beta #Correct angle from the l1 indicator

    #Update the indicators
    indicator1.axis=(x*np.cos(phi*0.01745),y,x*np.sin(phi*0.01745)) #calculate the new axis of the indicator
    l1_ind.axis=(l1*np.cos(alpha+theta)*np.cos(phi*0.01745),l1*np.sin(alpha+theta),l1*np.cos(alpha+theta)*np.sin(phi*0.01745)) #calculate the new axis of l1
    l2_ind.pos=(l1*np.cos(alpha+theta)*np.cos(phi*0.01745),l1*np.sin(alpha+theta),l1*np.cos(alpha+theta)*np.sin(phi*0.01745)) #calculate new origin for l2
    l2_ind.axis=(l2*np.cos(ang)*np.cos(phi*0.01745),l2*np.sin(ang),l2*np.cos(ang)*np.sin(phi*0.01745)) #Calculate new axis for l2
    in_x_plane.pos=(0,0,x*np.sin(phi*0.01745))
    in_y_plane.pos=(x*np.cos(phi*0.01745),0,x*np.sin(phi*0.01745))
    in_z_plane.pos=(x*np.cos(phi*0.01745),0,0)
    in_x_plane.axis=(x*np.cos(phi*0.01745),0,0)
    in_y_plane.axis=(0,y,0)
    in_z_plane.axis=(0,0,x*np.sin(phi*0.01745))


