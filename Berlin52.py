import TabuResultsHelper

def main():
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

    # PRIMERA ESTRATEGIA: Objetivo: disminuir la diversidad
    # - Aumentamos las penalizaciones Tabu
    # - Disminuimos los candidatos que se generan en cada iteracion
    # Cada vez le damos menos margen de variabilidad

    # # EXECUTION 1
    # #Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 15
    # maxCandidates = 50
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)

    # # EXECUTION 2
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 20
    # maxCandidates = 45
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)

    # # EXECUTION 3
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 25
    # maxCandidates = 40
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)
    #
    # # EXECUTION 4
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 30
    # maxCandidates = 35
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)
    #
    #
    # # SEGUNDA ESTRATEGIA: Objetivo: aumentar la diversidad
    # # - Disminuimos las penalizaciones Tabu
    # # - Aumentamos los candidatos que se generan en cada iteracion a 52, y lo dejamos fijo
    #
    # # EXECUTION 5
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 12
    # maxCandidates = 52
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)
    #
    # # EXECUTION 6
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 10
    # maxCandidates = 52
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)
    #
    # # EXECUTION 7
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 7
    # maxCandidates = 52
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)
    #
    # # EXECUTION 8
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 5
    # maxCandidates = 52
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)
    #
    # # EXECUTION 9
    # # Algorithm Configuration
    # maxIterations = 100
    # maxTabuCount = 3
    # maxCandidates = 52
    # # Execution
    # result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    # resultList.append(result)

    # TERCERA ESTRATEGIA: Objetivo: optimizar las mejores configuraciones
    # - Disminuimos/aumentamos el numero de iteraciones en las mejores configuraciones
    # Cogemos una de cada estrategia

    # EXECUTION 10
    # Algorithm Configuration
    maxIterations = 50
    maxTabuCount = 3
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 11
    # Algorithm Configuration
    maxIterations = 70
    maxTabuCount = 3
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 12
    # Algorithm Configuration
    maxIterations = 120
    maxTabuCount = 3
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 13
    # Algorithm Configuration
    maxIterations = 150
    maxTabuCount = 3
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)


    # Mejor solucion primera estrategia
    # EXECUTION 14
    # Algorithm Configuration
    maxIterations = 50
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 14
    # Algorithm Configuration
    maxIterations = 70
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 15
    # Algorithm Configuration
    maxIterations = 120
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)


    # EXECUTION 15
    # Algorithm Configuration
    maxIterations = 150
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 15
    # Algorithm Configuration
    maxIterations = 160
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)


    # EXECUTION 15
    # Algorithm Configuration
    maxIterations = 170
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # Export all the results to a csv file
    TabuResultsHelper.exportResults(resultList,csvFilename)

    # We print the results
    TabuResultsHelper.printResults(resultList)



if __name__ == '__main__':
    main()
