from time import sleep, strftime, time
import matplotlib as mat
#import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
from matplotlib import style

 


#TEMPERATURE =20.0

 

 

 

'''
def write_temp(temp):
    with open("temp_log.csv", "a") as log:
        log.write("{â€‹â€‹â€‹â€‹â€‹â€‹â€‹0}â€‹â€‹â€‹â€‹â€‹â€‹â€‹,{â€‹â€‹â€‹â€‹â€‹â€‹â€‹1}â€‹â€‹â€‹â€‹â€‹â€‹â€‹\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
'''
def data_collection():
    x =[]
    y1 =[]
    y2 =[]
    
    for i in range(1,21):
        y1.append(20.0 + random.random() * 15)
        y2.append(60 + random.random() * 20)
        x.append(time() * i)
    
    graph(x,y1,y2)
    
def alert ():
    Alert = ''
    temp = 20.0 + random.random() * 15
    hum = 60 + random.random() * 20
    if temp > 30 and hum > 70.0:
         Alert = ('Please Stay at Home!!')
    else:
         Alert = ('Enjoy your Ride!!')
    return(Alert)

 

def graph(x,y1,y2):
    fig = Figure()
    #plt = fig.add_subplot()
    mat.use('tkagg')
    title = alert()
    plt.clf()
    plt.scatter(x,y1)
    
    plt.plot(x,y1 , color = 'blue', label = 'Temperature')
    plt.plot(x,y2 , color = 'green',label = 'Humidity')
    plt.xlabel('Time in Seconds')
    plt.ylabel('Weather condition')
    plt.title(label = title)
    plt.legend(bbox_to_anchor=(1, 1))
    plt.savefig('fig1.png')
    #return fig
    #plt.show()
    

 


while True:
    
    #write_temp(temp)
    data_collection()
    #graph(temp)
    
    plt.pause(2)
 
