# Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
# * Write a python program that displays the answers to the following questions:
# * How much does it cost to operate one server per day?
# * How much does it cost to operate one server per week?
# * How much does it cost to operate one server per month?
# * How much days can I operate one server with $918?

def daily_cost(rate):
    return rate * 24

def weekly_cost(rate):
    return rate * 24 * 7

def monthly_cost(rate):
    return rate * 24 * 30

def days_with_budget(budget, rate):
    return budget / daily_cost(rate)

rate = 0.51
budget = 918
print("Cost one server per day", daily_cost(rate))
print("Cost one server per week", weekly_cost(rate))
print("Cost one server per month", monthly_cost(rate))
print("Number of days with budget", days_with_budget(budget, rate))
