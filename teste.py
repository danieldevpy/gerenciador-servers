import psutil

for proc in psutil.process_iter(['pid', 'name']):

    try:
        connections = proc.connections()
        for conn in connections:
            if conn.laddr.port == 80:
              
                print(conn)
                print(proc.pid)
            # if conn.laddr.port == port:
            #     proc.kill()
            #     return
    except psutil.AccessDenied:
        pass