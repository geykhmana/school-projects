#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

#define NUM_READERS 5
#define NUM_WRITERS 2

int shared_data = 0;
int read_count = 0;

sem_t mutex;
sem_t rw_mutex;

void *reader(void *arg){
	int id = *((int*)arg);
	while (1){
		sem_wait(&mutex);
		read_count++;
		if (read_count == 1) {
			sem_wait(&rw_mutex);
		}
		sem_post(&mutex);
		printf("Reader %d is reading: %d\n", id, shared_data);
		sleep(1);
		
		sem_wait(&mutex);
		read_count--;
		if (read_count == 0) {
			sem_post(&rw_mutex);
		}
		sem_post(&mutex);
		sleep(1);
	}
}

void *writer(void *arg){
	int id = *((int*)arg);
	while(1){
		sem_wait(&rw_mutex);
		shared_data += 1;
		printf("Writer %d wrote: %d\n", id, shared_data);
		sleep(2);
		sem_post(&rw_mutex);
		sleep(2);
	}
}

int main(){
	pthread_t readers[NUM_READERS];
	pthread_t writers[NUM_WRITERS];
	
	sem_init(&mutex, 0, 1);
	sem_init(&rw_mutex, 0, 1);

	int ids[NUM_READERS];

	for (int i = 0; i < NUM_READERS; i++){
		ids[i] = i+1;
		pthread_create(&readers[i], NULL, reader, &ids[i]);
	}

	for (int i = 0; i < NUM_WRITERS; i++){
		ids[i] = i+1;
        pthread_create(&writers[i], NULL, writer, &ids[i]);
        }

	for (int i = 0; i < NUM_READERS; i++){
		pthread_join(readers[i], NULL);
	}

	for (int i = 0; i < NUM_WRITERS; i++){
        pthread_join(writers[i], NULL);
        }

	return 0;
}

