import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# from AQI_plot import rgb


rgb = ([0, 121, 126], [5, 154, 99], [132, 188, 79], [255, 221, 53],
       [255, 184, 46], [254, 150, 51], [228, 73, 51], [200, 1, 58],
       [148, 2, 101], [120, 0, 62], [79, 0, 24])  # colour map
rgb = np.array(rgb)/255.0
cmap = mpl.colors.ListedColormap(rgb)
fig, ax = plt.subplots(figsize=(10, 1))
fig.subplots_adjust(bottom=0.5)
bounds = [25, 50, 75, 100, 125, 150, 175, 200, 300, 400]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='both')
cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                norm=norm,
                                orientation='horizontal',
                                spacing='proportional')
# cb2.set_label("Discrete intervals with extend='both' keyword")
plt.plot(np.arange(0, 10, 1))
if __name__ == '__main__':
    plt.show()
