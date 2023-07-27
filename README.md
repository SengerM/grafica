# grafica (DEPRECATED)

**DEPRECATED!** The idea was nice, but too much work. I just ended up using Plotly, and put all my utilities together in [plotly_utils](https://github.com/SengerM/plotly_utils).

My personal unified interface for doing plots. The idea is to wrap any plotting package (Matplotlib, Plotly, etc.) with a simple and unique interface, at least for "basic everyday" plots. So then you write one code to plot with any package.

### Maxims

The maxims to guide the development of this package are:

- The interface tries to capture the "concept" of each kind of plot rather than its drawing details.
- The interface is simple and easy without complicated details.
- The user must be able to easily access any property of the figure and/or any trace it contains.

This is an evolution of [myplotlib](https://github.com/SengerM/myplotlib).

## Installation
Just run
```
pip install git+https://github.com/SengerM/grafica
```
You also need to install [Plotly](https://plotly.com/python/) and [Matplotlib](https://matplotlib.org/).

## Usage example

The example below illustrates the philosophy of this package:
```Python
import grafica
import numpy

x = numpy.linspace(0,1)

for package in {'plotly','matplotlib'}: # The same code produces the plot with each package.
	figure = grafica.new(
		plotter_name=package, # Just tell me which package you want to use, I'll take care of the rest.
	)
	figure.scatter(x, x**2) # Draw a scatter plot.

grafica.show() # Show all plots.

```
More examples in the [tests directory](tests/plotter_tests).
