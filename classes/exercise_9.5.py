class User:
    login_attempts = 0
    def __init__(self):
        pass # pass means do nothing, it is just place holder
        # self.login_attempts = 0 this is alternate way of creating global variable

    def increment_login_attempts(self):
        print("incrementing the value by 1 ...")
        self.login_attempts += 1
    def reset_login_attempts (self):
        print("resetting the value by 0...")
        self.login_attempts = 0

user1 = User()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts: ", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts: ", user1.login_attempts)