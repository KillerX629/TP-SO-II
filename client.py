import rpyc

conn = rpyc.connect("localhost", port=18861)


print(conn.root.get_answer())
conn.root.stop()