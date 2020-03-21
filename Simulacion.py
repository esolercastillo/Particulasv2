from particulaMasa import *
from random import random, seed
from math import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
pausa = 0.02

class Simulacion:
        
    def __init__(self, NumParticulas, tiempoTot):
        self.N = NumParticulas
        self.tiempoTot = tiempoTot
        self.particulas = []
        for _ in range(0,self.N):
            self.particulas.append(ParticulaMasa())
        self.ini_valores()
        self.TamX=5
        self.TamY=5
        self.deltat = 0.1
        self.tiempo =0.0
        self.prepara_grafico()
        self.refresca_particulas() 

    def ini_valores(self):
        self.particulas[0].set_valores(np.zeros(3), np.zeros(3), np.zeros(3), 1.0e10)
        self.particulas[1].set_valores(np.array([1, 1, 0.]), np.array([0,0.5,0.]), np.zeros(3), 1.0e5)
        self.particulas[2].set_valores(np.array([1.2, 0.25, 0.]), np.array([0,0.5,0.]), np.zeros(3), 1.0e5)
        for i in range(3,self.N):
            self.particulas[i].set_valores(np.array([random()*self.TamX-self.TamX/2, random()*self.TamX-self.TamX/2, random()*self.TamX-self.TamX/2]),
            np.array([0,0.5,0]), np.zeros(3), 1.0e5)




    def print_particulas(self):
        for i in range(0,self.N):
            self.particulas[i].muestra()

    def cabecera(self):
        print ("Inicio de la simulación")


    def avanza(self):
        for i in range (0,self.N):# update acceleration
            self.particulas[i].aceleracion_cero()
            for j in range (0, self.N):
                    if (i!=j):
                        self.particulas[i].aceleracion_gravitatoria(self.particulas[j])
        
        for i in range (0,self.N):#update vel and pos
                self.particulas[i].actualiza_velocidad_y_posicion(self.deltat)        

    def simula(self):
        self.cabecera()
                   # prevents explosion in the case the particles are really close to each other 
        
        while self.tiempo <= self.tiempoTot: 
            print ("Timepo:", self.tiempo)
            self.print_particulas()
            self.avanza()
            self.refresca_particulas()
            self.tiempo += self.deltat
  
        print ("Fin particulas")


    def prepara_grafico(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection='3d')
        self.titulo=self.ax.text2D(0.05, 0.95, "Tiempo %.2f"%0.0, transform=self.ax.transAxes)
        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.set_zlim(-2.5,2.5)

        self.grafico = self.ax.scatter([],[],[],c='r',marker='o')
        plt.draw()

    def refresca_particulas(self):
       
        self.grafico.remove() #Limpia el grafico para mostrar las posiciones nuevas
        self.titulo.remove()
        self.titulo=self.ax.text2D(0.05, 0.95, "Tiempo %.2f"%self.tiempo, transform=self.ax.transAxes)
        col=['g']   # La primera verde y el resto rojas
        for _ in range (1,self.N):
            col.append('r')
        x,y,z = self.vectoriza()    
        self.grafico = self.ax.scatter(x,y,z,c=col,marker='o')

        plt.draw()
        plt.pause(pausa)

    def vectoriza(self):
        x=[]
        y=[]
        z=[]
        for i in range(0,self.N):
            x.append(self.particulas[i].pos[0])
            y.append(self.particulas[i].pos[1])
            z.append(self.particulas[i].pos[2])

        return x,y,z
