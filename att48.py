import TabuResultsHelper

def main():
    att48 = [[6734,1453],[223, 10], [5530, 1424], [401, 841], [3082, 1644],
         [7608, 4458], [7573, 3716], [7265, 1268], [6898, 1885],
         [1112, 2049], [5468, 2606],[5989, 2873], [4706, 2674],
         [4612, 2035], [6347, 2683], [6107, 669], [7611, 5184],
         [7462, 3590], [7732, 4723], [5900, 3561], [4483, 3369],
         [6101, 1110], [5199, 2182], [1633, 2809], [4307, 2322],
         [675, 1006], [7555, 4819],  [7541, 3981], [3177, 756],
         [7352, 4506], [7545, 2801], [3245, 3305], [6426, 3173],
         [4608, 1198], [23, 2216], [7248, 3779], [7762, 4595],
         [7392, 2244], [3484, 2829], [6271, 2135], [4985, 140],
         [1916, 1569], [7280, 4899], [7509, 3239], [10, 2676],
         [6807, 2993], [5185, 3258],[3023, 1942]
        ]
    optimalSolution = 10628
    csvFilename = 'att48Solutions.csv'
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

    # EXECUTION 2
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 20
    maxCandidates = 45
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 3
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 25
    maxCandidates = 40
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 4
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 30
    maxCandidates = 35
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)


    # SEGUNDA ESTRATEGIA: Objetivo: aumentar la diversidad
    # - Disminuimos las penalizaciones Tabu
    # - Aumentamos los candidatos que se generan en cada iteracion a 52, y lo dejamos fijo

    # EXECUTION 5
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 12
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 6
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 10
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 7
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 7
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 8
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 5
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 9
    # Algorithm Configuration
    maxIterations = 100
    maxTabuCount = 3
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # TERCERA ESTRATEGIA: Objetivo: optimizar las mejores configuraciones
    # - Disminuimos/aumentamos el numero de iteraciones en las mejores configuraciones

    # Mejor solucion segunda estrategia
    # EXECUTION 10
    # Algorithm Configuration
    maxIterations = 70
    maxTabuCount = 3
    maxCandidates = 52
    # Execution
    result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
    resultList.append(result)

    # EXECUTION 11
    # Algorithm Configuration
    maxIterations = 50
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

    # Export all the results to a csv file
    TabuResultsHelper.exportResults(resultList,csvFilename)

    # We print the results
    TabuResultsHelper.printResults(resultList)
