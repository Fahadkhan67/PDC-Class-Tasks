# 🖥️ Python Multiprocessing Project

This project demonstrates **Python multiprocessing** using multiple scripts, covering **process creation, naming, spawning, killing, daemon behavior, synchronization, and process pools**. All examples use a common computational function `do_something()`.

---

## ⚙️ 1. `naming_processes.py`

**Purpose:**
Create and **name processes explicitly** and observe execution and timing.

**Key Code:**

```python
process_with_name = multiprocessing.Process(
    name='do_something process 1',
    target=do_something,
    args=(1000, out_list1)
)
process_with_default_name = multiprocessing.Process(
    target=do_something,
    args=(1000, out_list2)
)
```

**Sample Output:**

```
Process 1 output list length: 1000
Process 2 output list length: 1000
Total execution time: 0.43 seconds
```

**Observation:**
Both processes executed concurrently. Execution time was significantly reduced compared to sequential execution.

---

## ⚙️ 2. `spawning_processes.py`

**Purpose:**
Dynamically **spawn multiple processes** using a loop.

**Key Code:**

```python
for i in range(6):
    process = multiprocessing.Process(target=myFunc, args=(i,))
    process.start()
    process.join()
```

**Sample Output:**

```
calling do_something from process no: 0
Process 0 finished with 0 results.
...
Process 5 finished with 5000 results.
```

**Observation:**
Processes executed independently; workload scaled linearly with `i`.

---

## ⚙️ 3. `killing_processes.py`

**Purpose:**
Demonstrates how to **start, terminate, and join a process** safely.

**Key Code:**

```python
p.start()
print('Process running:', p.is_alive())
p.terminate()
print('Process terminated:', p.is_alive())
p.join()
print('Process joined:', p.is_alive())
```

**Sample Output:**

```
Process running: True
Starting function (do_something)
Finished function with 10 results
Process terminated: False
Process joined: False
Process exit code: 0
```

**Observation:**
Shows safe lifecycle management using `.start()`, `.terminate()`, and `.join()`.

---

## ⚙️ 4. `run_background_processes_no_daemons.py`

**Purpose:**
Demonstrates **daemon vs non-daemon processes**.

**Key Code:**

```python
background_process.daemon = True
NO_background_process.daemon = False
```

**Sample Output:**

```
Starting background_process
---> 0
---> 1
---> 2
Starting NO_background_process
Results from do_something(): [0.0, 1.0, 2.0]
Exiting background_process
Exiting NO_background_process
```

**Observation:**
Daemon processes terminate with the main program; non-daemon processes complete independently.

---

## ⚙️ 5. `processes_barrier.py`

**Purpose:**
Demonstrates **process synchronization** using `Barrier` and `Lock`.

**Key Code:**

```python
synchronizer = Barrier(2)
serializer = Lock()
Process(name='p1 - test_with_barrier',
        target=test_with_barrier,
        args=(synchronizer, serializer)).start()
```

**Sample Output:**

```
process p3 - test_without_barrier ----> 2025-11-01 00:27:31
p3 - test_without_barrier results: [0.0, 1.0]
process p2 - test_with_barrier ----> 2025-11-01 00:27:31
p2 - test_with_barrier results: [0.0, 1.0]
```

**Observation:**
Barrier ensures all processes wait for each other; Lock guarantees orderly execution.

---

## ⚙️ 6. `process_pool.py`

**Purpose:**
Demonstrates **parallel execution using `multiprocessing.Pool`**.

**Key Code:**

```python
inputs = list(range(0,10))
pool = multiprocessing.Pool(processes=4)
pool_outputs = pool.map(do_something, inputs)
```

**Sample Output:**

```
Pool: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Observation:**
Work efficiently distributed among 4 processes; each input processed concurrently.

---

## 🧮 Summary Table

| Script                                 | Purpose                        | Success | Key Observation                               |
| -------------------------------------- | ------------------------------ | ------- | --------------------------------------------- |
| naming_processes.py                    | Process naming & execution     | ✅       | Concurrent execution; reduced runtime         |
| spawning_processes.py                  | Spawn processes dynamically    | ✅       | Independent execution; scalable workload      |
| killing_processes.py                   | Start, terminate, join process | ✅       | Proper lifecycle management                   |
| run_background_processes_no_daemons.py | Daemon vs non-daemon           | ✅       | Daemon terminated early; non-daemon completed |
| processes_barrier.py                   | Barrier & Lock synchronization | ✅       | Ordered execution; synchronized results       |
| process_pool.py                        | Parallel execution using Pool  | ✅       | Efficient concurrent results computation      |

---

## 🧩 Conclusion

* Multiprocessing enables **true parallelism** for CPU-bound tasks.
* Process naming and synchronization help **manage and debug concurrency**.
* Lifecycle management with `.start()`, `.terminate()`, and `.join()` ensures safety.
* Daemon processes terminate with the main program; non-daemon processes continue independently.
* Process pools and barriers provide structured ways to **manage and coordinate concurrent workloads**.

---

## 🧠 Overall Learning

Python’s `multiprocessing` module provides **robust and flexible parallel computation**.
Understanding process behavior, synchronization, daemonization, and pooling is essential for **efficient and robust concurrent applications**.

