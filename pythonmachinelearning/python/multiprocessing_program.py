#multi processing is the act of running multiple processes parallely in different cpu cores
import multiprocessing 
import time 
import math

result1=[]
result2=[]
result3=[]

def calc1(numbers):
    for number in numbers:
        result1.append(math.sqrt(number**3))

def calc2(numbers):
    for number in numbers:
        result2.append(math.sqrt(number**4))

def calc3(numbers):
    for number in numbers:
        result1.append(math.sqrt(number**5))
if __name__=="__main__":
  numbers= list(range(50000000))
  i = input("Enter 1 to run in single process or 2 to run in multiple processes: ")
  if i == "1":
        start_time = time.time()
        calc1(numbers)
        calc2(numbers)
        calc3(numbers)
        
        end_time = time.time()
        print("Single process time:", end_time - start_time)
  elif i == "2":
        p1 = multiprocessing.Process(target=calc1, args=(numbers,))
        p2 = multiprocessing.Process(target=calc2, args=(numbers,))
        p3 = multiprocessing.Process(target=calc3, args=(numbers,))
        start_time = time.time()

        p1.start()
        p2.start()
        p3.start()
       
        

        end_time = time.time()
        print("Multiple processes time:", end_time - start_time)


    



    