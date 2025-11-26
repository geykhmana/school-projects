#include "kernel/types.h"
#include "kernel/stat.h"
#include "user/user.h"

int main(void) {
  int pid1 = fork();
  if (pid1 == 0) {
    printf("Child 1 started (pid = %d)\n", getpid());
    for (volatile int i = 0; i < 300000000; i++);  
    printf("Child 1 finished\n");
    exit(0);
  }
  yield();

  int pid2 = fork();
  if (pid2 == 0) {
    printf("Child 2 started (pid = %d)\n", getpid());
    for (volatile int i = 0; i < 200000000; i++);  
    printf("Child 2 finished\n");
    exit(0);
  }
  yield();

  int pid3 = fork();
  if (pid3 == 0) {
    printf("Child 3 started (pid = %d)\n", getpid());
    for (volatile int i = 0; i < 100000000; i++);  
    printf("Child 3 finished\n");
    exit(0);
  }

  wait(0);
  wait(0);
  wait(0);
  printf("Parent done.\n");
  exit(0);
}

