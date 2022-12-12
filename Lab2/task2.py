from mpi4py import MPI
import numpy as np

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

# Define objects
class pair:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def num_sum(self):
        return self.number1 + self.number2

object1 = list(range(21))
object2 = pair(73, 37)
object3 = np.arange(12).reshape((3, 4))

list_of_objects = [object1, object2, object3]

if rank == 0:
    data = list_of_objects
else:
    data = None

data = MPI.COMM_WORLD.scatter(data, root=0)
print(f"Rank {rank} shows data:\n{data}\n")