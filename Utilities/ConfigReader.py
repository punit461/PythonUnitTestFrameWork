import configparser

# Initialize the configparser
config = configparser.ConfigParser()
config.read("..\Configurations\config.ini")

# Read data from the 'URLs' section
baseEnv = config.get('URLs', 'baseEnv')
if baseEnv == "testEnv":
    base_url = config.get('URLs', 'testEnv')
elif baseEnv == "devEnv":
    base_url = config.get('URLs', 'devEnv')
elif baseEnv == "stageEnv":
    base_url = config.get('URLs', 'stageEnv')
else:
    base_url = config.get('URLs', 'prodEnv')

# Read data from the 'Credentials' section
username = config.get('Credentials', 'username_admin')
password = config.get('Credentials', 'password_admin')

# Read the Settings value
timeout = config.get('Settings', 'default_timeout')
browser = config.get('Settings', 'default_browser')

# Print the read values to validate
# print("Username:", username)
# print("Password:", password)
# print("Login URL:", base_url)
