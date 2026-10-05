from typing import NamedTuple, Tuple

Polygon = NamedTuple("Polygon", 
                      centre=Tuple, 
                      radius=float, 
                      sides=int,
                      rotation=float,
                      color=str)