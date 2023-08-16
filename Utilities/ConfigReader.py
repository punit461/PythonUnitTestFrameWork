import configparser

# Initialize the configparser
config = configparser.ConfigParser()
config.read("..\Configurations\config.ini")

# Read data from the 'URLs' section
baseEnv = config.get('URLs', 'baseEnv')
if baseEnv == "testEnv":
    base_url = config.get('URLs', 'testEnv')
elif baseEnv == "testEnv":

# Read data from the 'Credentials' section
username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')

# Print the read values
print("Username:", username)
print("Password:", password)
print("Login URL:", login_url)
