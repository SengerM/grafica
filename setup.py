import setuptools

setuptools.setup(
	name = "grafica",
	version = "0",
	author = "Matias H. Senger",
	author_email = "m.senger@hotmail.com",
	description = "A unified plotting interface to make plots with any package",
	url = "https://github.com/SengerM",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_data = {'': [os.path.join(dp, f) for dp, dn, filenames in os.walk(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)),'PyticularsTCT'),'ximc')) for f in filenames]}, # This is for including all the files in the installation
)
