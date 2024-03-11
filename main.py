import os
import shutil

# Lista de nombres de carpetas de sistema de Windows
carpetas_sistema_windows = ['Windows', 'Program Files', 'Program Files (x86)', 'ProgramData']

def es_carpeta_sistema(carpeta):
    return any(carpeta.lower() == sys_folder.lower() for sys_folder in carpetas_sistema_windows)

def copiar_archivos(origen, destino):
    archivos = os.listdir(origen)
    total_archivos = len(archivos)
    contador = 0

    # Verificar si el directorio padre del origen existe en el destino, si no, crearlo
    nombre_directorio = os.path.basename(origen)
    if os.path.exists(nombre_directorio):
        print(f"\x1b[1;34mEl directorio '{nombre_directorio}' existe.")
    else:
        try:
            os.makedirs(nombre_directorio)
            print("\x1b[1;32mDirectorio creado exitosamente.")
        except OSError as error:
            print(f"Error al crear el directorio: {error}")
        print(f"\x1b[1;32mEl directorio {nombre_directorio} no existe. Se creó el directorio")

    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(f"{destino}/{nombre_directorio}", archivo)
        print(ruta_destino)
        if os.path.isfile(ruta_origen) and not os.path.islink(ruta_origen):
            if os.path.exists(ruta_destino):
                respuesta = input(f"\x1b[1;33m{'*'*50}\nATENCION, el programa requiere su intervencion\n{'*'*50}\nEl archivo {archivo} ya existe en el destino. ¿Desea reemplazarlo? (Sí/No): ").lower()
                if respuesta == 'no':
                    print(f"El archivo {archivo} se ha omitido.")
                    continue
            try:
                shutil.copy2(ruta_origen, ruta_destino)
            except PermissionError:
                print(f"No se pudo copiar el archivo {archivo} debido a permisos insuficientes.")
            except Exception as e:
                print(f"Error al copiar el archivo {archivo}: {e}")
            else:
                print(f"Archivo copiado: {archivo}")
        elif os.path.isdir(ruta_origen) and not es_carpeta_sistema(archivo):
            if os.path.exists(ruta_destino):
                respuesta = input(f"\x1b[1;33m{'*'*50}\nATENCION, el programa requiere su intervencion\n{'*'*50}\nLa carpeta {archivo} ya existe en el destino. ¿Qué desea hacer?\n1. Reemplazar.\n2. Fusionar.\n3. Omitir.\nIngrese el número correspondiente a la opción elegida: ")
                if respuesta == '1':
                    try:
                        shutil.rmtree(ruta_destino)
                        shutil.copytree(ruta_origen, ruta_destino)
                        print(f"Carpeta reemplazada: {archivo}")
                    except PermissionError:
                        print(f"No se pudo copiar la carpeta {archivo} debido a permisos insuficientes.")
                    except Exception as e:
                        print(f"Error al copiar la carpeta {archivo}: {e}")
                elif respuesta == '2':
                    try:
                        shutil.copytree(ruta_origen, ruta_destino, dirs_exist_ok=True)
                        print(f"Carpeta fusionada: {archivo}")
                    except PermissionError:
                        print(f"No se pudo copiar la carpeta {archivo} debido a permisos insuficientes.")
                    except Exception as e:
                        print(f"Error al copiar la carpeta {archivo}: {e}")
                elif respuesta == '3':
                    print(f"La carpeta {archivo} se ha omitido.")
                    continue
                else:
                    print("Opción inválida. La carpeta se ha omitido.")
                    continue
            else:
                try:
                    shutil.copytree(ruta_origen, ruta_destino)
                    print(f"Carpeta copiada: {archivo}")
                except PermissionError:
                    print(f"No se pudo copiar la carpeta {archivo} debido a permisos insuficientes.")
                except Exception as e:
                    print(f"Error al copiar la carpeta {archivo}: {e}")
        else:
            print(f"Ignorando carpeta de sistema: {archivo}")

        contador += 1
        print(f"Progreso: {contador}/{total_archivos}")

if __name__ == "__main__":
    origen = input("Ingrese la ruta del directorio a copiar: ")
    destino = input("Ingrese la ruta del directorio de destino: ")

    if not os.path.isdir(origen):
        print("La ruta de origen no es un directorio válido.")
    else:
        copiar_archivos(origen, destino)
