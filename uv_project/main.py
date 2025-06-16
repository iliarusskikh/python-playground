from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")#u need to specify which one to use

api_key = os.getenv("API_KEY")
print(f"Your API KEY {api_key}")

def main():
    print("Hello from uv-project!")


if __name__ == "__main__":
    main()



#UV vs PIP
#uv init .

#uv add numpy
#uv run .\main.py
