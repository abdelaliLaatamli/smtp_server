from DS import SingletonMeta
from exception_handlers import OverQuataEonnectionException
import queue
from threading import Thread

class ConnectionQueue(metaclass=SingletonMeta):
    
    __connectionthreads={}
    __queueConnections=queue.Queue(2000)
    __server_qouta = 2000


    def addConnectionthread( self , connection_thread:Thread ):
       
        if( len( self.__connectionthreads ) < self.__server_qouta ):
            connection_thread.start()
            self.__connectionthreads[connection_thread.ident] = connection_thread
            return

        if( self.__queueConnections.qsize() < self.__server_qouta ):
            self.__queueConnections.put( connection_thread )
            return

        raise OverQuataEonnectionException(" The service connection is full , try later please")


    def dequeue_connection( self , connection_thread_pid:int):
        self.__connectionthreads.pop( connection_thread_pid )
        if( self.__queueConnections.qsize() > 0 and len( self.__connectionthreads ) < self.__server_qouta ):
            queued_connection_thread = self.__queueConnections.get()
            queued_connection_thread.start()
            self.__connectionthreads[queued_connection_thread.ident] = queued_connection_thread
        print( len(self.__connectionthreads) )

            




        



    
    
