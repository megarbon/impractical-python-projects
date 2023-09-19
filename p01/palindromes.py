#Como las rutas relativas me daban problemas he usado absolutas pero este bloque podria no usarse
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join("H:\DEV23\python-book\p01", "d5.txt")

try:
    # Abre el archivo en modo de lectura ('r' significa read) donde va file_path se puede poner 'ruta_relativa' y borrar el bloque de arriba
    with open(file_path, 'r') as diccionario:
        contenido = diccionario.read().strip().split('\n')
    
    # Ahora contenido contiene el contenido del archivo
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe. Verifica la ruta y el nombre del archivo.")
except IOError as e:
    print(f"Ocurrió un error al abrir el archivo: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# Algoritmo de búsqueda de palíndromos, recorre la lista y hace 'reverse slicing' a cada palabra comparando la palabra con la inversa.
pali_list = []  # Inicializa la lista para almacenar los palíndromos

for palabra in contenido:
    if len(palabra) > 1 and palabra == palabra[::-1]:
        pali_list.append(palabra)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
