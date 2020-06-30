import cv2
from MapConnectorFile import MapConnector

mp = MapConnector()
mp.start_process()

# traditionally, this will wait indefinitely until the user presses a key and
# then close the windows and quit. The loop in this program will make it so that
# it never really gets here, but it's a good habit.
cv2.waitKey()
cv2.destroyAllWindows()