import cv2
import random
import time

start = time.time()

img = cv2.imread ('../Images/blue-chicory.jpg')

#cv2.line(img, (0,100), (500,600), (255,0,0), 3)
#cv2.circle (img, (400,400), 100, (0, 0, 255), -1)
#cv2.rectangle (img, (200,400), (600,800), (0,0,0), -1)

#img [300:900, 200:400] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

cv2.putText (img, 'This is a flower,', (330, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow ('Frame', img)
#cv2.imwrite ('../Images/another-blue-chicory.jpg', img)

end = time.time()
diff = end - start
print (diff)

print (img.shape)

cv2.waitKey(0)
