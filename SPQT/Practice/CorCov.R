dataset <- read.csv("Practice/data/COVARIANCE -CORRELATION-DATASET.csv")
m1 <- as.numeric(dataset$M1)
m1_len <- length(m1)
s1 <- as.numeric(dataset$S1)
s1_len <- length(s1)
cov <- sum(m1 * s1) / m1_len - mean(m1) * mean(s1)
cor <- cov / (sqrt(var(m1)) * sqrt(var(s1)))
plot(
    m1,
    s1,
    main = "Correlation b/w M1,S1",
    xlab = "M1", ylab = "S1",
    col = "red"
)
