[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19144272&assignment_repo_type=AssignmentRepo)
# Lab03: Visualización de Datos en Raspberry Pi 4

## Integrantes

Juan Sebastian Alvarez Muñoz

## Documentación


## Preguntas

1. ¿Qué función cumple ```plt.fignum_exists(self.fig.number)``` en el ciclo principal?

Este método se emplea para verificar si la ventana gráfica de Matplotlib continúa activa. Mientras la figura no haya sido cerrada por el usuario, el programa seguirá ejecutándose y actualizando la visualización. En caso de que el usuario cierre la ventana, el método devuelve False, lo que provoca que el ciclo termine y, con ello, se detenga el monitoreo.

2. ¿Por qué se usa ```time.sleep(self.intervalo)``` y qué pasa si se quita?

La función time.sleep(self.intervalo) se introduce para establecer una pausa entre cada iteración del ciclo, usando como referencia el intervalo definido. Esto evita que las lecturas y actualizaciones se ejecuten sin control. Si se eliminara esa pausa, el programa intentaría ejecutar las acciones lo más rápido posible, lo que implicaría un consumo excesivo de recursos y podría provocar inestabilidad o comportamiento no deseado en el sistema.

3. ¿Qué ventaja tiene usar ```__init__``` para inicializar listas y variables?

Definir variables y estructuras de datos dentro del método __init__ permite que cada vez que se crea una nueva instancia del objeto, estas se inicien con valores predeterminados. Esto facilita la reutilización del código y garantiza una configuración coherente y controlada de los atributos de la clase.

4. ¿Qué se está midiendo con ```self.inicio = time.time()```?

La asignación self.inicio = time.time() registra la hora exacta en que comienza el monitoreo, tomando como referencia el tiempo transcurrido desde el inicio del sistema (epoch). Esto se usa para calcular, en cada ciclo, cuánto tiempo ha pasado desde el inicio, lo cual es útil para representar correctamente los datos en la gráfica.

5. ¿Qué hace exactamente ```subprocess.check_output(...)```?

Este método ejecuta un comando del sistema operativo como si se tratara de una terminal. En este contexto, se utiliza para obtener la temperatura del procesador en una Raspberry Pi mediante el comando vcgencmd measure_temp. La salida del comando se captura y se procesa para extraer el valor numérico correspondiente a la temperatura.

6. ¿Por qué se almacena ```ahora = time.time() - self.inicio``` en lugar del tiempo absoluto?

Registrar el tiempo relativo desde el inicio del monitoreo permite tener una línea de tiempo coherente que siempre arranca desde cero. Si se usara el tiempo absoluto, los valores dependerían del momento del día, lo cual dificultaría la interpretación visual de los datos graficados.

7. ¿Por qué se usa ```self.ax.clear()``` antes de graficar?

Antes de trazar una nueva gráfica, se limpia el contenido anterior para evitar la superposición de datos. Esto asegura que en cada actualización se muestre únicamente la información más reciente, manteniendo la gráfica clara y ordenada.

8. ¿Qué captura el bloque ```try...except``` dentro de ```leer_temperatura()```?

Este bloque está diseñado para capturar excepciones que puedan surgir durante la ejecución del comando que obtiene la temperatura. Esto incluye errores como la ausencia del comando, problemas de permisos u otros fallos del sistema. Al manejar estas excepciones, se evita que el programa se detenga inesperadamente.

9. ¿Cómo podría modificar el script para guardar las temperaturas en un archivo .```csv```?

Para guardar los datos de temperatura en un archivo .csv, basta con añadir una función que escriba los valores en el archivo dentro del método actualizar_datos(). Cada nueva lectura se agregará como una fila en el archivo, lo que permite un registro cronológico de las mediciones para su análisis posterior.
