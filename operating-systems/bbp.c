#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int counter = 0;

void *producer(void *param){
	int item_produced = 1;
	while (1){
		while (counter == BUFFER_SIZE);
		buffer[in] = item_produced;
		in = (in + 1)%BUFFER_SIZE;
		counter++;

		printf("producer produced an item, counter is: %d\n", counter);
		sleep(1);
	}
}


void *consumer(void * param){
	while (1){
		while(counter == 0);
		int item = buffer[out];
		out = (out+1)%BUFFER_SIZE;
		counter--;
		sleep(2);
		printf("Consumer consumed %d items, count: %d\n", item, counter);
	}
}

int main(){

	pthread_t thread1, thread2;

	pthread_create(&thread1, NULL, producer, NULL);
	pthread_create(&thread2, NULL, consumer, NULL);

	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);

	return 0;

}


