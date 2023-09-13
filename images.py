from PIL import Image, ImageFilter
img = Image.open("./Pokedex/pikachu.jpg")
img2 = Image.open("./Pokedex/astro.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
converted_img = img.convert('L')
rotated_img = img.rotate(180)
resized_img = img.resize((300,300))

img2.thumbnail((400, 400))
#filtered_img.save("blur.png", 'png')
converted_img.save("grey.png", 'png')
#Crop image
box = (100, 100, 400, 400)
region = img.crop(box)


region.show()
img2.show()