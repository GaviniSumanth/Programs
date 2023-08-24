mean <- 60
sd <- 8
x <- c(36:84)
y <- dnorm(x, mean, sd)
plot(x, y, type = "o", col = "green")
abline(v = mean, col = "black")
p1 <- pnorm(40, mean, sd, lower.tail = FALSE)
x1 <- c(10:84)
y1 <- dnorm(x1, mean, sd)
polygon(c(40, x1, 84), c(0, y1, 0), col = "red")

p2 <- pnorm(56, mean, sd)
x2 <- c(36:56)
y2 <- dnorm(x2, mean, sd)
polygon(c(36, x2, 56), c(0, y2, 0), col = "blue")
