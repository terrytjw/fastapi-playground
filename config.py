import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the API keys from the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Other configurations
# ...