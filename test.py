from dotenv import load_dotenv
import os

load_dotenv()

print(f">> {os.getenv("OPENAI_API_KEY")}")
