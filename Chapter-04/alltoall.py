from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

send_data = (rank + 1) * np.arange(size, dtype=int)
recv_data = np.empty(size, dtype=int)

comm.Alltoall(send_data, recv_data)

print(f"Process {rank} sending {send_data} receiving {recv_data}")
