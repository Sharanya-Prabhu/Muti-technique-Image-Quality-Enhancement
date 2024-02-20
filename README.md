
# Muti-technique Image Quality Enhancement

Parallel programming implementation of image qulity enhancement techniques using 2D Image convolution in CUDA. 

Techniques implemented - 

1) Luminance-based Contrast Enhancement : This contrast-enhancement technique improves the visual quality of an image by adjusting the luminance of each pixel
2) Histogram Equalization : An image processing technique used to improve contrast by effectively spreading out the most frequent intensity values, i.e. stretching out the intensity range of the image. 
3) Denoising : A technique that involves removing unwanted noise while preserving important image features. 
4) Image sharpening : A technique that enhances the edges and fine details in an image, improving the overall clarity of the image.


## Methodology

### 1. Luminance-based Contrast Enhancement
Step 1: Extract the R, G, B values of the input pixel. 

Step 2: Calculate the value for the greyscale equivalent of luminance.

	 lum = 0.2126* R + 0.7152* G + 0.0722 * B
The weights are based on human sensitivity to different light colors. The human eye is most sensitive to green light, which is why, it is given the highest weight.

Step 3: Compute the new R, G, B values for the pixel and set it as the output pixel

	R_out = min( max( ( R – lum ) * 1.2 + lum , 0 ), 255 )  
	G_out = min( max( ( G – lum ) * 1.2 + lum , 0 ), 255 )
	B_out = min( max( ( B – lum ) * 1.2 + lum , 0 ), 255 )

In the formula, the difference between the pixel’s color and its luminosity is amplified. The min() and max() ensure the output values lie in the [0,255] range.

This results in an image with an increased contrast and more visible details, while preserving the overall brightness of the image.

### 2. Histogram Equalization

Step 1: Calculate the histogram for an input image. This is done by storing the frequency (number of pixels) for each intensity of pixel.

Step 2: Calculate the CDF (Cumulative Distribution Function) which for a random variable X (in this case intensity of pixels) is the number of pixels aving intensities lesser than or equal to X .

Step 3: Normalize the CDF to make sure the values of the intensities lie in the range of 0-255.

The aim is to make a clear distinction and contrast between the black part and white part of the image. The white part of the image contains the part which needs to be visible to the human eye. Using the CDF we make sure that the distribution of the frequency is uniform.

### 3. Denoising

- Each thread processes a single pixel of the input image and calculates the corresponding pixel value of the output image using the 9-point averaging filter.
- The filter used in this denoising kernel is a simple averaging filter that calculates the output pixel value by taking the weighted average of the surrounding 8 neighboring pixels and the pixel itself. The weights are constant and set to 1/10 for all pixels. This filter is effective at removing random noise from the image, but it can also cause blurring and loss of image details.

- The denoising kernel only processes pixels that are not on the image boundary. This is because the kernel accesses the neighboring pixels of the current pixel, and accessing out-of-bounds memory can cause undefined behavior.

### 4. Image Sharpening

Step 1: Define a 3*3 matrix in the kernel.

Step 2: Apply a checker to make sure the thread values we iterate through are within bounds. 

Step 3: Loop and check each RGB value from the image. Store the sum of the current pixel values for current thread. 

Step 4: To sharpen, multiply the pixel value  with the corresponding value in the kernel and adds it to the sum of the current thread.

Step 5: Assign the output pixel for the current thread with the RGB values 






