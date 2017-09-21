def plot_gen(filename, dim=2, i=1, j=2, show=1, save=0):
	import numpy as np
	import matplotlib.pyplot as plt

	data = np.loadtxt(filename)
	N=data.shape[0];

	print(N)

	x = data[:,i-1]
	y = data[:,j-1]
	colors = data[:,dim]

	fig = plt.figure()

	plt.scatter(x, y, c=colors, marker='o', s=10.0, alpha=0.3)

	plt.xlabel('var-'+str(i), fontsize=18)
	plt.ylabel('var-'+str(j), fontsize=18)
	plt.colorbar()

	if (show == 1):
		plt.show()

	if (save == 1):
		fig.savefig(filename+'.png', dpi=fig.dpi)

	return


