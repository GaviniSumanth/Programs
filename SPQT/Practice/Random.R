# Syntax: runif(n, min, max) # nolint
# Parameters:
# n: Number of observations
# min, max: represents lower and upper limits of the uniform distribution
x <- runif(10, min = -1, max = 1)
print(x)

# sample(data, size, replace = FALSE, prob = NULL) # nolint
#
# where,
# data -> Vector or Dataframe
# size -> Size of sample
# replace -> (Optional) To set the values again repeated if it is set to true
# prob -> (Optional) A vector of probability weights for obtaining the elements of the vector being sampled # nolint
data <- c(1:10)
sample(data, 3)
sample(data, 3, replace = TRUE)
sample(data, 3, prob = c(1:10))

# To genearate array of size 10
# from values 1 to 100
# with replacement
sample(100, 10, replace = TRUE)
