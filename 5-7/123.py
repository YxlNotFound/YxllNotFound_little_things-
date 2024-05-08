import os
import random
import time

for i in range(random.randint(time.gmtime()[-4],time.gmtime()[0])):
    os.popen('start cmd /c '+ os.popen('whoami').read().split('\\')[-1]. +str(i))
