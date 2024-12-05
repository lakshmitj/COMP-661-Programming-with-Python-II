import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time
        
def time_cost_efficiency_algorithm(problemSize):
    #Start the algorithm
    work = 1
    for x in range(problemSize):
        work += 5
        work -= 5
    #end of algorithm
    return work


    # Your algorithm here
problem_size = ['1,000,000' ,'3,000,000', '9,000,000', '27,000,000']
results = []
for size in problem_size:
    pSize = int(size.replace(',',''))
    with Timer() as t:
        work = time_cost_efficiency_algorithm(pSize) 
    results.append({'problem_size': size, 'time_interval':round(t.interval,4)})
    
print()
print(f"Problem Size\t\t\tSeconds")
for r in results :
    print(f"{r.get('problem_size')}\t\t\t{r.get('time_interval')}\n") 