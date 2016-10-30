library(plotly)
library(stats)
library(ggplot2)
library(graphics)

#Esto es una prueba con numeros aleatorios para generar un linechar, se debería hacer con los csv generados desde python


#datos_Tabu = read.csv("ejemploSalida1.csv", header = TRUE)

x <- c(1:100)
random_y <- rnorm(100, mean = 0)
data <- data.frame(x, random_y)

pruebaGrafico1 = plot_ly(data, x = ~x, y = ~random_y, type = 'scatter', mode = 'lines')
