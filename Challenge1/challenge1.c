#include <stdio.h>
#include <ctype.h>

int main() {
    char buffer[1000];
    int end = 0;
    char first, last;
    int i = 0;
    int sum = 0;

    FILE* f = fopen("input.txt", "r");
    
    while (fgets(buffer, 1000, f) != NULL) {
        first = 0;
        last = 0;
        end = 0;

        //Going forward, check for first num, then end
        for (i = 0; i < 1000; i++) {
            if (first == 0 && isdigit(buffer[i])) {
                first = buffer[i];
            }

            if (buffer[i] == '\n') {
                end = i-1;
                break;
            }
        }

        //Going backward, check for last num
        for (i = end; i >= 0; i--) {
            if (last == 0 && isdigit(buffer[i])) {
                last = buffer[i];
                break;
            }
        }

        sum += (first-'0')*10+(last-'0');
        printf("%d %d\n", (first-'0')*10+(last-'0'), sum);
    }

    fclose(f);
}