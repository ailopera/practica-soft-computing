from TabuSearch import search
import time
import csv

# TabuResultsHelper Proporciona metodos para exportar las soluciones al csv

def tabuSearch(nodes, maxIterations, maxTabuCount, maxCandidates, optimalSolution):

    # Execute the algorithm
    startTime = time.time()
    solution = search(nodes,maxIterations, maxTabuCount, maxCandidates)
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

    return result

# Escribe los resultados en el fichero csv seleccionado
def exportResults(resultList,filename):
    csvHeader = "maxIterations,maxTabuCount, maxCandidates, solution, efficacy, executionTime"
    with open(filename, 'w') as csvfile:
        fieldnames = ['maxIterations', 'maxTabuCount', 'maxCandidates', 'solution','efficacy','executionTime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        # Para cada resultado de la lista (resultList es una lista de diccionarios),
        # se escribe en el csv de resultados
        for result in resultList:
            writer.writerow(result)

# Imprime los resultados por pantalla (util mientras probamos con los parametros para buscar la mejor configuracion)
def printResults(resultList):
    for result in resultList:
        print "PARAMETERS"
        print "- maxIterations: " + str(result["maxIterations"])
        print "- maxTabuCount: " + str(result["maxTabuCount"])
        print "- maxCandidates: " + str(result["maxCandidates"])
        print "-------------------------------------------------"
        print "SOLUTION: " + str(result["solution"])
        print "- Execution time: " + str(result["executionTime"])
        print "- Efficacy (Error): " + str(result["efficacy"])
        print "################################################"
