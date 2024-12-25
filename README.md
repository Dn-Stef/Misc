<h1><p align="center">Miscellaneous</p></h1>
This repository contains various small and diverse Python projects. Each project includes a brief description of the code, along with a list of requirements needed to run it.

---
### PLA.py
This script extracts data from the NASA Exoplanet Archive, where planets were selected at random, each associated with a single solution. A solution represents a set of parameters derived from the data, with multiple solutions possible depending on observation methods and data quality. The analysis includes exploring relationships between planetary mass, radius, and equilibrium temperature through scatter plots and linear regressions. Despite weak correlations between mass and the other parameters, linear regressions for mass vs. radius ($R^2=0.15$) and mass vs. equilibrium temperature ($R^2=0.09$) indicate poor fits, suggesting that a linear model is not appropriate. These results point to the need for more complex models or additional variables to better explain planetary mass variations.

Requirements:
```
pandas 2.1.0
dataclasses 0.8
matplotlib 3.8.0
seaborn 0.13.2
scikit-learn 1.5.1
```

$${\color{red}Note:  \space The  \space  NASAPS201224.xlsx \space file  \space must  \space be  \space downloaded,  \space and  \space the  \space path  \space to  \space this  \space file  \space in  \space the  \space Python  \space script  \space should  \space be  \space updated  \space accordingly.}$$	

---
### pend.py
This is a basic simulation of a simple pendulum, using Pygame for visualization and basic physics principles. The pendulum's motion is influenced by both gravity and air resistance (drag force). The simulation displays the pendulum's motion in real-time, along with dynamic counters showing the pendulum's velocity magnitude in the X and Y axes, as well as the drag force.

Requirements:
```
pygame 2.1.2
```

---
