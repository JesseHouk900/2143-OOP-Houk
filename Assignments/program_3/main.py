
from PIL import Image
import os
import sys
import random
from ImageEdit import ImageEd

def determine_outfile_path(**args):
	if not os.path.isfile(args['outfile_name']):
		w,h = args['image'].size
		outImage = Image.new("RGB", (w,h))
	else:
		outImage = Image.open(args['outfile_name'])
	return outImage

		
if __name__=="__main__":
	args = {'file_name': 'fruitBowl.jpeg',
	'outfile_name': 'blurredFruitBowl.jpeg'}
	image = Image.open(args['file_name'])
	args['image'] = image
	# args['kernel'] = 5
	# args['imageOut'] = determine_outfile_path(**args)
	# ImageEd().Blur(**args)
	# args['imageOut'].close()
	
	# args['outfile_name'] = 'glassFilterFruitBowl.jpeg'
	# args['filterPower'] = 5
	# args['imageOut'] = determine_outfile_path(**args)
	# ImageEd().GlassFilter(**args)
	# args['imageOut'].close()
	
	# args['outfile_name'] = 'verticalFlipFruitBowl.jpeg'
	# args['imageOut'] = determine_outfile_path(**args)
	# ImageEd().VerticalFlip(**args)
	# args['imageOut'].close()
	
	# args['outfile_name'] = 'horizontalFlipFruitBowl.jpeg'
	# args['imageOut'] = determine_outfile_path(**args)
	# ImageEd().HorizontalFlip(**args)
	# args['imageOut'].close()
	
	# args['outfile_name'] = 'posterizeFruitBowl.jpeg'
	# args['imageOut'] = determine_outfile_path(**args)
	# args['snapValue'] = 32
	# ImageEd().Posterize(**args)
	# args['imageOut'].close()
	
	args['outfile_name'] = 'solarizeFruitBowlAbove.jpeg'
	args['imageOut'] = determine_outfile_path(**args)
	args['threshold'] = 100
	args['exposure'] = 'over'
	ImageEd().Solarize(**args)
	args['imageOut'].close()
	
	args['outfile_name'] = 'solarizeFruitBowlUnder.jpeg'
	args['imageOut'] = determine_outfile_path(**args)
	args['threshold'] = 100
	args['exposure'] = 'under'
	ImageEd().Solarize(**args)
	args['imageOut'].close()
	
	args['outfile_name'] = 'temp.jpeg'
	args['outfile_name2'] = 'warholFruitBowl.jpeg'
	args['imageOut2'] = determine_outfile_path(**args)
	args['imageOut'] = determine_outfile_path(**args)
	args['snapValue'] = 32
	ImageEd().Warhol(**args)
	args['imageOut'].close()
	args['imageOut2'].close()
	args['image'].close()
