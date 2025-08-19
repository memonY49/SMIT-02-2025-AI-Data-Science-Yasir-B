from datetime import datetime as dt
import  functools
today = dt.now()



class callcount:
    def __init__(self, func):
        functools.update_wrapper(self,func)
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count +=1
        print(f"Function: {self.func.__name__} is called: {self.count} ")
        return self.func(*args,**kwargs)
    # def __str__(self):
    #     return f"Result is: {self.func}"


def logger(func):
    def wrapper(*args,**kwargs):
        with open("log.txt", 'a') as log_file:
            running_log = f"{dt.now()} Running '{func.__name__}'.....\n"
            log_file.write(running_log)
            result = func(*args,**kwargs)
            finished_log = f"{dt.now()} Finished '{func.__name__}'.....\n"
            log_file.write(finished_log)
        return result
    return wrapper



def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args,*kwargs)
                if result == 5:
                    return result
                    break

            else:
                with open("log.txt", 'a') as log_file:
                    log_file.write(f"{func.__name__} is called 3 times and the function is now blocked....")
        return wrapper
    return decorator


@repeat(2)
@logger
@callcount
def add(a, b):
    # input()
    return a+b

@logger
@repeat(1)
@callcount
def sub(a,b):
    return a-b

print(add(1,4))
sub(6,1)