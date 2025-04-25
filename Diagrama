+-----------------------------+
| INICIO                      |
+-----------------------------+
            |
            v
+-----------------------------+
| Inicializar MonitorTemperaturaRPI  |
| - Configuración de duración, |
|   intervalo y archivo CSV    |
| - Configuración de gráfica   |
+-----------------------------+
            |
            v
+-----------------------------+
| Abrir archivo CSV           |
| - Verificar si está vacío   |
| - Escribir cabecera si es   |
|   necesario                  |
+-----------------------------+
            |
            v
+-----------------------------+
| ¿Existen condiciones para   |
| seguir monitoreando?        | 
| - Si (Ejecutar loop)        |
| - No (Finalizar ejecución)  |
+-----------------------------+
            |
        _________
       |         |
       v         v
+-----------------------------+   No
| Actualizar datos: leer       | <-----------------+
| temperatura, agregar tiempo, |                   |
| guardar en CSV, limpiar      |                   |
| datos antiguos si exceden   |                   |
| el límite de duración       |                   |
+-----------------------------+                   |
            |                                      |
            v                                      |
+-----------------------------+                   |
| Graficar datos en tiempo real|                   |
| - Actualizar gráfica        |                   |
+-----------------------------+                   |
            |                                      |
            v                                      |
+-----------------------------+                   |
| ¿Interrupción de teclado?    |                   |
| - Sí -> Finalizar            |                   |
| - No -> Continuar monitoreo  |                   |
+-----------------------------+                   |
            |                                      |
        _________                                  |
       |         |                                  |
       v         v                                  |
+-----------------------------+   Sí               |
| Finalizar ejecución         | <-----------------+
| - Apagar modo interactivo   |
| - Cerrar gráfica            |
+-----------------------------+
            |
            v
+-----------------------------+
| FIN                          |
+-----------------------------+
