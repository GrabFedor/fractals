import glob
from PIL import Image
from numpy import *
import os

def get_colors_array():
	colors = []

	for i in linspace( 0, 255, 100 ):
		# for i in range( 0, 255, 1 ):
		colors.append( (int( i ), int( i * 2 ), int( i * 4 )) )
	print( colors )
	return colors  # [::-1]


# image = np.zeros( (x_points, y_points) )
def manbrot(pmin, pmax, y_points, x_points, qmin, qmax, max_it=99, inf_board=4):
	img = Image.new( "RGB", (x_points, y_points) )
	colors = get_colors_array()
	print( colors )
	for ip, p in enumerate( linspace( pmin, pmax, x_points ) ):
		for iq, q in enumerate( linspace( qmin, qmax, y_points ) ):
			c = p + 1j * q
			z = 0
			for k in range( max_it ):
				z = z ** 2 + c

				if abs( z ) > inf_board:
					color = (k % 4 * 34, k % 8 * 32, k % 9 * 12)  #(255 // k, 255 // k, 255 // k)
					# Different types of coloring the fractal
					# color = (255 // k , 255 - (255 // k), 255 // k)
					# color = colors[k]
					# print(color)
					# image[ip, iq] = 1
					break
				else:
					color = (0, 33, 55)

			img.putpixel( (ip, iq), color )
		# img.putpixel( (ip, y_points - iq - 1), color )
	return img


max_frames = 200
max_zoom = 300
# I was trying to find another way to zoom, but it was not that good,
# because it is hard to choose a point, where the fractal would be seen good even
# x300 zoomed (or x15000), who knows :)
# max_frames = 200
# max_zoom = 210000
# i = 90
# p_center, q_center = -0.70386998880000, 0.4747055652254
# p_center, q_center = -1.325191078177363, 0.06000721735804

def create_images(i, max_frames, max_zoom):
	if i > max_frames // 2:
		img = Image.open( 'Images4/Mandelbrot{i}.png'.format( i=max_frames - i ) )
		img.save( 'Images4/Mandelbrot{i}.png'.format( i=i ), 'PNG' )
		return
	p_center, q_center = -0.793191078177363, 0.16093721735804
	zoom = (i / max_frames * 2) ** 3 * max_zoom + 1
	scalefactor = 1 / zoom
	pmin_ = (pmin - p_center) * scalefactor + p_center
	qmin_ = (qmin - q_center) * scalefactor + q_center
	pmax_ = (pmax - p_center) * scalefactor + p_center
	qmax_ = (qmax - q_center) * scalefactor + q_center
	img = manbrot( pmin_, pmax_,400, 400, qmin_, qmax_, inf_board=230, max_it=100 )
	img.save( "Images4/Mandelbrot{i}.png".format( i=i ), "PNG" )


def make_gif(gif_name):
	file_list = glob.glob( 'Images4/*.png' )  # Get all the pngs in the current directory
	list.sort( file_list, key=lambda x:
	int( x[18:].split( '.' )[0] ) )  # Sort the images by #, this may need to be tweaked for your use case
	print(file_list)
	with open( 'image_list.txt', 'w' ) as file:
		for item in file_list:
			file.write( "%s\n" % item )
	os.system( 'convert @image_list.txt {}.gif'.format( gif_name ) )  # On windows convert is 'magick'


# create_images(1,3,300)
# for i in range(max_frames):
# 	create_images(i, max_frames, max_zoom)

make_gif( 'manbrot' )
