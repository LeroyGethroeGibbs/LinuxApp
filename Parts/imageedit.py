__author__ = 'karinamarie'
import numpy as np
import Image

i= Image.open('colorbar.png')
i = i.convert('RGBA')
data = np.array(i)
red, green, blue, alpha = data.T

print data[0][250]
print len(data[0])

x = [ [146, 238, 138, 255],
      [249, 255, 0, 255],
      [252,164, 0, 255],
      [251, 0, 35, 255] ]
x=np.array(x)
x=x/255.0
print x