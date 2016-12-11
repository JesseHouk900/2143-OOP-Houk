"""
http://effbot.org/imagingbook/image.htm
http://www.textfiles.com/art/
http://www.tutorialspoint.com/python/python_files_io.htm
"""

from PIL import Image
import os
import sys
import random


class ImageEd(object):
	def GlassFilter(self, **args):
		# make a list to hold color values in cadence 
		colors = []
		# get the image height and width
		width, height = args['image'].size
		# save filterPower as fp
		fp = args['filterPower']
		# get number of elements to divide by
		d = 2 * fp * 2 * fp
		for x in range(fp,width-fp-1):
			for y in range(fp, height-fp-1):
				# loop through each cadence as i and j going from 
				# -fp to fp. z is for indexing colors
				for i in range(-fp, fp):
					# loop simultaneously through the lists returned by the
					# range function using the zip function. this will stop
					# looping when the shortest list is done indexing
					#for j,z in zip(range(-fp, fp), range(0,d)):
					#	print('j',j,'z',z)
					#	colors[z] = args['image'].getpixel((x+i,y+j))
					# doesn't work, but cool thought
					for j in range(-fp,fp):
						colors.append(args['image'].getpixel((x+i,y+j)))
				# if an imageOut argument was passed
				if not args['imageOut'] == None:
					# then set the pixel identical to the current pixel to
					# a random neighbour
					args['imageOut'].putpixel((x,y), random.choice(colors))
				else:
					# set current pixel to a random neighbour
					args['image'].putpixel((x,y), random.choice(colors))
				# clear array for reuse
				colors[:] = []
		if not args['imageOut'] == None:
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut'].save(args['outfile_name'])
		else:
			# save over the origional picture
			args['image'].save(args['file_name'])
				
				
	# Manipulates image across horizontal middle line
	def VerticalFlip(self, **args):

		width, height = args['image'].size
		# make a copy of the object at args['image'] and save it as image
		image = args['image']
		if not args['imageOut'] == None:
			for x in range(0, width):
				for y in range(0,height):
					args['imageOut'].putpixel((x,y), image.getpixel((x,height-y-1)))
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut'].save(args['outfile_name'])
		else:
			# loop through the image by half the width and height because for
			# every iteration, two pixels are changed
			for x in range(0, width//2):
				for y in range(0, height//2):
					# save the line being overwritten in a temp tup
					temp = image.getpixel((x,y))
					image.putpixel((x,y), image.getpixel((x,height-y-1)))
					image.putpixel((x,height-y-1), temp)
			# save over the origional picture
			image.save(args['file_name'])
				
		
				
				
					
	# Manipulates image across vertical middle line			
	def HorizontalFlip(self, **args):
	
		width, height = args['image'].size
		# make a copy of the object at args['image'] and save it as image
		image = args['image']
		if not args['imageOut'] == None:
			for x in range(0, width):
				for y in range(0, height):
					args['imageOut'].putpixel((x,y), image.getpixel((width-x-1,y)))
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut'].save(args['outfile_name'])
		else:
			# loop through the image by half the width and height because for
			# every iteration, two pixels are changed
			for x in range(0, width//2):
				for y in range(0, height//2):
					# save the line being overwritten in a temp tup
					temp = image.getpixel((x,y))
					image.putpixel((x,y), image.getpixel((width-x-1,y)))
					image.putpixel((width-x-1,y), temp)
			# save over the origional picture
			image.save(args['file_name'])
			
				

	def Posterize(self, **args):
	
		width, height = args['image'].size
		# make a copy of the object at args['image'] and save it as image
		image = args['image']
		colors = []
		# loop through the image
		for x in range(0, width):
			for y in range(0, height):
				# save pixel in pix
				pix = image.getpixel((x,y))
				# iterate through the pixels color channels
				for z in range(0,3):
					# change the color to a snaped color value
					colors.append(self.__snap_color__(pix[z],args['snapValue']))
				if not args['imageOut'] == None:
					args['imageOut'].putpixel((x,y), tuple(colors))
				else:
					# make the pixel the new snapped color set
					image.putpixel((x,y), tuple(colors))
				colors[:] = []			
		if not args['imageOut'] == None:
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut'].save(args['outfile_name'])
		else:
			# save over the origional picture
			image.save(args['file_name'])
				
	
	def Blur(self, **args):
		# get the color values of the image in a tuple, (R,G,B), in a list
		#self.all_pixels = list(image.getdata())
		r = 0 
		g = 0
		b = 0
		# get the image height and width
		width, height = args['image'].size
		# make a copy of the object at args['image'] and save it as image
		image = args['image']
		kernel = args['kernel']
		# get number of elements to divide by
		d = 2 * kernel * 2 * kernel
		# loop through the image as rows and columns with x's starting
		# distance as the kernel and end distance as width-kernel-1
		# and y's starting distance as the kernel and end distance as
		# height-kernel-1
		for x in range(0, width-1):
			for y in range(0, height-1):
				if x >= kernel and x < width-kernel and y >= kernel and y < height-kernel:
					# loop through each cadence as i and j going from 
					# -kernel to kernel
					for i in range(-kernel, kernel):
						for j in range(-kernel, kernel):
							# get current pixel for evaluation
							currPix = image.getpixel((x+i,y+j))
							# add color numbers together
							r += currPix[0]
							g += currPix[1]
							b += currPix[2]
					# replace the pixel at x,y with the new color averaged from
					# the sum of the numbers in the cadence
					if not args['imageOut'] == None:
						args['imageOut'].putpixel((x,y), (int(r/d),int(g/d),int(b/d)))
					else:
						image.putpixel((x,y), (int(r/d),int(g/d),int(b/d)))
					# reset the values to 0 
					r = 0 
					g = 0 
					b = 0
				else:
					if not args['imageOut'] == None:
						args['imageOut'].putpixel((x,y), image.getpixel((x,y)))
		if not args['imageOut'] == None:
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut'].save(args['outfile_name'])
		else:
			# save over the origional picture
			image.save(args['file_name'])
	
	
	def Solarize(self, **args):
		colors = []
		width, height = args['image'].size
		# make a copy of the object at args['image'] and save it as image
		image = args['image']
		thres = args['threshold']
		for x in range(0, width):
			for y in range(0, height):
				pix = image.getpixel((x,y))
				for z in range(0,3):
					if args['exposure'] == 'over':
						# check that the individual colors from the channels are
						# greater than or equal to the threshold
						
						if pix[z] > thres:
							colors.append(255 - pix[z])
						else:
							colors.append(pix[z])
					elif args['exposure'] == 'under':
						if pix[z] < thres:
							colors.append(255 - pix[z])
						else:
							colors.append(pix[z])
				if not args['imageOut'] == None:
					args['imageOut'].putpixel((x,y), tuple(colors))
				else:
					image.putpixel((x,y), tuple(colors))
				colors[:] = []
		if not args['imageOut'] == None:
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut'].save(args['outfile_name'])
		else:
			# save over the origional picture
			image.save(args['file_name'])
		
	def Warhol(self, **args):
		# list of 15 colors
		clrs = [(238,203,173), (0,255,255), (0,100,0),
		(255,255,0), (205,92,92), (250,128,114), (255,140,0),
		(176,48,96), (216,191,216), (210,180,140), (0,0,255),
		(124,252,0), (255,69,0), (255,20,147), (138,43,226),
		(230,230,250)]
# """1"""		(238,203,173),  """Peach Puff 2"""
# """2"""		(0,255,255),    """    Cyan    """
# """3"""		(0,100,0),      """ Dark Green """
# """4"""		(255,255,0),    """   Yellow   """
# """5"""		(205,92,92),    """ Indian Red """
# """6"""		(250,128,114),  """   Salmon   """
# """7"""		(255,140,0),    """Dark  Orange"""
# """8"""		(176,48,96),    """   Maroon   """
# """9"""		(216,191,216),  """   Thistle  """
# """10"""		(210,180,140),  """     Tan    """
# """11"""		(0,0,255),      """    Blue    """
# """12"""		(124,252,0),    """ Lawn Green """
# """13"""		(255,69,0),     """ Orange Red """
# """14"""		(255,20,147),   """ Deep  Pink """
# """15"""		(138,43,226),   """Blue  Violet"""
# """16"""		(230,230,250)]	"""  Lavender  """
		width, height = args['imageOut'].size
		snapValue = 17
		# grayscale image
		args['image'].convert("L")
		# posterize image
		self.Posterize(**args)
		# make a list of values coordnating with the avaliable values
		snapVals = []
		for x in range(0,256//snapValue + 1):
			snapVals.append(x*snapValue)
		colors = {snapVals[x]:clrs[x] for x in range(0,256//snapValue + 1)}
		newPix = []
# Makes a nightmare
		# loop through the image
		# for x in range(0, width):
			# for y in range(0, height):
				# # get pixel for evaluation
				# pix = image.getpixel((x,y))
				# # loop through channels of color
				# for c in range(0,3):
					# pixSnapVal = self.__snap_color__(pix[c], args['snapValue'])
					# # loop through avaliable snap values to determine
					# # which color to replace with
					# for z in range(0,len(snapVals)):
						# # if the pixels altered color is equal to a
						# # value in possible values
						# if pixSnapVal == snapVals[z]:
							# # then replace that color
							# if not args['imageOut'] == None:
								# args['imageOut'].putpixel((x,y), (colors[z][c]))
							# else:
								# image.putpixel((x,y), (colors[z][c]))
		for x in range(0, width):
			for y in range(0, height):
				# get pixel for evaluation
				pix = args['imageOut'].getpixel((x,y))
				# loop through channels of color
				for c in range(0,3):
					pixSnapVal = self.__snap_color__(pix[c], snapValue)
					# loop through avaliable snap values to determine
					# which color to replace with
					for z in colors.keys():
						# if the pixels altered color is equal to a
						# value in possible values
						if int(pixSnapVal) == int(z):
							# then replace that color
							newPix.append(int(colors[z][c]))
				if not args['imageOut2'] == None:
					args['imageOut2'].putpixel((x,y), tuple(newPix))
				else:
					args['imageOut'].putpixel((x,y), tuple(newPix))
				newPix[:] = []
		if not args['imageOut2'] == None:
			# save the image in the file associated with the key 'outfile_name'
			args['imageOut2'].save(args['outfile_name2'])
		else:
			# save over the origional picture
			args['imageOut'].save(args['outfile_name'])
				
				
	def printImage(self, image):
		for x in range(0,image.size[1]):
			for y in range(0,image.size[0]):
				print(image.getpixel((x,y)))
	def __snap_color__(self,color,snap_val):
		color = int(color)
		m = color % snap_val
		if m < (snap_val // 2):
			color -= m
		else:
			color += (snap_val - m)
		return int(color)
	
