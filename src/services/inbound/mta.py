from ServerSMTP import ServerSMTP


if __name__ == "__main__":
    server = ServerSMTP( "0.0.0.0" , 3000 )
    server.start()