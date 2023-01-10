# jupyter

## to html


```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)

from IPython.display import HTML
HTML(ani.to_jshtml())
```


## to video

```python
from matplotlib import animation
from IPython.display import HTML

# <insert animation setup code here>

anim = animation.FuncAnimation()  # With arguments of course!
HTML(anim.to_html5_video())
```