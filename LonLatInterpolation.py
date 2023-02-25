import numpy as np
from scipy.interpolate import interp2d
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

lons = [121.39, 126.19 ,130.27, 127.42, 126.14, 125.96, 123.15, 130.5,  129.08, 122.74]
lats = [13.51, 12.02, 13.11, 10.09, 15.33, 14, 10.88, 11.18, 15.78, 15.82]
values = [1.494, 1.934, 2.148, 9.155, 2.221, 8.1, 2.039, 1.916, 3.729, 7.137]
interp_func = interp2d(lons, lats, values, kind='linear')
gridlons = np.linspace(121, 131, 50)
gridlats = np.linspace(10, 16, 70)
interpolated_values = interp_func(gridlons, gridlats)
print(interpolated_values)
grid1, grid2 = np.meshgrid(gridlons, gridlats)
fig = plt.figure()
ax = fig.add_subplot( 1, 1, 1, projection='3d' )
ax.plot_surface( grid1, grid2, interpolated_values)
plt.show()
