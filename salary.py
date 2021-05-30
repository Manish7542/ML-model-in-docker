import joblib
model=joblib.load('salary.pk1')
def salary(exp):
    x=exp
    salary=model.predict([[x]])
    salaryfinal=round(salary[0],3)
    print("Your salary might be {} rupees".format(salaryfinal))
print("#######Welecome To my program #######\n")
exp=float(input("Please enter your year of Exp ?? "))
salary(exp)