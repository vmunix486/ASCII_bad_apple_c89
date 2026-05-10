/* C89 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

#define MAX_FILE_SIZE 1048576
#define MAX_FRAMES 5000
#define FRAME_RATE 10
#define RUN_TIME 218

int main(void)
{
    FILE *f;
    char *buffer;
    char *frames[MAX_FRAMES];
    long file_size;
    int frame_count = 0;
    char *p;
    struct timeval start, now;
    double elapsed;
    int frame_index;
    int i;

    /* Open file */
    f = fopen("play.txt", "r");
    if (f == NULL) {
        printf("Could not open play.txt\n");
        return 1;
    }

    /* Get file size */
    fseek(f, 0, SEEK_END);
    file_size = ftell(f);
    rewind(f);

    /* Allocate memory */
    buffer = (char *)malloc(file_size + 1);
    if (buffer == NULL) {
        printf("Out of memory\n");
        fclose(f);
        return 1;
    }

    /* Read file */
    fread(buffer, 1, file_size, f);
    buffer[file_size] = '\0';
    fclose(f);

    /* Replace '.' with spaces */
    for (i = 0; buffer[i] != '\0'; i++) {
        if (buffer[i] == '.')
            buffer[i] = ' ';
    }

    /* Split frames by "SPLIT" */
    frames[frame_count++] = buffer;

    p = buffer;
    
    while ((p = strstr(p, "SPLIT")) != NULL) {
	/* end current frame */
        *p = '\0';
	/* Move to next frame */
        p += strlen("SPLIT");

        if (frame_count < MAX_FRAMES)
            frames[frame_count++] = p;
    }

    /* start = time(NULL);*/
    gettimeofday(&start, NULL);

    while (1) {
        /* elapsed = (double)(clock() - start) / CLOCKS_PER_SEC; */
	/* elapsed = difftime(time(NULL), start); */
	gettimeofday(&now, NULL);

	elapsed =
		(now.tv_sec - start.tv_sec) +
        (now.tv_usec - start.tv_usec) / 1000000.0;

        if (elapsed >= RUN_TIME)
            break;

        frame_index = (int)(elapsed * FRAME_RATE);

        if (frame_index >= 0 && frame_index < frame_count) {

            /* Clear screen */
#ifdef _WIN32
            system("cls");
#else
            system("clear");
#endif

            printf("%s\n", frames[frame_index]);
        }

        /* Sleep about 50ms */
#ifdef _WIN32
        system("ping -n 1 -w 50 localhost > nul");
#else
        system("sleep 0.05");
#endif
    }

    free(buffer);

    return 0;
}
