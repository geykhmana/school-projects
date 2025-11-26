
void timer_isr(){
	ticks++;
	printf("Interrupt Service Routine Timer tick value: %d\n", ticks);
}

int main(){
	struct sigaction sigfunc = {0};
	sigfunc.sa_handler = timer_isr;
	sigemptyset(&sigfunc.sa_mask);
	sigfunc.sa_flags = SA_RESTART;

	if (sigaction(SIGALRM, &sigfunc, NULL) == -1){
		perror("Signal function error");
		return 1;
	}

	struct itimerval interval_timer = {0};
	interval_timer.it_interval.tv_sec = 0;
	interval_timer.it_interval.tv_usec = 250000; //250 ms
	interval_timer.it_value.tv_sec = 0;
	interval_timer.it_value.tv_usec = 250000;

	if(setitimer(ITIMER_REAL, &interval_timer, NULL) == -1){
		perror("Timer failed");
		return 1;
	}

	printf("PID = %d timer interrupts every 250ms\n", getpid());
	for (int i = 0; i < 20; i++) {
		printf("main thread working: i=%d, ticks = %d\n", i, ticks);
		usleep(180000); //180ms

	}

	printf("Done\n");
	return 0;

}