# Algoritmo inútil que resta billetes de 100,10 y 1 a un monto dado.
import time
def entrega_billetes_2(monto):
  billete=100
  inc=0
  billete_actual=billete/(10**inc)
  while(monto>0):
    if monto >= billete_actual:
      monto=monto-billete_actual
    else:
      inc=inc+1
      billete_actual=billete/(10**inc)
def prueba_tiempos(a,b,c):
	print(f"para los param:{a}, {b} ,{c}")
	start = time.time()
	for i in range(a,b,c):
		entrega_billetes_2(i)
	end = time.time()
	print(end - start)
	return (end-start)
sum=prueba_tiempos(0,100,10)
sum+=prueba_tiempos(100,1000,100)
sum+=prueba_tiempos(1000,10000,1000)
sum+=prueba_tiempos(10000,100000,10000)
sum+=prueba_tiempos(100000,1000000,100000)
print(f"el total de tiempo fue:{sum}")