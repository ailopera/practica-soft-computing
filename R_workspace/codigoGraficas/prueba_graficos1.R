library(stats)
library(ggplot2)
library(graphics)
library(plotly)



datos_berlin = read.csv("BerlinSolutions.csv", header = TRUE)
datos_att48 = read.csv("att48Solutions.csv", header = TRUE)
datos_a280 = read.csv("a280Solutions.csv", header = TRUE)

#Visualización de Berlin
berlin_fase1 <- datos_berlin[1:12,]
berlin_fase2 <- datos_berlin[13:24,]
berlin_fase3 <- datos_berlin[25:36,]
berlin_fase4 <- datos_berlin[37:48,]

plot_berlin <- plot_ly(berlin_fase1, x = berlin_fase1$executionTime, y = berlin_fase1$solution, type = 'scatter', name ='estrategia 1', mode = 'markers', color = I('red'))
plot_berlin <- add_trace(p = plot_berlin, data = berlin_fase2, x = berlin_fase2$executionTime, y = berlin_fase2$solution, name = 'estrategia 2', type = 'scatter', mode = 'markers', color = I('pink'))
plot_berlin <- add_trace(p = plot_berlin, data = berlin_fase3, x = berlin_fase3$executionTime, y = berlin_fase3$solution, name = 'estrategia 3', type = 'scatter', mode = 'markers', color = I('purple'))
add_trace(p = plot_berlin, data = berlin_fase4, x = berlin_fase4$executionTime, y = berlin_fase4$solution, name = 'estrategia 4', type = 'scatter', mode = 'markers', color = I('blue'))

#Visualización de att48
att48_fase1 <- datos_att48[1:12,]
att48_fase2 <- datos_att48[13:24,]
att48_fase3 <- datos_att48[25:36,]
att48_fase4 <- datos_att48[37:48,]

plot_att48 <- plot_ly(att48_fase1, x = att48_fase1$executionTime, y = att48_fase1$solution, type = 'scatter', name ='estrategia 1', mode = 'markers', color = I('red'))
plot_att48 <- add_trace(p = plot_att48, data = att48_fase2, x = att48_fase2$executionTime, y = att48_fase2$solution, name = 'estrategia 2', type = 'scatter', mode = 'markers', color = I('pink'))
plot_att48 <- add_trace(p = plot_att48, data = att48_fase3, x = att48_fase3$executionTime, y = att48_fase3$solution, name = 'estrategia 3', type = 'scatter', mode = 'markers', color = I('purple'))
add_trace(p = plot_att48, data = att48_fase4, x = att48_fase4$executionTime, y = att48_fase4$solution, name = 'estrategia 4', type = 'scatter', mode = 'markers', color = I('blue'))

#Visualización de a280
a280_fase1 <- datos_a280[1:12,]
a280_fase2 <- datos_a280[13:24,]
a280_fase3 <- datos_a280[25:36,]
a280_fase4 <- datos_a280[37:48,]

plot_a280 <- plot_ly(a280_fase1, x = a280_fase1$executionTime, y = a280_fase1$solution, type = 'scatter', name ='estrategia 1', mode = 'markers', color = I('red'))
plot_a280 <- add_trace(p = plot_a280, data = a280_fase2, x = a280_fase2$executionTime, y = a280_fase2$solution, name = 'estrategia 2', type = 'scatter', mode = 'markers', color = I('pink'))
plot_a280 <- add_trace(p = plot_a280, data = a280_fase3, x = a280_fase3$executionTime, y = a280_fase3$solution, name = 'estrategia 3', type = 'scatter', mode = 'markers', color = I('purple'))
add_trace(p = plot_att48, data = a280_fase4, x = a280_fase4$executionTime, y = a280_fase4$solution, name = 'estrategia 4', type = 'scatter', mode = 'markers', color = I('blue'))

