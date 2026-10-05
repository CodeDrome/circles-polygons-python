import numpy as np

import capplotter as capp
import polygon as pg


def main():

    polygons = []
            
    # circle
    polygons.append(pg.Polygon((0,0), 1.0, 360, 0.0, "#FFFFFF"))

    # triangle
    # polygons.append(pg.Polygon((0,0), 1.0, 3, np.pi / 2.0, "#FF0000"))
    
    # square
    polygons.append(pg.Polygon((0,0), 1.0, 4, np.pi / 4.0, "#0000FF"))

    # pentagon
    polygons.append(pg.Polygon((0,0), 1.0, 5, np.pi / 10.0, "#008000"))

    # hexagon
    polygons.append(pg.Polygon((0,0), 1.0, 6, 0.0, "#FF8000"))

    # heptagon
    polygons.append(pg.Polygon((0,0), 1.0, 7, np.pi / 4.5, "#8000FF"))

    # octagon
    polygons.append(pg.Polygon((0,0), 1.0, 8, np.pi / 8, "#0080FF"))
    
    capp.plot(polygons)


if __name__ == "__main__":

    main()