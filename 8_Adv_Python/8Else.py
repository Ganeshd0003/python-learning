# a = 300/0 This line itself error due to 0

try:
    a = 300/0 # if we do 300/10 so else block printed
except Exception as e:
    print(e)

else:
    print("It works when the No error occured")