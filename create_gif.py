import imageio.v3 as iio

filenames = []
#filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []

print('Welcome to GIF creator. Please type in the name of the first file below.')
name = str(input('Name of the first file (eg: img1.png): '))
filenames.append(name)

print('Thanks! Would you like to add another? (Y/N)')
nextstep = str(input('Y/N: '))
while nextstep != 'N':
   name = str(input('Name of the next file: '))
   filenames.append(name)
   print('Thanks! Would you like to add another? (Y/N)')
   nextstep = str(input('Y/N: '))

print('Thanks! What would you like to name your creation?')
giftitle = str(input('Title of your GIF (creation.gif): '))

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite(giftitle, images, duration = 500, loop = 0)
