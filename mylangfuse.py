import os
from langfuse import get_client
from dotenv import load_dotenv
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
import smolagents

load_dotenv()

pub = os.getenv("LANGFUSE_PUBLIC_KEY")
pri = os.getenv("LANGFUSE_SECRET_KEY")
host = os.getenv("LANGFUSE_HOST")

langfuse = get_client()

# verify connection
if langfuse.auth_check():
    print("Client Authenticated")
else:
    print("Authentication Failed")


instrument = SmolagentsInstrumentor()
instrument.instrument()