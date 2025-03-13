

user_credentials = {}


while True:
  def register_user():
    
      username = input("Enter username ")
    
      if username in user_credentials:
        print("Username already exists. Please choose a different username.")
      else:
        password = input("Enter password: ")
        user_credentials[username] = password
        print("Registration successful!")

  def login_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in user_credentials and user_credentials[username] == password:
      print("Welcome back!")
    else:
      print("Invalid username or password.")  
    
  def authentication_system():
    while True:
      print("Basic Authentication System")
      print("1. Register")
      print("2. Login")
      print("3. Exit")

      option = input("Enter your choice (1-3): ")
      if option == "1":
        register_user()  
      elif option == "2":
        login_user()
      elif option == "3":
        print("Exiting the system.")
        break
      else:
        print("Invalid option. Please try options 1-3.")
        break
    
  authentication_system()
  