def load(filename):
    """
    Carga un archivo de diccionario de palabras y devuelve una lista de palabras.
    
    Args:
    filename (str): El nombre del archivo de diccionario.
    
    Returns:
    list: Una lista de palabras cargadas desde el archivo.
    """
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  # Elimina espacios en blanco y saltos de línea
            word_list.append(word)
    return word_list
