# 2 dice are rolled 15 times,fin the probability of sum 9
# 1) Exactly 8 times
# 2) Atmost 6 times
# 3) Atleast 9 times
n <- 15
p <- 4 / 36
lambda <- n * p
p1 <- dpois(8, lambda)
p2 <- ppois(6, lambda, lower.tail = TRUE)
p3 <- ppois(9, lambda, lower.tail = FALSE)

# 5 coins are tossed 10 times,fin the probability of exactly 3 heads
# 1) No occurances
# 2) Atmost 6 times
# 3) Atleast 2 times
n <- 10
p <- 10 / 32
lambda <- n * p
p1 <- dpois(0, lambda)
p2 <- ppois(6, lambda, lower.tail = TRUE)
p3 <- ppois(2, lambda, lower.tail = FALSE)

# Probability of being defective is 20% there are 15 times
# 1)None are defective
# 2)Atmost 10 are defective
# 3)Aleast 1 is defective
n <- 15
p <- 20 / 100
lambda <- n * p
p1 <- dpois(0, lambda)
p2 <- ppois(10, lambda, lower.tail = TRUE)
p3 <- ppois(1, lambda, lower.tail = FALSE)

# --------------- Common Code ---------------
x <- c(0:15)
y <- dpois(x, lambda)
z <- ppois(x, lambda)
plot(
    x,
    y,
    main = "Poisson Probability",
    xlab = "Poisson Random Variables",
    ylab = "Probability",
    type = "h",
    col = "violet"
)
plot(
    x,
    z,
    main = "Poisson Probability",
    xlab = "Poisson Random Variables",
    ylab = "Probability",
    type = "s",
    col = "blue"
)
