import time

def time_cost_efficiency_algorithm(problemSize):
    #Start the algorithm
    work = 1
    for x in range(problemSize):
        work += 5
        work -= 5
    #end of algorithm
    return work

def main():
    
    problem_size = ['1,000,000' ,'3,000,000', '9,000,000', '27,000,000']
    results = []
    for size in problem_size:
        pSize = int(size.replace(',',''))
        start_time = time.time()
        time_cost_efficiency_algorithm(pSize)
        end_time = time.time()
        time_interval = end_time - start_time 
        results.append({'problem_size': size, 'time_interval': time_interval})
    
    print()
    print(f"Problem Size\t\t\tSeconds")
    for r in results :
        print(f"{r.get('problem_size')}\t\t\t{r.get('time_interval'):.4f}\n")   


if __name__ == '__main__':
    main()