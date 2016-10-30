import csv

# TabuResultsHelper Proporciona metodos para exportar las soluciones al csv
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
