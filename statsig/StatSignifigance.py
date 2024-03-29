import math

"""Hypothesis Test - If the
sample proportion of
observing a sammple statistic as
extreme than the one observed
under the assumption that the
statement in the null
hypothesis is true.

null hypothesis - denoted H0
is read as H-naught, is a 
statement to be tested. The 
null hypothesis is a 
statement of no change, no 
effect, or no difference and 
is assumed true until 
evidence indicates otherwise.

alternative hypothesis - 
denoted H1 read as H-one is a 
statement that we are trying 
to findo evidence to support.

Two tail test
H0 = some value
H1 != some value
 
Left tail test
H0 = some value
H1 < some value

Right tail test
H0 = some value
H1 > some value

Four Outcomes from Hypothesis
Testing
1. Reject the null hypothesis
when the alternative 
hypothesis is true. This 
decision would be correct.

2. Do no reject the null when the
null is true. This decission 
would be correct.

3. Reject the null when the null
is true. This would be 
incorrect. This is a TYPE 1 
ERROR.

4. Do not reject the null 
when the alternative is true.
This decision would be 
incorrect.  TYPE 2 ERROR


The probablity of making a 
TYPE 1 or TYPE 2 error

apha = P(TYPE 1 ERROR)
P(REJECTING H0 WHEN H0 IS TRUE)

beta = P(TYPE 2 ERROR)
P(NOT REJECTING H0 WHEN H1 IS TRUE)

Level of Significance - 
alpha, is the probability of 
making a TYPE 1 ERROR.

Statistically Significant - 
When observed results are 
unlikely under the assumption that
the null hypothesis is true, we
say the result is statistically
significant and reject the 
null. 
 """


def pop_proportion(p_hat, p, n):
    # x is the standard deviation of the formula
        x = math.sqrt(p*(1-p)/n)
        z_naught = (p_hat - p) / x
        print("The z value is: ", z_naught)


def t_distribution(p_hat, p, sd, n):
        t = (p_hat-p)/(sd/math.sqrt(n))
        print("The t value is, ", t)



if __name__ == "__main__":
    print("p_hat is the number your testing,\
        p is the number your testing against, \
        n is the number in your sample")

    choice = input("Press 1 for z_score, 2 for t_distribution: ")
    if choice =="1":
        p_hat = float(input("Enter P_hat: "))
        p = float(input("Enter p: "))
        n = float(input("Enter number: "))
        print(p_hat, p, n)
        pop_proportion(p_hat, p, n)

    elif choice == "2":
        p_hat = float(input("Enter P_hat: "))
        p = float(input("Enter p: "))
        sd = float(input("Enter the standard deviation: "))
        n = float(input("Enter number: "))
        print(p_hat, p, sd, n)
        t_distribution(p_hat, p, sd, n)
