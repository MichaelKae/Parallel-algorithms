#include <iostream>
#include <omp.h>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);
    double time_for_one_tread;
    double** a = new double* [n];
    double** b = new double* [n];
    double** c = new double* [n];

    for (int i = 0; i < n; ++i)
    {
        a[i] = new double[n];
        b[i] = new double[n];
        c[i] = new double[n];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            a[i][j] = (double(rand()) / RAND_MAX);
            b[i][j] = (double(rand()) / RAND_MAX);
        }
    }

    for (int num = 1; num <= 10; num++)
    {
        for (int i = 0; i < num; i++)
        {
            for (int j = 0; j < n; j++)
            {
                c[i][j] = 0;
            }
        }

        double exec_start_time = omp_get_wtime();

        #pragma omp parallel for num_threads(num)
        for (int k = 0; k < n; k++)
        {
            for (int j = 0; j < n; j++)
            {
                for (int i = 0; i < n; i++)
                {
                    c[i][j] = c[i][j] + a[i][k] * b[k][j];
                }
            }
        }

        double exec_time = (double)(omp_get_wtime() - exec_start_time);
        if (num == 1)
        {
          time_for_one_tread = exec_time;
        }
        double efficiency = time_for_one_tread / exec_time;
        printf("The number of threads: %d; The execution time: %.10f; Efficiency: %.10f\n", num, exec_time, efficiency);
    }
    return 0;
}
