from matplotlib import pyplot
from pylab import *
from numpy import *
from itertools import cycle
import matplotlib.colors as clr

# LinearSegmentedColormap создаёт палитру по заданным точкам и заданным цветам
# можете попробовать выбрать другие цвета
pmin = -2.5
pmax = 1.5
qmin = -2
qmax = 2
# пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
# а q меняется в диапазоне от qmin до qmax

ppoints, qpoints = 200, 200
# число точек по горизонтали и вертикали

max_iterations = 300
# максимальное количество итераций

infinity_border = 10
# если ушли на это расстояние, считаем, что ушли на бесконечность
image = zeros( (ppoints, qpoints) )
# image — это двумерный массив, в котором будет записана наша картинка
# по умолчанию он заполнен нулями

p, q = mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)]
# np.mgrid создаёт сетку значений p и q, ppoints*1j здесь означает
# что мы хотим получить ppoints точек — это такая магия

c = p + 1j * q
z = zeros_like( c )


# теперь c и z — это двумерные матрицы



def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=200, infinity_border=10):
	image = np.zeros( (ppoints, qpoints) )
	p, q = np.mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)]
	c = p + 1j * q
	z = np.zeros_like( c )
	for k in range( max_iterations ):
		z = z ** 2 + c
		mask = (np.abs( z ) > infinity_border) & (image == 0)
		image[mask] = 1
		z[mask] = np.nan

	return -image.T

# pmin = -2.5
# pmax = 1.5
# qmin = -2
# qmax = 2

max_frames = 200
max_zoom = 1
i = 95
# p_center, q_center = -0.793191078177363, 0.16093721735804
p_center, q_center = -2.1078177363, 0.16093721735804
# p_center, q_center = -0., 0.
zoom = (i / max_frames * 2) ** 3 * max_zoom + 1
scalefactor = 1 / zoom
pmin_ = (pmin - p_center) * scalefactor + p_center
qmin_ = (qmin - q_center) * scalefactor + q_center
pmax_ = (pmax - p_center) * scalefactor + p_center
qmax_ = (qmax - q_center) * scalefactor + q_center
image = mandelbrot( pmin_, pmax_, 1000, qmin_, qmax_, 1000)


# image = mandelbrot( -2.5, 1.5, 1500, -2.0, 2.0, 1500, infinity_border=50, max_iterations=200 )
xticks( [] )
yticks( [] )
figure( figsize=(10, 10) )

# colorpoints = [(1-(1-q)**4, c) for q, c in zip(np.linspace(0, 1, 20),
#                                                cycle(['#ffff88', '#000000', '#ffaa00',]))]

def clamp(x):
	return max( 0, min( x, 255 ) )


def rgb2hex(r, g, b):
	return ("#{0:02x}{1:02x}{2:02x}".format( clamp( r ), clamp( g ), clamp( b ) ))


colors = []
for i in np.linspace( 0, 255, 255 ):
	colors.append( rgb2hex( int( i ), int( i ), int( i ) ) )

colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip( np.linspace( 0, 1, 255 ),
                                                      colors)]#[::-1] )]

# print(colorpoints)
# cycle(['#ffff88', '#000000',
#        '#ffaa00',]))]


cmap = clr.LinearSegmentedColormap.from_list( 'mycmap',
                                              colorpoints, N=2048 )

show( imshow( image, cmap=cmap, interpolation='none' ) )
savefig( 'example.png' )
