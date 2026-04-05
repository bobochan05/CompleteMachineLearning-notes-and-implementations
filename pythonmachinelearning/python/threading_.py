#thread is a flow of execution.like a separate program. each thread take a running time.
#GIL is a global interpreter lock. it is used to prevent multiple threads from executing at once 
#for a cpu bound task that is program waits most of the time for internal events, we use multiprocessing.
#for a io bound task that is program waits most of the time for external events, we use multithreading.

i=input("enter 1 for single thread and 2 for multithreading :")
match i:
     case '1':
        import threading
        import time 

        def brush():
         print("brushing teeth")
        time.sleep(2) #delays execution for 2 seconds
        print("done brushing teeth")
    
        def breakfast():
         print("making breakfast")
         time.sleep(3) #delays execution for 3 seconds
         print("done making breakfast")
    
        def study():
         print("studying") 
         time.sleep(4) #delays execution for 4 seconds
         print("done studying")

        brush()
        breakfast()
        study()

     case '2':
        import threading 
        import time 
        def brush():
            
            time.sleep(2)  # delays execution for 2 seconds
            print("done brushing teeth")
        def breakfast():
            
            time.sleep(3)
            print("done making breakfast")
        def study():
            
            time.sleep(4)
            print("done studying")
        #creating threads
        #we create separate threads for each function so now 3 threads will run simultaneously
        t1=threading.Thread(target=brush)
        t2=threading.Thread(target=breakfast)
        t3=threading.Thread(target=study)
        t1.start()
        t2.start()
        t3.start()

#daemon thread is a thread that runs in the background and does not block the main program from exiting.
#ex- background task , garbage collection, etc.
#eq - a daemon thread can be used to count how many seconds a user is logged in to a program.





    
