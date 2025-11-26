#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_PHIL 5 

typedef enum { THINKING, HUNGRY, EATING } State;

pthread_mutex_t mutex;
pthread_cond_t condition[NUM_PHIL];
State state[NUM_PHIL];

void eat(int i) {
    printf("Philosopher %d is eating.\n", i);
    sleep(rand() % 2 + 1);
    printf("Philosopher %d finished eating and put down chopsticks.\n", i);
}

void test(int i) {
	if (state[i] == HUNGRY &&
	state[(i + 4) % NUM_PHIL] != EATING &&
	state[(i + 1) % NUM_PHIL] != EATING) {
		state[i] = EATING;
        	pthread_cond_signal(&condition[i]);
        }
}

void pickup(int i) {
	pthread_mutex_lock(&mutex);
	state[i] = HUNGRY;
	test(i);
	while (state[i] != EATING) {
    		pthread_cond_wait(&condition[i], &mutex);
    	}
    	pthread_mutex_unlock(&mutex);
}

void putdown(int i) {
	pthread_mutex_lock(&mutex);
	state[i] = THINKING;
	test((i + 4) % NUM_PHIL);
	test((i + 1) % NUM_PHIL);
	pthread_mutex_unlock(&mutex);
}




void *philosopher(void *num) {
    int i = *(int *)num;
    while (1) {
        printf("Philosopher %d is thinking...\n", i);
        sleep(rand() % 3 + 1);
       
        pickup(i);
        eat(i);
        putdown(i);
    }
}


int main() {
    pthread_t thread_id[NUM_PHIL];
    int phil_id[NUM_PHIL];
   
    pthread_mutex_init(&mutex, NULL);
    for (int i = 0; i < NUM_PHIL; i++) {
        pthread_cond_init(&condition[i], NULL);
        state[i] = THINKING;
        phil_id[i] = i;
        pthread_create(&thread_id[i], NULL, philosopher, &phil_id[i]);
    }

    for (int i = 0; i < NUM_PHIL; i++) {
        pthread_join(thread_id[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    for (int i = 0; i < NUM_PHIL; i++) {
        pthread_cond_destroy(&condition[i]);
    }
   
    return 0;
}
