"""
Configuration Manager
• Objective: Use classes, inheritance, dictionaries, and file I/O to manage application
configuration.
• Task: Create a configurable system that loads database settings from a file
"""
import configparser
class Config:
    pass
class DatabaseConfig(Config):
    def load_config(self):
        config = configparser.ConfigParser()
        config.read("db.ini")
        required_keys = [
            "host",
            "user",
            "password",
            "database"
        ]
        for key in required_keys:
            if key not in Config["DATABASE"]:
                print(f"Missing key: {key}")
                return
        
        print("Database Configuration")
        print("Host:",config["DATABASE"]["host"])
        print("User:",config["DATABASE"]["user"])
        print("Password:",config["DATABASE"]["password"])
        print("Database:",config["DATABASE"]["database"])
db = DatabaseConfig()
db.load_config()


