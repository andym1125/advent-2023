#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

const RED = 12, GREEN = 13, BLUE = 14;

char *trim(char *str) {
    while(isspace((unsigned char)*str)) str++;

    if(*str == 0)  
        return str;

    char *end_str;
    end_str = str + strlen(str) - 1;
    while(end_str > str && isspace((unsigned char)*end_str)) end_str--;

    end_str[1] = '\0';

    return str;
}

int main() {

	char buffer[1000];
	FILE* f = fopen("input.txt", "r");
	char games[100][1000];
	int sum = 0;


	// Parse each game
	int i = 0;
	while(fgets(buffer, 1000, f) != NULL) {
		char *input = strtok(buffer, ":");
		char* game = strtok(NULL, ":");
		game = trim(game);
		strcpy(games[i], game);
		printf("%s\n", games[i]);
		i++;
		input = strtok(NULL, ":");
	}

	// each game, check the plays for calls larger than possible
	for(int game = 0; game < 100; game++)
	{
		int invalid = 0;
		char* colorPlay = strtok(games[game], ",;");
		while(colorPlay != NULL) {
			colorPlay = trim(colorPlay);
			int color = atoi(colorPlay);
			
			for(int i = 0; i < strlen(colorPlay); i++) {
				if(colorPlay[i] == 'd' && color > RED) { //d in red
					invalid = 1;
					printf("Invalidr: %d\n", color);

					break;
				} else if(colorPlay[i] == 'n' && color > GREEN) { //n in green
					printf("Invalidg: %d\n", color);
					invalid = 1;
					break;
				} else if(colorPlay[i] == 'b' && color > BLUE) { // b in blue
					invalid = 1;
					printf("Invalidb: %d\n", color);
					break;
				}
			}
			colorPlay = strtok(NULL, ",;");
		}

		if(invalid == 1)
			printf("Game %d: Invalid\n", game + 1);
		else {
			printf("Game %d: Valid\n", game + 1);
			sum += game+1;
		}

	}

	printf("Sum: %d\n", sum);

	fclose(f);
}
