from TabuSearch import search
import TabuResultsHelper
import time

def main():
    # Vector = [1,2]
    # Problem Configuration
    berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
                [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
                [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
                [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
                [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
                [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
                [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
                [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
                [830,610],[605,625],[595,360],[1340,725],[1740,245]]
    optimalSolution = 7542
    csvFilename = 'BerlinSolutions.csv'
    resultList = []

    # EXECUTION 1
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 15
    maxCandidates = 50

    # Execute the algorithm
    startTime = time.time()
    solution = search(berlin52,maxIterations, maxTabuCount, maxCandidates)
    endTime = time.time()
    executionTime = endTime - startTime

    # Calculate algorithm efficacy in this execution
    efficacy = round(float((solution["cost"] - optimalSolution)/optimalSolution),2)

    # Round execution time and tour cost of the actual solution
    executionTime = round(executionTime, 2)
    tourCost = round(solution["cost"],2)

    # We add the result data to the results list
    result = {"maxIterations": maxIterations, "maxTabuCount": maxTabuCount,
     "maxCandidates": maxCandidates, "solution": tourCost, "efficacy": efficacy,
     "executionTime": executionTime}
    resultList.append(result)

    # EXECUTION 2
    # Algorithm Configuration
    maxIterations = 50
    maxTabuCount = 15
    maxCandidates = 50

    # Execute the algorithm
    startTime = time.time()
    solution = search(berlin52,maxIterations, maxTabuCount, maxCandidates)
    endTime = time.time()
    executionTime = endTime - startTime

    # Calculate algorithm efficacy in this execution
    efficacy = round(float((solution["cost"] - optimalSolution)/optimalSolution),2)

    # Round execution time and tour cost of the actual solution
    executionTime = round(executionTime, 2)
    tourCost = round(solution["cost"],2)

    # We add the result data to the results list
    result = {"maxIterations": maxIterations, "maxTabuCount": maxTabuCount,
     "maxCandidates": maxCandidates, "solution": tourCost, "efficacy": efficacy,
     "executionTime": executionTime}
    resultList.append(result)

    # EXECUTION 3
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 20
    maxCandidates = 45

    # Execute the algorithm
    startTime = time.time()
    solution = search(berlin52,maxIterations, maxTabuCount, maxCandidates)
    endTime = time.time()
    executionTime = endTime - startTime

    # Calculate algorithm efficacy in this execution
    efficacy = round(float((solution["cost"] - optimalSolution)/optimalSolution),2)

    # Round execution time and tour cost of the actual solution
    executionTime = round(executionTime, 2)
    tourCost = round(solution["cost"],2)

    # We add the result data to the results list
    result = {"maxIterations": maxIterations, "maxTabuCount": maxTabuCount,
     "maxCandidates": maxCandidates, "solution": tourCost, "efficacy": efficacy,
     "executionTime": executionTime}
    resultList.append(result)

    # Export all the results to a csv file
    TabuResultsHelper.exportResults(resultList,csvFilename)

    # We print the results
    TabuResultsHelper.printResults(resultList)




if __name__ == '__main__':
    main()
