# test_plot.py
import matplotlib.pyplot as plt
import matplotlib

# Print the location of the matplotlibrc file being used
print("Using matplotlibrc file from:", matplotlib.matplotlib_fname())

# Print some key configuration parameters to verify they are set correctly
print("axes.facecolor:", plt.rcParams['axes.facecolor'])
print("figure.facecolor:", plt.rcParams['figure.facecolor'])
print("text.color:", plt.rcParams['text.color'])

# Generate a simple plot
plt.plot([0, 1, 2, 3], [0, 1, 4, 9])
plt.title('Test Plot')
plt.grid(True)
# Display the plot
plt.show()
