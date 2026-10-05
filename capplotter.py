from typing import List

import numpy as np
import matplotlib.pyplot as plt


def plot(polygons: List) -> None:

    """
    polygons parameter is a list of Polygon tuples
    """
    
    for p in polygons:

        # theta is an array of angles round the circle/polygon
        # rotation is added to the range of angles
        # number of angles is one more than the number of sides
        theta = np.linspace(0.0 + p.rotation, 2.0*np.pi + p.rotation, p.sides+1)
        
        x = p.radius * np.cos(theta) + p.centre[0]
        y = p.radius * np.sin(theta) + p.centre[1]

        plt.plot(x,
                 y,
                 color=p.color)
        
    plt.gca().set_aspect('equal')
    plt.gca().set_facecolor((0,0,0))  

    plt.show()