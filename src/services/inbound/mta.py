import server 

if __name__ == "__main__":
    serverM = server.ServerSMTP( "0.0.0.0" , 3000 )
    serverM.start()