
# ASCII Art Generator

ASCII (American Standard Code for Information Interchange) is a common encoding format used for representing text data in computers.
This project converts Digital images to ASCII Art.


![input](https://user-images.githubusercontent.com/76778888/174254644-570b4ca6-5fcf-4a84-bf87-6f4871a49523.jpg)

Input image
![output1](https://user-images.githubusercontent.com/76778888/174254891-8a78e0ba-7065-403d-afb4-873a1dc077e2.jpg)

ASCII Image

![output](https://user-images.githubusercontent.com/76778888/174255295-34f575ef-d70b-4959-bd12-d7ead5828353.png)

Pencil Sketch of ASCII image

## Steps to Run the Project
1. Open Vs code and Open file ascii.py.
2. Open terminal of Vs code and type command "py ascii.py" and run the command.
3. Enter path of image to be convert in to ascii art.
4. After successful running of programme two files is generated one color ASCII image and other pencil sketch of ASCII image.
5. Now you can see the image in the path which is given in the code.
6. To change the background of image from white to black you have to change the color=(255,255,255) to color=(0,0,0).
## Theory
The theory behind this project is to map each pixel of image in to suitable ascii character which has same brightness value.
Since, each image is represented as a pixel which has different brightness value. To calculate the brightness value of each pixel we have to get the image size and for getting the size of each pixel we have to adjust the number of columns by itself.
We have to also find the character width and height. After getting character height and width we have to resize our image according to calculated parameter.
Now, main important part of this project is to map pixels in to character. For this we have find brightness value of each pixel in array form and then we have to calculate the single brightness value. After getting single brightness value we have to find suitable character from the list of character which has been arranged according to brightness value.
By this way we have converted digital image in to ascii image.
## Lessons Learned
1. How digital images are stored
2. Converting each pixel in to ascii character with the help brightness value.
3. Basics of image processing.
4. Libraries and framework such as openCv, Pillow, Numpy.
5. Scaling of image to get desired Output

## Additional Task
conversion of the ascii image in to pencil sketch. After getting the ascii image, i have used openCv library to convert it in it pencil sketch. 

## Video Demo


https://user-images.githubusercontent.com/76778888/174349704-eb6d49cb-64c9-48d5-ab1b-4c6342c9cf75.mp4


## Resources and References
1. Basics of ascii art and images -https://www.javatpoint.com/what-is-ascii-art
2. How images are stored- https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/
3.  documentation for generate ascii art-https://levelup.gitconnected.com/python-ascii-art-generator-60ba9eb559d7
