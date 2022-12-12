from mpi4py import MPI
import sys

N = 5

comm = MPI.COMM_WORLD.Spawn(sys.executable, args=['worker.py'], maxprocs=N)

for i in range(N):
    data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
    print(f"Worker {data} sent message '{data}'")

comm.Disconnect()
