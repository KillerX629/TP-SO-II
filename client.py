import rpyc

#la conexión debe tener la dirección IP entre comillas
conn = rpyc.connect("localhost", port=18861)


print(conn.root.get_answer())
conn.root.stop()