# Copiador de Archivos

Este script en Python permite copiar archivos y directorios de un origen a un destino, con la capacidad de gestionar archivos y carpetas existentes en el destino.

## Requisitos

- Python 3.x instalado en tu sistema.
- No se requieren dependencias externas, ya que el script utiliza solo bibliotecas estándar de Python.

## Funcionamiento

1. **Ejecución del Script:**

   - Ejecuta el script `copiar_archivos.py`.
   - Se te pedirá ingresar la ruta del directorio que deseas copiar y la ruta del directorio de destino.

2. **Copia de Archivos:**

   - El script recorre todos los archivos y carpetas del directorio de origen.
   - Por cada archivo, pregunta al usuario si desea reemplazarlo si ya existe en el destino.
   - Si el archivo no existe en el destino o se elige reemplazarlo, se copia al destino manteniendo la estructura de directorios.

3. **Copia de Carpetas:**

   - Si se encuentra una carpeta en el directorio de origen, el script también la copiará al destino.
   - Si la carpeta ya existe en el destino, se preguntará al usuario qué acción desea tomar (reemplazar, fusionar o omitir).

4. **Gestión de Carpetas de Sistema:**

   - El script ignora automáticamente las carpetas de sistema de Windows para evitar problemas.

5. **Progreso:**

   - Durante la ejecución, se mostrará el progreso en la consola, indicando cuántos archivos y carpetas se han copiado hasta el momento.

6. **Interacción con el Usuario:**

   - El script requiere intervención del usuario para decidir sobre la gestión de archivos y carpetas existentes en el destino.

## Colaboración

Si encuentras algún problema o tienes alguna sugerencia de mejora, ¡no dudes en abrir un issue o enviar un pull request!
