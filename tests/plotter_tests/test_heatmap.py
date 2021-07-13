import unifiedplottinginterface as upi
import numpy as np

x = np.linspace(0,np.pi,99)
y = np.linspace(0,2*np.pi,77)

xx, yy = np.meshgrid(x,y)
zz = np.sin(xx)

fig = upi.manager.new(
	title = 'Basic heatmap plot',
	xlabel = 'x',
	ylabel = 'y',
)
fig.heatmap(
	x = x,
	y = y,
	z = zz,
)

fig = upi.manager.new(
	title = 'Heatmap plot with annotations and alpha',
	xlabel = 'x',
	ylabel = 'y',
)
fig.heatmap(
	x = x,
	y = y,
	z = zz,
	zlabel = 'Temperature (°C)',
	alpha = .5,
)

fig = upi.manager.new(
	title = 'Heatmap plot with logarithmic scale',
	xlabel = 'x',
	ylabel = 'y',
)
fig.heatmap(
	x = x,
	y = y,
	z = zz-.5,
	zlabel = 'Temperature (°C)',
	zscale = 'log',
)

fig = upi.manager.new(
	title = 'Heatmap plot with zlim',
	xlabel = 'x',
	ylabel = 'y',
)
fig.heatmap(
	x = x,
	y = y,
	z = zz,
	zlim = (.5,1.5),
)

for plotter in upi.manager.plotters:
	upi.manager.draw(plotter=plotter)
upi.manager.save(mkdir=True)