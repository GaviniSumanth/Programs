# X is a normal random variable
# E(X) = 50, sigma_x=10
# 1) P(X < 35)
# 2) P(X < 60)
# 3) P(X > 28)
# 4) P(X > 67)
# 5) P(30 < X < 60)
# 6) P(55 < X < 75)
exp_x <- 50
sigma_x <- 10
# 1
p1 <- pnorm(35, exp_x, sigma_x, lower.tail = TRUE)
x1 <- c(20:35)
y1 <- dnorm(x1, exp_x, sigma_x)
x <- c((exp_x - 3 * sigma_x):(exp_x + 3 * sigma_x))
y <- dnorm(x, exp_x, sigma_x)
plot(
    x,
    y,
    main = "Probability with Mean = 50",
    xlab = "Random Variables",
    ylab = "Probability",
    type = "o",
    col = "violet"
)
polygon(c(20, x1, 35), c(0, y1, 0), col = "red")
# 2
p2 <- pnorm(60, exp_x, sigma_x, lower.tail = TRUE)
x2 <- c(20:60)
y2 <- dnorm(x2, exp_x, sigma_x)
x <- c((exp_x - 3 * sigma_x):(exp_x + 3 * sigma_x))
y <- dnorm(x, exp_x, sigma_x)
plot(
    x,
    y,
    main = "Probability with Mean = 50",
    xlab = "Random Variables",
    ylab = "Probability",
    type = "o",
    col = "violet"
)
polygon(c(20, x2, 60), c(0, y2, 0), col = "red")
# 3
p3 <- pnorm(28, exp_x, sigma_x, lower.tail = FALSE)
x3 <- c(28:80)
y3 <- dnorm(x3, exp_x, sigma_x)
x <- c((exp_x - 3 * sigma_x):(exp_x + 3 * sigma_x))
y <- dnorm(x, exp_x, sigma_x)
plot(
    x,
    y,
    main = "Probability with Mean = 50",
    xlab = "Random Variables",
    ylab = "Probability",
    type = "o",
    col = "violet"
)
polygon(c(28, x3, 80), c(0, y3, 0), col = "red")
# 4
p4 <- pnorm(67, exp_x, sigma_x, lower.tail = FALSE)
x4 <- c(67:80)
y4 <- dnorm(x4, exp_x, sigma_x)
x <- c((exp_x - 3 * sigma_x):(exp_x + 3 * sigma_x))
y <- dnorm(x, exp_x, sigma_x)
plot(
    x,
    y,
    main = "Probability with Mean = 50",
    xlab = "Random Variables",
    ylab = "Probability",
    type = "o",
    col = "violet"
)
polygon(c(67, x4, 80), c(0, y4, 0), col = "red")
# 5
p5 <- pnorm(60, exp_x, sigma_x, lower.tail = TRUE) - pnorm(30, exp_x, sigma_x, lower.tail = TRUE)
x5 <- c(30:60)
y5 <- dnorm(x5, exp_x, sigma_x)
x <- c((exp_x - 3 * sigma_x):(exp_x + 3 * sigma_x))
y <- dnorm(x, exp_x, sigma_x)
plot(
    x,
    y,
    main = "Probability with Mean = 50",
    xlab = "Random Variables",
    ylab = "Probability",
    type = "o",
    col = "violet"
)
polygon(c(30, x5, 60), c(0, y5, 0), col = "red")
# 6
p6 <- pnorm(75, exp_x, sigma_x, lower.tail = TRUE) - pnorm(55, exp_x, sigma_x, lower.tail = TRUE)
x6 <- c(55:75)
y6 <- dnorm(x6, exp_x, sigma_x)
x <- c((exp_x - 3 * sigma_x):(exp_x + 3 * sigma_x))
y <- dnorm(x, exp_x, sigma_x)
plot(
    x,
    y,
    main = "Probability with Mean = 50",
    xlab = "Random Variables",
    ylab = "Probability",
    type = "o",
    col = "violet"
)
polygon(c(55, x6, 75), c(0, y6, 0), col = "red")
