import math
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageOps, ImageFont



# list of characters used for mapping Pixels
Character= "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
char_arr= list(Character)
fnt=ImageFont.truetype("fonts/DejaVuSansMono-Oblique.ttf", size=21)
scalef=2
char=len(char_arr)
n_cols=150
 
# get_char function can be used to get suitable char at different intensity value
def get_char(inputvalue):
	
	getchar=char_arr[math.floor(inputvalue)]
	return getchar

image = cv2.imread("data/input.jpg")


height, width, _ = image.shape

# Defining height and width of each cell==pixel
cell_w = width / n_cols
cell_h = scalef * cell_w
n_rows = int(height / cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = fnt.getsize("A")
out_width = char_width * n_cols
out_height = scalef * char_height * n_rows

# Making a new Image using PIL
# to make background white or black 
# just replace color=(0,0,0) to color=(255,255,255)
# color=(0,0,0) for black and color=(255,255,255) for white
color=(255,255,255)
out_image = Image.new("RGB", (out_width, out_height), color)
draw = ImageDraw.Draw(out_image)





#mapping in pixels to characters
for i in range(n_rows):
    for j in range(n_cols):
        pix_image= image[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w),width),:] 
        avg_color=np.sum(np.sum(pix_image,axis=0),axis=0)/(cell_h*cell_w)
        avg_color=tuple(avg_color.astype(np.int32).tolist())
       # c=char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
        c=get_char(min(int(np.mean(pix_image)*char/255),char-1))
        draw.text((j*char_width, i*char_height), c, fill=avg_color, font=fnt)
if color==(255,255,255):
	 cropped_image = ImageOps.invert(out_image).getbbox()
elif color==(0,0,0):
     cropped_image = out_image.getbbox()
out_image = out_image.crop(cropped_image)
#out_image.save("output7.jpg")
# for converting color ascii image to pencil sketch
image2=np.array(out_image)
grey_filter=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey_filter)
blur=cv2.GaussianBlur(invert, (21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch_filter=cv2.divide(grey_filter, invertedblur,scale=200)
cv2.imwrite("data/output.png",sketch_filter)
	

