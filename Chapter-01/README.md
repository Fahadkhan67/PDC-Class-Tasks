**Prime Number Multithreading and Multiprocessing Comparison**

This project checks how much time a Prime Number Checker program takes to run when we use different numbers of threads and processes.
<br>

We tested it with 5, 10, and 15 threads and processes to compare performance.
<br>

**🧵 Multithreading Results:**
<br>
Threads	Time Taken
<br>
🧵 Threads: 5 | Time taken: 0.9086 seconds
<br>
🧵 Threads: 10 | Time taken: 1.4564 seconds
<br>
🧵 Threads: 15 | Time taken: 2.1721 seconds

**⚙️ Multiprocessing Results:**
<br>
Processes	Time Taken
<br>
⚙️ Processes: 5 | Time taken: 0.6560 seconds
<br>
⚙️ Processes: 10 | Time taken: 1.1960 seconds
<br>
⚙️ Processes: 15 | Time taken: 1.6283 seconds

**📊 Comparison Summary:**
<br>
In this project, multithreading and multiprocessing were tested for prime number checking on a large set of numbers.
<br>
The multithreading results show that increasing the number of threads does not reduce the execution time much.
<br>
This is because Python threads are limited by the Global Interpreter Lock (GIL), which prevents true parallel CPU execution.
<br>
On the other hand, multiprocessing gave much better results.
<br>
As the number of processes increased, the total execution time decreased, because each process runs independently on different CPU cores.

**✅ Conclusion:**
<br>
Multithreading is not efficient for CPU-heavy programs like prime number checking because it cannot use multiple cores effectively.
<br>
Multiprocessing is much faster for this type of computation since it runs each process in parallel on separate cores.
<br>
When dealing with CPU-intensive tasks, multiprocessing gives better performance and reduces total computation time.
<br>
However, for simple or I/O-based tasks, multithreading can still be a good choice.
