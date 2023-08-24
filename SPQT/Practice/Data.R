# Ungrouped to Grouped
data <- sample(100, 10, replace = TRUE)
l <- length(data)
r <- range(data)
bins <- seq(r[1], r[2], by = 10)
class_interval <- cut(data, bins, right = FALSE)
table <- table(class_interval)
transform(table)
