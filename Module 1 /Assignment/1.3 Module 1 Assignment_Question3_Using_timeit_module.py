import timeit

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
    no_of_time_to_execute = 1
    for problemSize in problem_size:
        
        pSize = int(problemSize.replace(',',''))
      
        execution_time = timeit.timeit(lambda: time_cost_efficiency_algorithm(pSize),
                    number=no_of_time_to_execute)
        average_time = execution_time/no_of_time_to_execute
        
        results.append({'problem_size': problemSize, 'time_interval': average_time})
    
    print()
    print(f"Problem Size\t\t\tSeconds")
    for r in results :
        print(f"{r.get('problem_size')}\t\t\t{r.get('time_interval'):.4f}\n")   


if __name__ == '__main__':
    main()