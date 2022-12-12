from mpi4py import MPI
import numpy as np

# Get info
comm = MPI.COMM_WORLD
size, rank = comm.Get_size(), comm.Get_rank()

if rank == 0:
    num = int(10e5)
    
    vector1, vector2 = np.random.random(num), np.random.random(num)

    message1, message2 = np.array_split(vector1, size-1), np.array_split(vector2, size-1)
    
    for worker in range(size-1):
        req1 = MPI.COMM_WORLD.isend(message1[worker], dest=worker+1, tag=worker+1)
        req2 = MPI.COMM_WORLD.isend(message2[worker], dest=worker+1, tag=worker+1001)

    dot_prod = 0

    for worker in range(size-1):
        dot_prod += MPI.COMM_WORLD.recv(source=worker+1, tag=worker+2001)

    print(f"Total product is {dot_prod:.3f}")

else:
    # workers
    array1, array2 = MPI.COMM_WORLD.recv(source=0, tag=rank), MPI.COMM_WORLD.recv(source=0, tag=rank+1000)
    result = np.dot(array1, array2)
    print(f"Worker {rank} sum is {result:.4f}")

    res = MPI.COMM_WORLD.isend(result, dest=0, tag=rank+2000)