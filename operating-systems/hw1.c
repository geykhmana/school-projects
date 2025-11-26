#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/timer.h>
#include <linux/uaccess.h> 



static struct timer_list my_timer;
void timer(struct timer_list *t);


void timer(struct timer_list *t) { 
 
 mod_timer(&my_timer, jiffies + msecs_to_jiffies(1000));

  
}



static ssize_t proc_read(struct file *file, char __user *buf, size_t len, loff_t *offset) {
    static int completed = 0;
    const char *message = ""; 
    size_t message_len = strlen(message);

    if (completed) {
        completed = 0; 
        return 0; 
    }

    if (copy_to_user(buf, message, message_len)) {
        return -EFAULT;
    }

    completed = 1; 
    return message_len;
}


static const struct proc_ops proc_ops = {
    .proc_read = proc_read,
};



int counter_module_init(void) {
	
    	timer_setup(&my_timer, timer, 0);
    	mod_timer(&my_timer, jiffies + msecs_to_jiffies(1000));
	

    return 0;
}



void counter_module_exit(void) {
	
	del_timer(&my_timer);
    	
}

