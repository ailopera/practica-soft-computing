''' berlin52.py: Programa para generar las soluciones del problema berlin52
    en base a las estrategias/configuraciones definidas.
    @author: Ana Isabel Lopera Martinez
    @author: Pedro del Pozo Jimenez
'''
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
    csvFilename = 'BerlinSolutionsV2.csv'
    resultList = []

    # Lo pongo en varios bucles para separar por estrategias.
    # PRIMERA ESTRATEGIA: Objetivos:
    # - Baja diversidad
    # - Memoria moderada
    maxIterationsList = [100,100,100,130,130,130,170,170,170,200,200,200]
    maxTabuCountList = [20,60,100,20,60,100,20,60,100,20,60,100]
    maxCandidates = 30

    for maxIterations,maxTabuCount in zip(maxIterationsList,maxTabuCountList):
        # Execution
        result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
        resultList.append(result)


    # SEGUNDA ESTRATEGIA: Objetivos:
    # - Alta diversidad
    # - Memoria moderada
    # maxIterationsList = [100,100,100,130,130,130,170,170,170,200,200,200]
    # maxTabuCountList = [20,60,100,20,60,100,20,60,100,20,60,100]
    maxCandidates = 100

    for maxIterations,maxTabuCount in zip(maxIterationsList,maxTabuCountList):
        # Execution
        result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
        resultList.append(result)

    # TERCERA ESTRATEGIA: Objetivos:
    # - Baja diversidad
    # - Memoria alta
    # maxIterationsList = [100,100,100,130,130,130,170,170,170,200,200,200]
    maxTabuCountList = [140,160,200,140,160,200,140,160,200,140,160,200]
    maxCandidates = 30

    for maxIterations,maxTabuCount in zip(maxIterationsList,maxTabuCountList):
        # Execution
        result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
        resultList.append(result)

    # CUARTA ESTRATEGIA: Objetivos:
    # - Alta diversidad
    # - Memoria alta
    maxTabuCountList = [140,160,200,140,160,200,140,160,200,140,160,200]
    maxCandidates = 100

    for maxIterations,maxTabuCount in zip(maxIterationsList,maxTabuCountList):
        # Execution
        result = TabuResultsHelper.tabuSearch(berlin52, maxIterations,maxTabuCount, maxCandidates, optimalSolution)
        resultList.append(result)

    # Export all the results to a csv file
    TabuResultsHelper.exportResults(resultList,csvFilename)

    # We print the results
    TabuResultsHelper.printResults(resultList)



if __name__ == '__main__':
    main()
