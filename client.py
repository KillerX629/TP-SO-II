import rpyc

#la conexión debe tener la dirección IP entre comillas
conn = rpyc.connect("localhost", port=18861)

#se usa conn.root para hacer las llamadas a servicios externos
#root trae el objeto raíz del servidor (en este caso el servicio)

print(conn.root.get_answer())
#se usa stop para cerrar la conexión
conn.root.stop()