# Fractals
***
## Sierpinski fractal
code: sierpinski.py 

The Sierpinski triangle, also called the Sierpinski gasket or the Sierpinski Sieve, is a fractal and attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. Originally constructed as a curve, this is one of the basic examples of self-similar sets, i.e., it is a mathematically generated pattern that is reproducible at any magnification or reduction. It is named after the Polish mathematician Wacław Sierpiński, but appeared as a decorative pattern many centuries before the work of Sierpiński.
### Chaos game (One of the algorithms) 
1. Take three points in a plane to form a triangle, you need not draw it.
2. Randomly select any point inside the triangle and consider that your current position.
3. Randomly select any one of the three vertex points.
4. Move half the distance from your current position to the selected vertex.
5. Plot the current position.
6. Repeat from step 3
### ![Here is my generated Sierpinsiy fractal](https://pp.userapi.com/c850428/v850428205/2d5b/b_d_ipZD6bs.jpg "Sierpinsli fractal")
you can check read about Sierpinski triangle [here](https://en.wikipedia.org/wiki/Sierpinski_triangle) 
***

# Mandelbrot fractal:
code: mandelbrot.py

Here i render mandelbrot fractal determining whether a point (pixel) falls into a Mandelbrot set. 
The set of points C on the complex plane for which the sequence zn, defined by  ![](https://pp.userapi.com/c850428/v850428052/2b80/sL3aPACMNoc.jpg)
does not go to infinity is a Mandelbrot set. Script checks all the points on a complex plane whether it is in the set and take coordinates from them. 

![black and white Mandelbrot set](https://pp.userapi.com/c850428/v850428205/2d62/mZ8kvMk0540.jpg "Man set")

image with zoomed blacknwhite Mandelbrot fractal.

#### Let's see a simple example of how to get the number:
* c = -1,3 + 0,8i
* z0 = 0
* z1 = z0^2 + c = -1,3 + 0,8i
* z2 = z1^2 + c = 1.05 - 2.08i + c = -0.25 - 1.28i
* z3 = z2^2 + c = -1.5759 + 0.64i + c = -1.55 - 0.48i
* z4 = z3^2 + c = 2.1721 + 1.488i + c =  0.8721 + 2.288i

i am not going to do more maths, but we can see, that this number with each iteration goes closer to infinity. Every complex number is a set of coordinates on the plane, if number c is in Mandelbrot set, script takes a point and colors it. To make a fractal picture more beautiful i decided to compare how far goes the complex number and made 255 levels (levels of how far is it), and got 255 shadows of gray color (example on the picture above).


I can change colors in my code and get something like this:
![](https://pp.userapi.com/c850428/v850428205/2d7f/y1glYHUrW_s.jpg "man brot fractal colored")

Also we can animate it and see the zoom process with a really good colors:
![](https://github.com/GrabFedor/fractals/blob/master/manbrot.gif)

you can check more information about Mandelbrot set [here](https://en.wikipedia.org/wiki/Mandelbrot_set)
