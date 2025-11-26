#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_PHIL 5



void eat(int id) {
    sleep(rand() % 2 + 1); 
}


void *philosopher(void *num) {
    int id = *(int *)num;
    while (1) {
        printf("Philosopher %d is thinking...\n", id);
        sleep(rand() % 3 + 1);
       
        printf("Philosopher %d is hungry and tries to pick chopsticks...\n", id);
        printf("Philosopher %d picked chopsticks and is eating.\n", id);
        eat(id);
       
        printf("Philosopher %d finished eating and put down chopsticks.\n", id);
    }
}


int main() {
    pthread_t thread_id[NUM_PHIL];
    int phil_id[NUM_PHIL];

    for (int i = 0; i < NUM_PHIL; i++) {
        phil_id[i] = i;
        pthread_create(&thread_id[i], NULL, philosopher, &phil_id[i]);
    }

    for (int i = 0; i < NUM_PHIL; i++) {
        pthread_join(thread_id[i], NULL);
    }

    return 0;
}



