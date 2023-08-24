library(moments)
iris <- read.csv("Practice/data/Iris.csv")
pl <- iris$PetalLengthCm
# Non-Central Moments
pl_fncm <- moment(pl, order = 1, central = FALSE)
pl_sncm <- moment(pl, order = 2, central = FALSE)
pl_tncm <- moment(pl, order = 3, central = FALSE)
pl_foncm <- moment(pl, order = 4, central = FALSE)
# Central Moments
pl_fcm <- moment(pl, order = 1, central = TRUE)
pl_scm <- moment(pl, order = 2, central = TRUE)
pl_tcm <- moment(pl, order = 3, central = TRUE)
pl_focm <- moment(pl, order = 4, central = TRUE)

# Skewness, Kurtosis
pl_beta1 <- pl_tcm^2 / pl_scm^3
pl_gamma1 <- sqrt(pl_beta1)
pl_beta2 <- pl_focm / pl_scm^2
pl_gamma2 <- pl_beta2 - 3
