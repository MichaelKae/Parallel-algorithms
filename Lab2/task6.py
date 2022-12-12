from mpi4py import MPI
from sys import getsizeof
import time

# Get info
comm = MPI.COMM_WORLD
size, rank = comm.Get_size(), comm.Get_rank()

N = 10

if rank == 0:

    for sheldon_iq in range(51):
        obj = [3773]*(1000*sheldon_iq + 1)
        L = getsizeof(obj) # size in bytes
    
        T = time.time()
        for j in range(N):
            MPI.COMM_WORLD.send(obj, dest=1, tag=1000*sheldon_iq+j)
            obj = MPI.COMM_WORLD.recv(source=1, tag=1000*sheldon_iq+j+1)
        T = time.time() - T
    
        print(f"Object {L} size (bytes):    {((2 * N * L * 10e-6) / T):.2f} MB/s")

elif rank == 1:
    # only one worker
    for sheldon_iq in range(51):
        for i in range(N):
            mes = MPI.COMM_WORLD.recv(source=0, tag=1000*sheldon_iq+i)
            MPI.COMM_WORLD.send(mes, dest=0, tag=1000*sheldon_iq+i+1)

