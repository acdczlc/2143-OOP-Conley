from PIL import Image
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from random import randint

"""Class imageEd

    class recieves an image and can modify it using the methods in
    the class.

    Attributes:
        glass_effect: makes pic look like it is being viewed through glass
        flip: turns pic upside down
        blur: makes pic blurry
        posterize: reduces color
        solarize: makes pic look overexposed
        warhol: greyscales posterizes and then adds different colors
    """
class imageEd(object): #class containing methods
    def __init__(self,filename):
        img = Image.open(filename)
        self.img=img #opens image and saves in self
        width, height = img.size
        self.w=width #saves height and width for later use
        self.h=height

    """glass effect

    makes picture look like it was viewed through glass

    Args:
        self
        distance: value passed in defaults to 8 determines clearness
    """
    def glass_effect(self,distance=8):
        for y in range(0,self.h):
            for x in range(0,self.w):
                newx=random.randint((x-distance),(x+distance))
                newy=random.randint((y-distance),(y+distance))
                if newx<0:     #gets random number in area
                    newx=0
                if newx>self.w-1: #makes sure number in area
                    newx=self.w-1 #that exists
                if newy<0:
                    newy=0
                if newy>self.h-1:
                    newy=self.h-1
                pix = self.img.getpixel((newx,newy)) #gets random pixel
                self.img.putpixel((x,y),(pix[0],pix[1],pix[2]))
        self.img.show()  #places random pixel
         
    """flip

    turns picture upside down
    Args:
        self
    """
    def flip(self):
        newimg=Image.new("RGBA",(self.w,self.h))#creates new image
        for r in range(0,self.h):               #to put pixels in
            for c in range(0,self.w):
                pix = self.img.getpixel((c,r))
                newimg.putpixel((c,self.h-r-1),(pix[0],pix[1],pix[2]))
        newimg.show() #puts pixels in new image upside down

    """blur

    makes picture look blurry

    Args:
        self
        blur_power: value passed in defaults to 3 determines blurriness
    """
    def blur(self,blur_power=3):
        d = 2*blur_power * 2*blur_power #area of blur
        for x in range(blur_power,self.w-blur_power):
            for y in range(blur_power,self.h-blur_power):
                r = 0
                g = 0
                b = 0
                for i in range(-blur_power,blur_power):
                    for j in range(-blur_power,blur_power):
                        pix = self.img.getpixel((x+i,y+j))
                        r += pix[0] #accumulates color values
                        g += pix[1]
                        b += pix[2]
                self.img.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
        self.img.show()
        
    """posterize

    makes picture look cartoonish

    Args:
        self
        snapval: value passed in defaults to 64 
        determines colors
    """
    def posterize(self,snapval=64):
        for x in range(0,self.w):
            for y in range(0,self.h):
                pix=self.img.getpixel((x,y))
                color=[0,0,0] #stores each color value
                for u in range(0,3):#runs once for each color
                    color[u]=pix[u]
                    m=pix[u]%snapval #calculates m 
                    if m < (snapval // 2):
                        color[u] -= m 
                    else:
                        color[u] += (snapval - m)
                self.img.putpixel((x,y),(color[0],color[1],color[2]))
        self.img.show() #puts new colors in original spots

    """solarize

    makes picture look overexposed

    Args:
        self
        threshold: value passed in defaults to 100
        determines colors
    """
    def solarize(self,threshold=100):
        for x in range(0,self.w):
            for y in range(0,self.h):
                pix=self.img.getpixel((x,y))
                color=[0,0,0] #stores each color value
                for u in range(0,3): #runs once for each color
                    if pix[u]<threshold:
                        color[u]=255-pix[u] #negates value
                    else:
                        color[u]=pix[u] #keeps original value
                self.img.putpixel((x,y),(color[0],color[1],color[2]))
        self.img.show() #puts new color in original spot

    """warhol

    makes picture distorted with different colors

    Args:
        self
        rectangle size: value passed in defaults to 5
        how big of an area is used 
    """
    def warhol(self,rectangleSize=5):
        for y in range(0,self.h): #greyscales pic
            for x in range(0,self.w):
                pix=self.img.getpixel((x,y))
                avg=(pix[0]+pix[1]+pix[2])/3
                self.img.putpixel((x,y),(avg,avg,avg))
        self.posterize() #runs posterize on pic
        #colors at intervals for warhol
        warhol=[(0,0,255),(255,0,255),(255,165,0),(255,255,0),
        (255,0,0),(0,255,0),(0,128,128)]
        for y in range(0,self.h):
            for x in range(0,self.w):
                totalred=0
                totalgreen=0
                totalblue=0
                for h in range(y-rectangleSize, y+rectangleSize):
                    for g in range(x-rectangleSize,x+rectangleSize):
                        if g<0:
                            g=0
                        if g>self.w-1: #stops out of image pixels from being used
                            g=self.w-1
                        if h<0:
                            h=0
                        if h>self.h-1:
                            h=self.h-1
                        pix=self.img.getpixel((g,h))
                        totalred+=pix[0] #accumulates values
                        totalgreen+=pix[1]
                        totalblue+=pix[2]

                        #calculates new colors using size of rectangle
                newred=totalred/(2*(rectangleSize*rectangleSize)+1)
                newgreen=totalgreen/(2*(rectangleSize*rectangleSize)+1)
                newblue=totalblue/(2*(rectangleSize*rectangleSize)+1)
                totalintensity=(newred+newgreen+newblue)/3
                warholcolor=totalintensity%32 #calculates warholcolor
                if warholcolor>6: #catches any outliers
                    warholcolor=6
                self.img.putpixel((x,y),warhol[warholcolor])
        self.img.show() #places new color in original spot

