from time import sleep, strftime, time
import matplotlib as mat
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
from matplotlib import style


#TEMPERATURE =20.0





'''
def write_temp(temp):
    with open("temp_log.csv", "a") as log:
        log.write("{​​​​​​​0}​​​​​​​,{​​​​​​​1}​​​​​​​\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
'''
def data_collection():
    x =[]
    y =[]
    for i in range(1,21):
        y.append(20.0 + random.random() * 15)
        x.append(time() * i)
    
    graph(x,y)


def graph(x,y):
    fig = Figure()
    #plt = fig.add_subplot()
    mat.use('tkagg')

    plt.clf()
    plt.scatter(x,y)
    plt.xlabel('Time in Seconds')
    plt.ylabel('Temperature in oC')
    plt.plot(x,y)
    plt.savefig('fig1.png')
    #return fig
    #plt.show()
    


while True:
    
    #write_temp(temp)
    data_collection()
    #graph(temp)
    
    plt.pause(2)
