import matplotlib.pyplot as plt
import time
import random
import csv

class MonitorTemperaturaPC:
    def __init__(self, duracion_max=45, intervalo=0.8, archivo_csv="temperaturas.csv"):
        self.duracion_max = duracion_max
        self.intervalo = intervalo
        self.tiempos = []
        self.temperaturas = []
        self.inicio = time.time()
        self.archivo_csv = archivo_csv
        
        plt.ion()
        self.fig, self.ax = plt.subplots()

        self.iniciar_csv()

    def iniciar_csv(self):
        with open(self.archivo_csv, mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Tiempo (s)", "Temperatura (°C)"])

    def leer_temperatura(self):
        # Simulación de temperatura entre 35°C y 75°C con pequeñas fluctuaciones
        if self.temperaturas:
            # Fluctuar suavemente a partir del último valor
            ultima = self.temperaturas[-1]
            temp = max(45, min(65, ultima + random.uniform(-0.7, 0.7)))
        else:
            # Valor inicial aleatorio
            temp = random.uniform(45, 55)
        return round(temp, 2)

    def actualizar_datos(self):
        ahora = time.time() - self.inicio
        temp = self.leer_temperatura()
        if temp is not None:
            self.tiempos.append(ahora)
            self.temperaturas.append(temp)

            while self.tiempos and self.tiempos[0] < ahora - self.duracion_max:
                self.tiempos.pop(0)
                self.temperaturas.pop(0)

            self.guardar_datos_csv(ahora, temp)

    def guardar_datos_csv(self, tiempo, temperatura):
        with open(self.archivo_csv, mode='a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([tiempo, temperatura])

    def graficar(self):
        self.ax.clear()
        self.ax.plot(self.tiempos, self.temperaturas, color='red')
        self.ax.set_title("Temperatura CPU PC (Simulada)")
        self.ax.set_xlabel("Tiempo transcurrido (s)")
        self.ax.set_ylabel("Temperatura (°C)")
        self.ax.grid(True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def ejecutar(self):
        try:
            while plt.fignum_exists(self.fig.number):
                self.actualizar_datos()
                self.graficar()
                time.sleep(self.intervalo)

        except KeyboardInterrupt:
            print("Monitoreo interrumpido por el usuario.")

        finally:
            print("Monitoreo finalizado.")
            plt.ioff()
            plt.close(self.fig)

if __name__ == "__main__":
    monitor = MonitorTemperaturaPC()
    monitor.ejecutar()
