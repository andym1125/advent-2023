#include <stdio.h>
#include <ctype.h>

int isanydigit(char buffer[1000], int cursor) {
    if (isdigit(buffer[cursor])) {
        return buffer[cursor]-'0';
    }

    switch(buffer[cursor]) {
        case 'o': //1
            if (cursor+2 < 1000 &&
                buffer[cursor+1] == 'n' &&
                buffer[cursor+2] == 'e')
                return 1;
            return -1;
        case 't': //23
            if (cursor+2 < 1000 &&
                buffer[cursor+1] == 'w' &&
                buffer[cursor+2] == 'o')
                return 2;
            if (cursor+4 < 1000 &&
                buffer[cursor+1] == 'h' &&
                buffer[cursor+2] == 'r' &&
                buffer[cursor+3] == 'e' &&
                buffer[cursor+4] == 'e')
                return 3;
            return -1;
        case 'f': //45
            if (cursor+3 < 1000 &&
                buffer[cursor+1] == 'o' &&
                buffer[cursor+2] == 'u' &&
                buffer[cursor+3] == 'r')
                return 4;
            if (cursor+3 < 1000 &&
                buffer[cursor+1] == 'i' &&
                buffer[cursor+2] == 'v' &&
                buffer[cursor+3] == 'e')
                return 5;
            return -1;
        case 's': //67
            if (cursor+2 < 1000 &&
                buffer[cursor+1] == 'i' &&
                buffer[cursor+2] == 'x')
                return 6;
            
            if (cursor+4 < 1000 &&
                buffer[cursor+1] == 'e' &&
                buffer[cursor+2] == 'v' &&
                buffer[cursor+3] == 'e' &&
                buffer[cursor+4] == 'n')
                return 7;
            return -1;
        case 'e': //8
            if (cursor+4 < 1000 &&
                buffer[cursor+1] == 'i' &&
                buffer[cursor+2] == 'g' &&
                buffer[cursor+3] == 'h' &&
                buffer[cursor+4] == 't')
                return 8;
            return -1;
        case 'n': //9
            if(cursor+3 < 1000 &&
                buffer[cursor+1] == 'i' &&
                buffer[cursor+2] == 'n' &&
                buffer[cursor+3] == 'e')
                return 9;
            return -1;
        case 'z': //0
            if(cursor+3 < 1000 &&
                buffer[cursor+1] == 'e' &&
                buffer[cursor+2] == 'r' &&
                buffer[cursor+3] == 'o')
                return 0;
            return -1;
        default:
            return -1;
    }
}

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
            if (first == 0 && isanydigit(buffer, i) != -1) {
                first = isanydigit(buffer, i);
            }

            if (buffer[i] == '\n') {
                end = i-1;
                break;
            }
        }

        //Going backward, check for last num
        for (i = end; i >= 0; i--) {
            if (last == 0 && isanydigit(buffer, i) != -1) {
                last = isanydigit(buffer, i);
                break;
            }
        }

        sum += (first)*10+(last);
        printf("%d %d\n", (first)*10+(last), sum);
    }

    fclose(f);
}