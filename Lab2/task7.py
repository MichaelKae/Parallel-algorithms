from mpi4py import MPI
from sys import getsizeof
import time

# Get info
comm = MPI.COMM_WORLD
size, rank = comm.Get_size(), comm.Get_rank()

N = 10

assert size == N, f"Number of workers is ({size}) and is not equal to {N}"

circle = list(range(N)) + [0]
message = "This text is too simple"

for i in range(N+1):
    if i == rank or i == rank+N:
        if i != 0:
            request = MPI.COMM_WORLD.irecv(source=circle[i-1], tag=i-1)
            message = request.wait()
            print(f"Message '{message}' has been recieved by {rank} from {circle[i-1]}.")
        if i != N:
            MPI.COMM_WORLD.send(message, dest=circle[i+1], tag=i)
            print(f"Message was sent from {rank} to {circle[i+1]}.")
