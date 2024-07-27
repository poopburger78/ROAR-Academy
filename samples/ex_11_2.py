from matplotlib import image
from matplotlib import pyplot
import os

# Read an image file
path_1 = os.path.dirname(os.path.abspath(__file__))
filename_1 = path_1 + '/' + 'lenna.bmp'
data_1 = image.imread(filename_1)

path_2 = os.path.dirname(os.path.abspath(__file__))
filename_2 = path_2 + '/' + 'flag.jpg'
data_2 = image.imread(filename_2)

# Display image information
# print('Image type is: ', type(data))
# print('Image shape is: ', data.shape)

# Add some color boundaries to modify an image array
plot_data = data_1.copy()
for width in range(data_2.shape[1]):
    for height in range(data_2.shape[0]):
        plot_data[height][width] = data_2[height][width]

# Write the modified images
image.imsave(path_1+'/'+'lenna-mod.jpg', plot_data)

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()