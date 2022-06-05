from ctypes import RTLD_GLOBAL
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# link lengths in mm
a1 = float(input("a1 = ")) # For testing, 150 mm
a2 = float(input("a2 = ")) # For testing, 80 mm
a3 = float(input("a3 = ")) # For testing, 80 mm
a4 = float(input("a4 = ")) # For testing, 80 mm

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)

# link limits converted to meters
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)
lm2 = float(input("lm2 = "))
lm2 = mm_to_meter(lm2)
lm3 = float(input("lm3 = "))
lm3 = mm_to_meter(lm3)

# Create Links
# [robot variable]=DHRobot([RevoluteDH(theta,r/a,alpha,offset)])
Carte_Standard = DHRobot([
    PrismaticDH(0,0,(270/180)*np.pi,a1,qlim=[0,0]),
    PrismaticDH((270/180)*np.pi,0,(270/180)*np.pi,a2,qlim=[0,lm1]),
    PrismaticDH((270/180)*np.pi,0,(90/180)*np.pi,a3,qlim=[0,lm2]),
    PrismaticDH(0,0,0,a4,qlim=[0,lm3])
], name='Cartesian')
print(Carte_Standard)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi


# q Paths
q0 = np.array([0,0,0,0])
q1 = np.array([0,mm_to_meter(float(input("d1 = "))),
                mm_to_meter(float(input("d2 = "))),
                mm_to_meter(float(input("d3 = ")))])
#q2 = np.array([0,mm_to_meter(float(input("d1 = "))),
#                mm_to_meter(float(input("d2 = "))),
#                mm_to_meter(float(input("d3 = ")))])
#q3 = np.array([0,mm_to_meter(float(input("d1 = "))),
#                mm_to_meter(float(input("d2 = "))),
#                mm_to_meter(float(input("d3 = ")))])

#plot scale
x1=-0.3
x2=0.3
y1=-0.3
y2=0.3
z1=-0.3
z2=0.3

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,50)
#traj2 = rtb.jtraj(q1,q2,50)
#traj3 = rtb.jtraj(q2,q3,50)

# for Joint Variable vs Time(s) table
rtb.qplot(traj1.q)

Carte_Standard.plot(traj1.q, limits=[x1,x2,y1,y2,z1,z2], movie='Cartesian1.gif')
#Carte_Standard.plot(traj2.q, limits=[x1,x2,y1,y2,z1,z2], movie='Cartesian2.gif')
#Carte_Standard.plot(traj3.q, limits=[x1,x2,y1,y2,z1,z2], movie='Cartesian3.gif', block= True)

#plot commands
Carte_Standard.teach(jointlabels=1) # for teach