library(stats)
library(ggplot2)
library(graphics)
library(plotly)

#Esto es una prueba con numeros aleatorios para generar un linechar, se debería hacer con los csv generados desde python


datos_Tabu = read.csv("BerlinSolutions2.csv", header = TRUE)

#datos_TabuNormalizados = datos_Tabu[, datos_Tabu$maxIterations/max(datos_Tabu$maxIterations)]

datos_TabuEnOrden <- datos_Tabu[with(datos_Tabu, order(datos_Tabu$executionTime)), ]

datos_TabuNormalizados <- datos_Tabu

for(i in 1:length(datos_TabuNormalizados)){
  datos_TabuNormalizados[, i] <- datos_TabuNormalizados[, i]/max(datos_TabuNormalizados[, i])
}


#x <- c(1:100)
#random_y <- rnorm(100, mean = 0)
#data <- data.frame(x, random_y)

#pruebaGrafico1 <- plot_ly(datos_TabuNormalizados, x = datos_TabuNormalizados$executionTime, y = datos_TabuNormalizados$solution, type = 'scatter', mode = 'lines+markers')

pruebaPlot1 <- plot_ly(datos_TabuNormalizados, name = 'executionTime', x = datos_TabuNormalizados$executionTime, y = datos_TabuNormalizados$solution, type = 'scatter', mode = 'markers')
pruebaPlot1 <- add_trace(p = pruebaPlot1, data = datos_TabuNormalizados, x = datos_TabuNormalizados$maxIterations, name = 'maxIterations', type = 'scatter', mode = 'markers')
pruebaPlot1 <- add_trace(p = pruebaPlot1, data = datos_TabuNormalizados, x = datos_TabuNormalizados$maxTabuCount, name = 'maxIteramaxTabuCounttions', type = 'scatter', mode = 'markers')
pruebaPlot1 <- add_trace(p = pruebaPlot1, data = datos_TabuNormalizados, x = datos_TabuNormalizados$maxCandidates, name = 'maxCandidates', type = 'scatter', mode = 'markers')
pruebaPlot1 <- add_trace(p = pruebaPlot1, data = datos_TabuNormalizados, x = datos_TabuNormalizados$efficacy, name = 'efficacy', type = 'scatter', mode = 'markers')
add_trace(p = pruebaPlot1, data = datos_TabuNormalizados, x = datos_TabuNormalizados$solution, name = 'solution', type = 'scatter', mode = 'markers')
