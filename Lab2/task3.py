from mpi4py import MPI
import time

# Get my rank
comm = MPI.COMM_WORLD
size, rank = comm.Get_size(), comm.Get_rank()

if rank == 0:
    for i in range(1, size):
        data = MPI.COMM_WORLD.recv(source=i, tag=i)
        print(f"Time of receiving of message'{data[0]}' from rank {i} is {1000 * (time.time() - data[1]):.4f} ms")
else:
    message = "Text"
    cur_time = time.time()
    data = (message, cur_time)
    MPI.COMM_WORLD.send(data, dest=0, tag=rank)
