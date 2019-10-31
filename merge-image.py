from PIL import Image

# User Input - opacity of the image that is going to be merged
opacity = float(input('What should be the opacity of the merged image (range 0 - 1): '))

# Images must be of same pixel size
image1 = Image.open('Test-1.png')
image1 = image1.resize((1289, 638))
image2 = Image.open('Test-2.png')
image2 = image2.resize((1289, 638))

newImage = Image.blend(image1, image2, opacity).show()
