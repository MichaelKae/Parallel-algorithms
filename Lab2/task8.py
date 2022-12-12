from mpi4py import MPI
import time

def sleep_for(tm=25):
    full_time = int(tm/5)
    for i in range(full_time):
        time.sleep(5)
        print("Please, wait...")
    rest = tm % 5
    time.sleep(rest)

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    # master
    message0 = "I feel... cold"
    MPI.COMM_WORLD.isend(message0, dest=1, tag=0)
    sleep_for()
    message1 = MPI.COMM_WORLD.recv(source=1, tag=1)
    print(f"Master {rank} received Doctor message '{message1}'")

# this program will work only with single worker
if rank == 1:
    # worker
    message0 = MPI.COMM_WORLD.recv(source=0, tag=0)
    print(f"Doctor {rank} received Master message '{message0}'")
    message1 = message0 + " back"
    MPI.COMM_WORLD.isend(message1, dest=0, tag=1)
    print(f"Message '{message1}' by Doctor {rank} was sent to Master")

