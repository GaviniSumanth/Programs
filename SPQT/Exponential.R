mean <- 3
theta <- 1 / mean
a1 <- pexp(2.9, theta, lower.tail = FALSE)
a2 <- pexp(3.6, theta)
a3 <- pexp(
    2.6,
    theta,
    lower.tail = FALSE
) - pexp(
    3.4,
    theta,
    lower.tail = FALSE
)
x <- seq(0, 20, by = 0.05)
y <- dexp(x, theta)
z <- pexp(x, theta)
plot(x, y)
plot(x, z)
