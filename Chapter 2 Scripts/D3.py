# D3.py - Pictures on the Go
#
# Develop and test a Python program that determines how many images can be 
# stored on a given size USB (fash) drive. The size of the USB drive is to 
# be entered by the user in gigabytes (GB). The number of images that can 
# be stored must be calculated for GIF, JPEG, PNG, and TIFF image file 
# formats. The program output should be formatted as given below.
#   
#   Enter USB size (GB): 4
#   xxxxx images in GIF format can be stored
#   xxxxx images in JPEG format can be stored
#   xxxxx images in PNG format can be stored
#   xxxxx images in TIFF format can be stored
#
# The ultimate file size of a given image depends not only on the image format 
# used, but also on the image itself. In addition, formats such as JPEG allow 
# the user to select the degree of compression for the image quality desired. 
# For this program, we assume the image compression ratios given below. Also 
# assume that all the images have a resolution of 800 * 600 pixels.
# Thus, for example, a 800 * 600 resolution image with 16-bit (2 bytes) color 
# depth would have a total number of bytes of 800 * 600 * 2 = 960,000. For a 
# compression rate of 25:1, the total number of bytes needed to store the image 
# would be 960000 / 25 = 38400. Finally, assume that a GB (gigabyte) equals 
# 1,000,000,000 bytes, as given in Figure 2.1.
#
# (TABLE MODIFIED)
# +--------+---------------+----------+--------+
# | Format | Color (bytes) | Quality  | Ratio  |
# |--------+---------------+----------+--------|
# |  GIF   |       1       | lossless |  5 : 1 |
# |  JPGE  |       3       | lossy    | 25 : 1 |
# |  PNG   |       3       | lossless |  8 : 1 |
# |  TIFF  |       6       | lossless |  n / a |
# *--------+---------------+----------+--------+
#
# Note that a “lossless” compression is one in which no information is lost. A 
# “lossy” compression does lose some of the original information.
#
# Analysis:
#   All images have the resolution of 800 * 600 = 480000 bytes. However, each fo-
#   rmat have an unique color depth and compression ratio so the file size for
#   each format is shown as the followings:
#       * GIF   =  480000  *  1  /  5  =    96000 bytes 
#       * JPGE  =  480000  *  3  / 25  =    57600 bytes
#       * PNG   =  480000  *  3  /  8  =   180000 bytes
#       * TIFF  =  480000  *  6  /  1  =  2880000 bytes
#   
#   By dividing the size per one image per each format by the size of the flash
#   drive, we will be able to get how many images can be store in a flash drive
#   per each format.
#
# Implementaiton:
#   Print the results after some arithmetics.
#
# Date:    09/10/2016
# Author:  Chiayo Lin
# License: GPL 3.0

flash_drive_size = int(input("Enter USB size (GB): ")) * 1e9
formats_and_bytes = \
    (("GIF", 96000), ("JPGE", 57600), ("PNG", 180000), ("TIFF", 2880000))

for name, size in formats_and_bytes: 
    print("{0:<5} images in {1} format can be stored".
            format(int(flash_drive_size // size), name))
