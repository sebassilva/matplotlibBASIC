#regular expresions
#vagina
import re

def regex():
    m = re.search('(?<=abc)media', "asdfedefqwa")
    print(m.group(0))


import os
    
def pingTest(host):
    ping = os.popen('ping '+ host + ' -n 1') #-n numero de veces que hara la peticion
    result = ping.readlines()
    #regex()
    #print(result)

pingTest("google.com")
pingTest("stackoverflow.com")






#GRAFICA
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1,2,3]
y = [12,16,6]

x2 = [5,6,7]
y2 = [6,15,7]


plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')


plt.title('Ping test')
plt.ylabel('Y tiempo')
plt.xlabel('X axis')

plt.show()

#Pausa la CMD
#os.system("pause")
