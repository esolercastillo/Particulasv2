from particulaMasa import *
from random import random, seed
from math import sqrt
import matplotlib.pyplot as plt
import time
from mpl_toolkits import mplot3d
pausa = 0.02

class GSimulacion:
        
    def __init__(self, NumParticulas, tiempoTot):
        self.N = NumParticulas
        self.tiempoTot = tiempoTot
        self.particulas = []
        for _ in range(0,self.N):
            self.particulas.append(ParticulaMasa())
        self.init_pos()  
        self.init_vel() 
        self.init_masa()
        self.deltat = 0.1
        self.tiempo =0.0

    def init_pos(self):
        self.particulas[0].pos=np.zeros(3) # la primera en el centro
        self.particulas[1].pos=np.array([1, 1, 0.])
        self.particulas[2].pos=np.array([1.2, 0.25, 0.])

        seed()
        for i in range(3,self.N):
            self.particulas[i].pos =np.array([random()*2-1, random()*2-1, random()*2-1])

    def init_vel(self):
        seed()
        self.particulas[0].vel=np.zeros(3) # la primera quieta
        self.particulas[1].vel=np.array([0,0.5,0.])
        self.particulas[2].vel=np.array([0,0.5,0.])
        for i in range(3,self.N):
            # self.particulas[i].vel =[random()*2-1,random()*2-1,random()*2-1]
            self.particulas[i].vel =np.array([0.,0.5,0.])

    def init_masa(self):
        self.particulas[0].masa = 1.0e10  # La primera más grande
        for i in range(1,self.N):
            self.particulas[i].masa = 1.0e5

# """ """     def prepara_grafico(self):
#         plt.ion()
#         self.fig = plt.figure()
#         self.ax = self.fig.add_subplot(111,projection='3d')
#         # self.ax = plt.axes(projection='3d')

#         self.ax.set_xlim(-2.5,2.5)
#         self.ax.set_ylim(-2.5,2.5)
#         self.ax.set_zlim(-2.5,2.5)

#         #prueba
#         self.grafico = self.ax.scatter([],[],[],c='r',marker='o')
#         plt.draw() """

    # def refresca_particulas(self):
       
    #     self.grafico.remove()
    #     # self.grafico=self.ax.scatter3D(x, y, z, c=z, cmap='Greens')
    #     col=['g']
    #     for _ in range (1,self.N):
    #         col.append('r')
    #     x,y,z = self.vectoriza()    
    #     # plt.title("Partículas. Tiempo= "+ str(self.tiempo))
    #     self.grafico = self.ax.scatter(x,y,z,c=col,marker='o')
    #     # self.ax.view_init(30, 30)
    #     plt.draw()
    #     plt.pause(pausa)

    def print_particulas(self):
        for i in range(0,self.N):
            self.particulas[i].muestra()

    def cabecera(self):
        print ("Inicio de la simulación")


    def paso_simulacion(self):
        for i in range (0,self.N):# update acceleration
            self.particulas[i].aceleracion_cero()
            for j in range (0, self.N):
                    if (i!=j):
                        self.particulas[i].aceleracion_gravitatoria(self.particulas[j])
        
        for i in range (0,self.N):#update vel and pos
                self.particulas[i].actualiza_velocidad_y_posicion(self.deltat)        

    def start(self):
        self.cabecera()
                   # prevents explosion in the case the particles are really close to each other 
        
        while self.tiempo <= self.tiempoTot: 
            print ("Timepo:", self.tiempo)
            self.print_particulas()
            self.paso_simulacion()
            self.tiempo += self.deltat
  
        print ("Fin particulas")


