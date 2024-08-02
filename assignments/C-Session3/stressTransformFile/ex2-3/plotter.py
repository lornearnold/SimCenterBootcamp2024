import sys
import matplotlib.pyplot as plt
import numpy as np

try:
    data = np.genfromtxt('./list.csv',delimiter=',')
except:
    print("Could not find file: 'list.csv'")
    sys.exit(-1)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(data[:,1],data[:,3], label="Mohr's circle")
ax1.set_xlabel('$\\sigma_x$')
ax1.set_ylabel('$\\tau_{xy}$')
ax1.grid(True)
ax2.axis('equal')

ax2.plot(data[:,0],data[:,1], label="$\\sigma_x$")
ax2.set_xlabel('$\\theta$')
ax2.set_ylabel('$\\sigma_x$')
ax2.grid(True)

ax3.plot(data[:,0],data[:,2], label="$\\sigma_y$")
ax3.set_xlabel('$\\theta$')
ax3.set_ylabel('$\\sigma_y$')
ax3.grid(True)

ax4.plot(data[:,0],data[:,3], label="$\\tau_{xy}$")
ax4.set_xlabel('$\\theta$')
ax4.set_ylabel('$\\tau_{xy}$')
ax4.grid(True)
plt.show()
