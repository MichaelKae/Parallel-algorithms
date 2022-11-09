#include <iostream>
#include <omp.h>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv)
{
    int len = atoi(argv[1]);
    double* array = new double[len];

    for (int i = 0; i < len; i++)
    {
        array[i] = (double(rand()) / RAND_MAX);
    }

    for (int num = 1; num <= 10; num++)
    {
        double max_value = array[0];
        double start_time_stamp = omp_get_wtime();

	#pragma omp parallel for num_threads(num) reduction(max:max_value)
        for (int j = 0; j < len; j++)
        {
            max_value = max(max_value, array[j]);
        }

	double total_time = (double)(omp_get_wtime() - start_time_stamp);
        printf("The number of threads: %d;The execution time: %.10f.\n", num, total_time);
    }
    return 0;
}
