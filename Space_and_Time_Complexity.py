                                     # EXPRESSED AS THE BIG O
# time complexity is the run time required by an algorithm or a program to run
#  as the output size increases

                                             # THE CONSTANT O(1)
# It is used when we have a specific operation that can be performed in a fixed number of steps

import timeit

def print_first_element(lst):
    print(lst[0])

# Measure execution time for [1, 2, 3, 4, 5]
time_taken = timeit.timeit(lambda: print_first_element([1, 2, 3, 4, 5]), number=1)
print("Time taken for [1, 2, 3, 4, 5]:", time_taken)

# Measure execution time for [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
time_taken = timeit.timeit(lambda: print_first_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), number=1)
print("Time taken for [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:", time_taken)

                                            # THE LINEAR O(N)
# An algorithm with linear time complexity has a running time that increases propotionately with the input size
import time
def print_list_item(lst):
    for item in lst:
      print(item)   


start_time = time.time()
#calling the function outside the function
print_list_item([1, 2, 3, 4])
end_time = time.time()
print("Time taken for [1, 2, 3, 4]:", end_time - start_time)


start_time = time.time()
#calling the function outside the function
print_list_item([1, 2, 3, 4, 5, 6, 7, 8])
end_time = time.time()
print("Time taken for [1, 2, 3, 4, 5, 6, 7, 8]:", end_time - start_time)                             

                            # Quadratic Time Complexity O(N**2) this men N raised to power 2
# It has a running time that increases quadratically with the input size
# it usually occurs within nested loops                          
def print_list_item(lst):
   for i in lst:
      for j in lst:
         print(i, j)


start_time = time.time()
#calling the function outside the function
print_list_item([1, 2])
end_time = time.time()  
print("Time taken for [1, 2]:", end_time - start_time)        

start_time = time.time()
#calling the function outside the function
print_list_item([1, 2, 3,4])
end_time = time.time()   
print("Time taken for [1, 2, 3, 4, 5, 6, 7, 8]:", end_time - start_time)  