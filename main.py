import PyAuthGG, time

App = PyAuthGG.Application("API KEY", "AID", "project_secret")

print("\t\tREGISTER")

License = str(input("LICENSE: "))
Username = str(input("USERNAME: "))
Email = str(input("EMAIL: "))
Password = str(input("PASSWORD: "))

register = App.Register(License, Username, Email, Password)

if register["result"] == "success":
    print("\n[X]\tUSER REGISTRED")
    App.Log(Username, "Registred")
else:
    print("\n[X]\tUSERDATA INVALID")

print("\n[X]\tEXITING...")
time.sleep(5)
exit()
