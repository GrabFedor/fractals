from PIL import Image, ImageDraw
from random import randint
import json
import requests
import glob
import os

def new_point(first_point, second_point):
	x = abs(int((first_point[0] + second_point[0]) / 2))
	y = abs(int((first_point[1] + second_point[1]) / 2))
	return (x, y)

def make_gif(gif_name):
	file_list = glob.glob('Serpinskiy/*.png') # Get all the pngs in the current directory
	list.sort( file_list, key=lambda x:
		int(x[21:].split( '.' )[0] )) # Sort the images by #, this may need to be tweaked for your use case

	with open('image_list.txt', 'w') as file:
		for item in file_list:
			file.write("%s\n" % item)
	os.system('convert @image_list.txt {}.gif'.format(gif_name))

def make_a_triangle(iterations):
	img = Image.new( "RGB", (600, 600) )

	a_vertex = (50, 550)
	b_vertex = (550, 550)
	c_vertex = (300, 50)

	img.putpixel( a_vertex, (255, 255, 255) )
	img.putpixel( b_vertex, (255, 255, 255) )
	img.putpixel( c_vertex, (255, 255, 255) )

	point = (132, 89)
	numbers = [randint(1,3) for _ in range(iterations)]
	for number in numbers:

		if number == 1:
			point = new_point( point, a_vertex )
			color = (129,55,60)

		if number == 2:
			point = new_point( point, b_vertex )
			color = (10, 55, 200)

		if number == 3:
			point = new_point( point, c_vertex )
			color = (70, 230, 170)

		img.putpixel(point, color)
	img.save( 'Serpinskiy2/Serpinskiy.png', 'PNG' )

if __name__ == '__main__':
	make_a_triangle(1000000)