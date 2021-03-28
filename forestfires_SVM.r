library(kernlab)
library(caret)
library(plyr)

# Read the data
FF <- read.csv(file.choose())
View(FF)
class(FF)

str(FF)

# The area value has lots of zeros

hist(FF$area)
rug(FF$area)

# Transform the Area value to Y 

FF1 <- mutate(FF, y = log(area + 1))  # default is to the base e, y is lower case
hist(FF1$y)

summary(FF) # Confirms on the different scale and demands normalizing the data.

# Prediction of Forest fires requires only prediction from 
# temperature, rain, relative humidity and wind speed

# Apply Normalization technique to the whole dataset :

normalise <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))  # subtract the min value in x and divide by the range of values in x.
}

FF$temp <- normalise(FF$temp)
FF$rain <- normalise(FF$rain)
FF$RH <- normalise(FF$RH)
FF$wind <- normalise(FF$wind)

# note, our earlier transformation was redundant, $area gives the same results
sum(FF$area < 5) 
sum(FF$area >= 5)

FF$size <- NULL
FF$size <- factor(ifelse(FF$area < 5, 1, 0),
                      labels = c("small", "large"))
train <- sample(x = nrow(FF), size = 400, replace = FALSE)

m.poly <- ksvm(size ~ temp + RH + wind + rain,
               data = FF[train, ],
               kernel = "polydot", C = 1)
m.poly

m.rad <- ksvm(size ~ temp + RH + wind + rain,
              data = FF[train, ],
              kernel = "rbfdot", C = 1)
m.rad

m.tan <- ksvm(size ~ temp + RH + wind + rain,
              data = FF[train, ],
              kernel = "tanhdot", C = 1)
m.tan

pred <- predict(m.rad, newdata = FF[-train, ], type = "response")

table(pred, FF[-train, "size"])
confusionMatrix(table(pred, FF[-train, "size"]), positive = "small") 

sessionInfo()
