import os

secret_name = "SNOWFLAKE_ACCOUNT" 

secret_value = os.getenv(secret_name)

if secret_value: 
    print(f"The value of '{secret_name}' is: {secret_value}") 
else: 
    print(f"Secret '{secret_name}' is not set or is empty.")  
