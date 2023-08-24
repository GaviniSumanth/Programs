iris <- read.csv("Practice/data/Iris.csv")
pl <- iris$PetalLengthCm
# Mean
pl_mean <- sum(pl) / length(pl)
pl_mean <- mean(pl)
# Median
pl_median <- quantile(pl, 0.5)
pl_median <- median(pl)
# Mode
pl_table <- table(pl)
pl_mode <- names(pl_table)[pl_table == max(pl_table)]

# Range
pl_range <- max(pl) - min(pl)
# Coefficient of range
pl_coef_range <- pl_range / (max(pl) + min(pl))

# Quartile deviation
pl_q1 <- quantile(pl, 0.25)
pl_q3 <- quantile(pl, 0.75)
pl_qd <- (pl_q3 - pl_q1) / 2
pl_qd <- IQR(pl) / 2
# Mean Absolute Deviation
pl_md <- mad(pl, center = mean(pl))
# Variance
pl_var <- sum((pl - mean(pl))^2) / length(pl)
pl_var <- var(pl)
# Standard Deviation
pl_sd <- sqrt(pl_var)
# Covariance
pl_cov <- (pl_sd / mean(pl)) * 100


# Frequency Distributions
dataset <- read.csv("Practice/data/Problem Sheet.csv")
xi <- dataset$Xi
f1 <- dataset$f1
data1 <- data.frame(xi, f1, xi * f1, xi^2 * f1)
totals1 <- c(sum(xi), sum(f1), sum(xi * f1), sum(xi^2 * f1))
data_table1 <- rbind(data1, totals1)
row.names(data_table1)[length(xi) + 1] <- "Total"
x_bar1 <- sum(xi * f1) / sum(f1)
x_var1 <- (sum(xi^2 * f1) / sum(f1)) - x_bar1^2
x_sd1 <- sqrt(x_var1)
x_cov1 <- (x_sd1 / x_bar1) * 100
