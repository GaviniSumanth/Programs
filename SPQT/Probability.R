# Q1,3
mat1 <- matrix(
    c(1 / 16, 1 / 8, 1 / 16, 1 / 8, 1 / 4, 1 / 8, 1 / 16, 1 / 8, 1 / 16),
    nrow = 3, ncol = 3, byrow = TRUE
)
rownames(mat1) <- c("x=0", "x=1", "x=2")
colnames(mat1) <- c("y=0", "y=1", "y=2")
# compute marginal probability
px <- apply(mat1, 1, sum)
py <- apply(mat1, 2, sum)
# compute expectation and variance
x <- c(0, 1, 2)
exp_x <- sum(x * px)
exp_x2 <- sum((x^2) * px)
var_x <- exp_x2 - (exp_x^2)

y <- c(0, 1, 2)
exp_y <- sum(y * py)
exp_y2 <- sum((y^2) * py)
var_y <- exp_y2 - (exp_y^2)

# covariance
x2 <- matrix(x, nrow = 3, ncol = 1, byrow = FALSE)
y2 <- matrix(y, nrow = 1, ncol = 3, byrow = TRUE)

exp_xy <- sum(x2 %*% y2 * mat1)
cov_xy <- exp_xy - (exp_x * exp_y)

mp1 <- mat1[x = 2, y = 1] / py[1]
mp2 <- mat1[x <= 2, y = 1] / py[1]
mp3 <- mat1[x > 1, y > 0] / py[y > 0]

# -----------------------------------
# Q2,4
mat2 <- matrix(
    c(
        4 / 120, 1 / 60, 2 / 120, 2 / 60, 1 / 60, 3 / 60, 2 / 40, 1 / 40,
        1 / 120, 1 / 40, 1 / 60, 1 / 60, 2 / 60, 2 / 60, 1 / 60, 1 / 15,
        1 / 40, 1 / 60, 1 / 30, 2 / 120, 3 / 120, 1 / 120, 1 / 60, 1 / 30,
        3 / 120, 2 / 120, 1 / 60, 1 / 60, 2 / 40, 2 / 30, 1 / 60, 1 / 120,
        2 / 120, 1 / 60, 1 / 60, 1 / 40, 3 / 120, 1 / 60, 1 / 60, 2 / 120
    ),
    nrow = 5, ncol = 8, byrow = TRUE
)
rownames(mat2) <- c("x=1", "x=2", "x=3", "x=4", "x=5")
colnames(mat2) <- c("y=1", "y=2", "y=3", "y=4", "y=5", "y=6", "y=7", "y=8")

# marginal probability
px <- apply(mat2, 1, sum)
py <- apply(mat2, 2, sum)

# expectation and variance
x <- c(1, 2, 3, 4, 5)
exp_x <- sum(x * px)
exp_x2 <- sum((x^2) * px)
var_x <- exp_x2 - (exp_x^2)

y <- c(1, 2, 3, 4, 5, 6, 7, 8)
exp_y <- sum(y * py)
exp_y2 <- sum((y^2) * py)
var_y <- exp_y2 - (exp_y^2)

# covariance
x2 <- matrix(x, nrow = 5, ncol = 1, byrow = FALSE)
y2 <- matrix(y, nrow = 1, ncol = 8, byrow = TRUE)

exp_xy <- sum(x2 %*% y2 * mat2)
cov_xy <- exp_xy - (exp_x * exp_y)

mp1 <- mat2[x = 3, y = 2] / py[2]
mp2 <- mat2[x <= 3, y = 2] / py[2]
mp3 <- mat2[x <= 4, y >= 5] / py[y >= 5]
mp4 <- mat2[x = 5, y <= 7] / py[y <= 7]

# -----------------------------------
# Q5,7
mat3 <- matrix(
    c(
        3 / 72, 6 / 72, 9 / 72,
        5 / 72, 8 / 72, 11 / 72,
        7 / 72, 10 / 72, 13 / 72
    ),
    nrow = 3, ncol = 3, byrow = TRUE
)
rownames(mat3) <- c("x=1", "x=2", "x=3")
colnames(mat3) <- c("y=-2", "y=0", "y=1")
# compute marginal probability
px <- apply(mat3, 1, sum)
py <- apply(mat3, 2, sum)
# compute expectation and variance
x <- c(1, 2, 3)
exp_x <- sum(x * px)
exp_x2 <- sum((x^2) * px)
var_x <- exp_x2 - (exp_x^2)

y <- c(-2, 0, 1)
exp_y <- sum(y * py)
exp_y2 <- sum((y^2) * py)
var_y <- exp_y2 - (exp_y^2)

# covariance
x2 <- matrix(x, nrow = 3, ncol = 1, byrow = FALSE)
y2 <- matrix(y, nrow = 1, ncol = 3, byrow = TRUE)

exp_xy <- sum(x2 %*% y2 * mat3)
cov_xy <- exp_xy - (exp_x * exp_y)

mp1 <- mat3[x = 2, y = 2] / py[2]
mp2 <- mat3[x <= 2, y = 2] / py[2]
mp3 <- mat3[x <= 1.5, y > 1.5] / py[y > 1.5]

# -----------------------------------
# Q6,8
mat4 <- matrix(
    c(1 / 16, 1 / 8, 1 / 16, 1 / 8, 1 / 4, 1 / 8, 1 / 16, 1 / 8, 1 / 16),
    nrow = 3, ncol = 3, byrow = TRUE
)
rownames(mat4) <- c("x=1", "x=2", "x=3")
colnames(mat4) <- c("y=-4", "y=-1", "y=2")
# compute marginal probability
px <- apply(mat4, 1, sum)
py <- apply(mat4, 2, sum)
# compute expectation and variance
x <- c(1, 2, 3)
exp_x <- sum(x * px)
exp_x2 <- sum((x^2) * px)
var_x <- exp_x2 - (exp_x^2)

y <- c(-4, -1, 2)
exp_y <- sum(y * py)
exp_y2 <- sum((y^2) * py)
var_y <- exp_y2 - (exp_y^2)

# covariance
x2 <- matrix(x, nrow = 3, ncol = 1, byrow = FALSE)
y2 <- matrix(y, nrow = 1, ncol = 3, byrow = TRUE)

exp_xy <- sum(x2 %*% y2 * mat4)
cov_xy <- exp_xy - (exp_x * exp_y)

mp1 <- mat4[x = 2, y = -1] / py[-1]
mp2 <- mat4[x <= 2, y = 2] / py[2]
mp3 <- mat4[x <= 2.5, y > -1.5] / py[y > -1.5]
