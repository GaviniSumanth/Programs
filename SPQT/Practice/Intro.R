# Aritmetic Operations
a <- 5
print(a)

a1 <- 5
a2 <- 3
a1 + a2
a1 - a2
a1 / a2
a1 * a2
a1**a2
a1 %% a2

# Vector Operations
x1 <- c(1:10)
x2 <- c(11:20)
x1 + x2
x1 - x2
x1 * x2
(x1 / 3) * (x2 / 4)
x1^10

# Matrix Operations
m1 <- matrix(c(1:25), nrow = 5, ncol = 5)
m2 <- matrix(c(1:25), nrow = 5, ncol = 5, byrow = TRUE)
rownames(m2) <- c("R1", "R2", "R3", "R4", "R5")
colnames(m2) <- c("C1", "C2", "C3", "C4", "C5")
row_sum <- rowSums(m2)
col_sum <- colSums(m2)
gt_col <- sum(col_sum)
