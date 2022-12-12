from mpi4py import MPI
import time

def sleep_for(tm=10):
    time.sleep(tm)

def cur_time(tm):
    return time.asctime(time.localtime(tm))

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    print(f"Rank {rank} is - {cur_time(time.time())}")
    sleep_for()
    print(f"Rank {rank} is - {cur_time(time.time())}\n")
    message = MPI.COMM_WORLD.recv(source=1, tag=0)
    print(f"Rank {rank} received message:")
    print(f"'{message}' which translates to '{cur_time(message)}'")
    print(f"from {(time.time() - message):.2f} sec ago")

# this program will work only with single worker
if rank == 1:
    # this is worker
    sheldons_number = [
"The best number is 73.",
"Why? 73 is the 21st prime number.",
"Its mirror, 37, is the 12th and its mirror, 21,",
"is the product of multiplying 7 and 3.",]
    message = time.time()
    req = MPI.COMM_WORLD.isend(message, dest=0, tag=0)
    for item in sheldons_number:
        print(item)
        sleep_for(0.25)