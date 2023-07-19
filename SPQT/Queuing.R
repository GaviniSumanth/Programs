mm1_model <- function(lambda, mu, n) {
    rho <- lambda / mu
    po <- 1 - rho
    pn <- (rho^n) * (1 - rho)
    pn_1 <- rho^n
    ls <- rho / (1 - rho)
    lq <- rho / ls
    ws <- ls / lambda
    wq <- lq / lambda
    x <- data.frame(rho, po, pn, pn_1, ls, lq, ws, wq)
    print(x)
}

mm1_model(6, 18, 4)
mm1_model(8, 16, 24)
