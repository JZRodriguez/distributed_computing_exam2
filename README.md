# Distributed Computing Exam 2

![Alt text](https://github.com/JZRodriguez/distributed_computing_exam1/blob/main/ENES%20UNAM.jpg 'Enes logo')

## Student 
* Jadiel Zuñiga Rodriguez


## Introduction
This repository is part of Distributed Computing's exam 2 of the school ENES Morelia


## Results
![Alt text](https://github.com/JZRodriguez/distributed_computing_exam2/blob/main/latency_graph.png 'Latency')



## Requirements
* subprocess
* re
* matplotlib
* sys



## Code
The way the [test_exam.py](https://github.com/JZRodriguez/distributed_computing_exam2/blob/main/test_exam.py) file works is by calling the functions located in the [exam.py](https://github.com/JZRodriguez/distributed_computing_exam2/blob/main/exam.py) file. Those functions create a test file that contains the amount of megabytes asked and gets the time that it takes to upload the file to the specified IP.

After getting the data needed, the code plots the data into a line graph, since is the one that represents the change in time for upload the best, and saves the figure as png file.



## Instructions
* On an enviroment with the required libraries as specified above, run the python file named [test_exam.py](https://github.com/JZRodriguez/distributed_computing_exam2/blob/main/test_exam.py) with the next structure:

> python3 test_exam.py 10 100 10 [IP]

* Get the result on the current directory


## Reference
* de la Luz, V. (s. f.). Cómputo en la Nube. Classroom. Recuperado 11 de junio de 2022, de https://classroom.google.com/u/0/c/NDY4ODc2ODY4MTA2
