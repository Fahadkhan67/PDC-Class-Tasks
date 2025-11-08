# 🧵 Thread Synchronization in Python

This project demonstrates **thread synchronization** in Python using four different mechanisms from the `threading` module: **Lock, RLock, Semaphore, and Condition**. Each example ensures that multiple threads safely share resources without causing **race conditions**.

The examples use a common computational function from `do_something.py`.

---

## 🔒 1. Lock

**Purpose:** Ensures exclusive access — only one thread can modify the shared resource at a time.

**File:** `Lock.py`

**Behavior Observed:**

```
Thread 0 started.
Thread 0 finished.
Thread 1 started.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Lock): 21
```

**Result:** Sequential execution of threads; safe access to the shared list.

---

## 🔑 2. RLock (Reentrant Lock)

**Purpose:** Allows the same thread to acquire the lock multiple times safely.

**File:** `RLock.py`

**Behavior Observed:**

```
Thread 0 started.
Thread 0 finished.
Thread 1 started.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (RLock): 21
```

**Result:** Similar to Lock; safe access with **nested locking** capability.

---

## 🟢 3. Semaphore

**Purpose:** Limits the number of threads that can access a resource simultaneously.

**File:** `Semaphore.py`

**Behavior Observed:**

```
Thread 0 waiting for permit...
Thread 0 started.
Thread 1 waiting for permit...
Thread 2 waiting for permit...
Thread 1 started.
Thread 0 finished.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Semaphore): 21
```

**Result:** Threads run in controlled batches; data integrity maintained.

---

## 🔔 4. Condition

**Purpose:** Allows threads to wait for a **specific condition** before proceeding.

**File:** `Condition.py`

**Behavior Observed:**

```
Thread 0 notifying condition.
Thread 1 notifying condition.
Thread 2 notifying condition.
Monitor: Current length = 7
Monitor: Current length = 14
Monitor: Current length = 21
```

**Result:** Threads coordinate via signaling; monitor tracks progress correctly.

---

## 📊 Comparison Table

| Mechanism | Main Use                          | Behavior                  | Safety | Best For                     |
| --------- | --------------------------------- | ------------------------- | ------ | ---------------------------- |
| Lock      | Exclusive access                  | Sequential execution      | ✅ Safe | General thread safety        |
| RLock     | Reentrant lock for nested locking | Similar to Lock           | ✅ Safe | Nested locks                 |
| Semaphore | Limits concurrent access          | Controlled parallelism    | ✅ Safe | Limited resources management |
| Condition | Waits for specific events/signals | Event-driven coordination | ✅ Safe | Producer-consumer models     |

---

## 🚀 How to Run

Run each file separately to observe its synchronization behavior:

```bash
python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
```

---

## 🏁 Conclusion

All four mechanisms successfully:

* Prevent **race conditions**
* Maintain data integrity
* Produce the expected output

**Guideline for use:**

* **Lock / RLock:** Use for simple mutual exclusion
* **Semaphore:** Use when limiting concurrent threads
* **Condition:** Use for threads coordination based on signals/events

