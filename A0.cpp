#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    int words_amount = 0;
    bool flag = true;

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (argv[1][i] == ' ' || argv[1][i] == '\t' || argv[1][i] == '\n' || argv[1][i] == '\r')
        {
            flag = true;
        }

        else if (flag == true)
        {
            flag = false;
            words_amount += 1;
        }
    }

    if (argc > 1)
    {
        printf("This string contains %d words!", words_amount);
    }

    else
    {
        printf("This string contains 0 words!");
    }
}
