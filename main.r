
# 1. Goodness-of-Fit Test
cat("===== 1. GOODNESS-OF-FIT TEST =====\n")

# Coin toss results
observed_coin <- c(37, 23)
expected_coin <- c(30, 30)

test_coin <- chisq.test(x = observed_coin, p = expected_coin/sum(expected_coin))

print(test_coin)

if(test_coin$p.value < 0.05){
  cat("Decision: Reject H0\n")
  cat("Conclusion: The coin is not fair.\n")
} else {
  cat("Decision: Fail to Reject H0\n")
  cat("Conclusion: The coin may be fair.\n")
}

cat("\n")

# Additional experiment
observed <- c(24, 108, 95, 23)
expected <- c(30, 90, 90, 30)

test_exp <- chisq.test(x = observed, p = expected/sum(expected))

cat("Additional Experiment\n")
print(test_exp)

if(test_exp$p.value < 0.05){
  cat("Decision: Reject H0\n")
  cat("Conclusion: Observed and expected frequencies are significantly different.\n")
} else {
  cat("Decision: Fail to Reject H0\n")
  cat("Conclusion: No significant difference between observed and expected frequencies.\n")
}

# 2. Test of Independence

cat("\n===== 2. TEST OF INDEPENDENCE =====\n")

vaccination <- matrix(c(9,42,
                        17,28),
                      nrow=2,
                      byrow=TRUE)

rownames(vaccination) <- c("Vaccinated", "Not Vaccinated")
colnames(vaccination) <- c("Got Disease", "Did Not Get Disease")

print(vaccination)

test_vaccine <- chisq.test(vaccination)

print(test_vaccine)

if(test_vaccine$p.value < 0.05){
  cat("Decision: Reject H0\n")
  cat("Conclusion: Vaccination and disease occurrence are related.\n")
} else {
  cat("Decision: Fail to Reject H0\n")
  cat("Conclusion: Vaccination and disease occurrence are independent.\n")
}



# 3. Chi-Square Test in Real-World Context

cat("\n===== 3. SLEEPING PILLS TEST =====\n")

sleep_test <- matrix(c(44,10,
                       81,35),
                     nrow=2,
                     byrow=TRUE)

rownames(sleep_test) <- c("Sleeping Pills", "Sugar Pills")
colnames(sleep_test) <- c("Slept Well", "Did Not Sleep Well")

print(sleep_test)

test_sleep <- chisq.test(sleep_test)

print(test_sleep)

if(test_sleep$p.value < 0.05){
  cat("Decision: Reject H0\n")
  cat("Conclusion: Sleeping pills are effective.\n")
} else {
  cat("Decision: Fail to Reject H0\n")
  cat("Conclusion: No significant evidence that sleeping pills are effective.\n")
}

# 4. Measure of Association
cat("\n===== 4. MEASURE OF ASSOCIATION =====\n")

association <- matrix(c(49,25,
                        30,96),
                      nrow=2,
                      byrow=TRUE)

rownames(association) <- c("Blue Eyes", "Not Blue")
colnames(association) <- c("Blonde", "Not Blonde")

print(association)

test_assoc <- chisq.test(association)

print(test_assoc)

# Coefficient of Contingency
chi2 <- test_assoc$statistic
n <- sum(association)

C <- sqrt(chi2 / (chi2 + n))

cat("\nCoefficient of Contingency =", round(C,2), "\n")

# Interpretation
if(C < 0.30){
  cat("Interpretation: Weak association\n")
} else if(C < 0.60){
  cat("Interpretation: Moderate association\n")
} else {
  cat("Interpretation: Strong association\n")
}