import algo1 

def search(Array,element):
  #Busca un elemento en el Array 
  encontrado=0
  for i in range(0,len(Array)):
    if Array[i]==element:
      encontrado=1
      return i
  if  encontrado==0:
    return None
    
def insert(Array,element,position):
  #Inserta un elemento en una posición determinada de un Array
  dim=len(Array)
  vectorResultado= algo1.Array(dim,0)
  if len(Array)>position:
    print("Se pudo insertar correctamente en la posc: ",position)
    for i in range(0,dim):
      if i<position:
        vectorResultado[i]=Array[i]
      elif i==position:
        vectorResultado[i]=element
      else:
        vectorResultado[i]=Array[i-1]
  else:
    return None
  if position>=dim:
    return None
  for i in range(0,dim):
    Array[i]=vectorResultado[i]
  return position
 
  
def delete(Array,element):
  #Elimina un elemento del arreglo
  Encontrado=False
  n=len(Array)
  for i in range(0,n):
    if Array[i]==element and Encontrado==False :
        print("El elemento a eliminar se encuentra en la poscicion: ",i)
        Encontrado=True
        indice=i
  if Encontrado==False:
    return None
  else:
    for i in range(indice,n):
      if i+1 < n:
        Array[i]=Array[i+1]
      else:
        Array=None
    return indice
def length(Array):
  #Calcula el número de elementos activos que hay en la secuencia
  contador=0
  for i in range(0,len(Array)):
    if Array[i] != None:
      contador+=1
  return contador
      