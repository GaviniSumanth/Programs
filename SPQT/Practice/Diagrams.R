data1 <- sample(10000, 300, replace = TRUE)
data2 <- sample(5, 300, replace = TRUE)

# Histogram
hist1 <- hist(
    data1,
    main = "Histogram",
    xlab = "Observation",
    ylab = "Frequency",
    xlim = c(0, 15000),
    ylim = c(0, 60),
    col = rainbow(10)
)
text(hist1$mids, hist1$counts)
# Barplot
bar1 <- barplot(
    data1,
    main = "Barplot",
    xlab = "Observation",
    ylab = "Frequency",
    col = rainbow(100)
)
# Barplot (Contingency table)
bar_contingency1 <- barplot(
    matrix(data1, nrow = 30, ncol = 10, byrow = TRUE),
    main = "Barplot (Contingency table)",
    xlab = "Groups",
    ylab = "Counts",
    col = rainbow(100)
)
# Boxplot
box1 <- boxplot(
    data1,
    main = "Boxplot",
    xlab = "Observation",
    ylab = "Count",
    col = rainbow(100)
)
# Density plot
density1 <- plot(
    density(data1),
    main = "Density Plot",
    xlab = "Observation",
    ylab = "Relative Frequency",
    col = "blue",
    lwd = 3
)
# Pie Charts (2d)
table2 <- table(data2)
pie_percentage <- round(table2 / sum(table2) * 100, 2)
labels <- c("L1", "L2", "L3", "L4", "L5")
pie2 <- pie(
    table2,
    main = "Pie Chart",
    labels = paste(labels, pie_percentage, "%"),
    col = rainbow(10)
)
legend("topright", labels, ce = 2, fill = rainbow(10))
# Pie Charts (3d)
library(plotrix)
table2 <- table(data2)
pie_percentage <- round(table2 / sum(table2) * 100, 2)
labels <- c("L1", "L2", "L3", "L4", "L5")
pie2 <- pie3D(
    table2,
    main = "3D Pie Chart",
    labels = paste(labels, pie_percentage, "%"),
    explode = 0.2,
    radius = 1.2,
    labelcex = 2,
    col = rainbow(10, alpha = 0.7)
)
legend("topright", labels, ce = 2, fill = rainbow(10))
