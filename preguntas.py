"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    punto1 = 0;
    for i in data:
      punto1 += int(i[1])

    return punto1


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import collections
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    punto2 = [i[0] for i in data]
    punto2.sort()
    diccionario = collections.Counter(punto2)
    dict1 = diccionario.items()
    resultados = []
    for x, y in dict1:
        numero = str(y)
        resultados.append((x,y))
  
    return  resultados



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    p3 = [i[0] for i in data]
    p3 = list(set(p3))
    p3.sort()
    p33 = [[i[0], i[1]] for i in data]
    resultados = []
    for i in p3:
        suma = 0
        for o in p33:
            if (i in o):
               suma += int(o[1])
        resultados.append((str(i),suma))
    return resultados

    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import collections
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    p4 = [i[2].split('-')[1] for i in data]
    p4.sort()
    diccionario = collections.Counter(p4)
    dict1 = diccionario.items()
    resultados=[]
    for x, y in dict1:
        resultados.append((str(x),y))
    
    return resultados
    


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    p55 = [i[0] for i in data]
    p55 = list(set(p55))
    p55.sort()
    p5 = [[i[0], i[1]] for i in data]
    resultados=[]
    for i in p55:
      lista = []

      for o in p5:
          if (i in o):
            lista.append(o[1])
      resultados.append((i, int(max(lista)), int(min(lista))))

    return resultados
        
def pregunta_06():
    """
  La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
  una clave y el valor despues del caracter `:` corresponde al valor asociado a la
  clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
  grande computados sobre todo el archivo.
  Rta/
  [
      ("aaa", 1, 9),
      ("bbb", 1, 9),
      ("ccc", 1, 10),
      ("ddd", 0, 9),
      ("eee", 1, 7),
      ("fff", 0, 9),
      ("ggg", 3, 10),
      ("hhh", 0, 9),
      ("iii", 0, 9),
      ("jjj", 5, 17),
  ]
  """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    columna5 = [i[4].split(',') for i in data]
    punto6 = []
    for i in columna5:
      for o in i:
        punto6.append(o.split(':'))
    punto6
    p6 = []
    for i in punto6:
      p6.append(i[0])
    p6 = list(set(p6))
    p6.sort()
    respuesta = []
    for i in p6:
      lista = []
      for o in punto6:
        if (o[0] == i):
          lista.append(int(o[1]))
      re=str(i),int(min(lista)),int(max(lista))
      respuesta.append(re)
    return(respuesta)

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    columna2 = [i[1] for i in data]
    columna2 = list(set(columna2))
    columna2.sort()
    p7 = [[i[0], i[1]] for i in data]
    resuesta=[]
    for i in columna2:
      lista = []

      for o in p7:
        if (o[1] == i):
          lista.append(o[0])
      re=(int(str(i)),lista)
      resuesta.append(re)
    return(resuesta)
    


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    columna2 = [i[1] for i in data]
    columna2 = list(set(columna2))
    columna2.sort()
    p7 = [[i[0], i[1]] for i in data]
    respuesta = []
    for i in columna2:
      lista = []
      for o in p7:
        if (o[1] == i):
          lista.append(o[0])

      lista = list(set(lista))
      lista.sort()
      re = (int(str(i)), lista)
      respuesta.append(re)
    return(respuesta)
    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import collections
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    col5 = [i[4].split(',') for i in data]
    punto6 = []
    for i in col5:
      for o in i:
        punto6.append(o.split(':')[0])
    punto6.sort()
    diccionario = collections.Counter(punto6)
    dict1 = diccionario.items()
    respuesta = {}
    for x, y in dict1:
      respuesta[str(x)]=y
    return(respuesta)
        


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    respuesta=[]
    for i in data:
      re=str(i[0]),len(i[3].split(',')),len(i[4].split(','))
      respuesta.append(re)
    return(respuesta)
        


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    filas = [i[3].split(',') for i in data]
    filas
    letras= []
    for i in filas:
      for o in i:
        letras.append(o)
    letras = list(set(letras))
    letras.sort()
    p11 = [[i[1],i[3]]for i in data]
    respuesta={}
    for i in letras:
      cont = 0
      for o in p11:
        if (i in o[1]):
          cont += int(o[0])
          respuesta[str(i)] =cont
    return(respuesta)
        


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = open('data.csv', 'r').readlines()
    data = [i.replace('\n', '') for i in data]
    data = [i.split('\t') for i in data]
    data
    colum5 = [i[4].split(',') for i in data]
    l = [i[0] for i in data]
    sumas = []
    respuesta={}
    for i in colum5:
      cont=0
      for o in i:
        cont += int(o.split(':')[1])
      sumas.append(cont)

    for i in range(0, len(sumas)):
      if(str(l[i]) in respuesta):
        respuesta[str(l[i])]=respuesta[str(l[i])]+sumas[i]
      else:
        respuesta[str(l[i])]=sumas[i]

    return(respuesta)
