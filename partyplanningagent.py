
from smolagents import InferenceClientModel, CodeAgent, DuckDuckGoSearchTool, tool, Tool, VisitWebpageTool, FinalAnswerTool
import numpy as np
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# premiliminary check to see if the account is connected
# agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=InferenceClientModel())
# agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")

# A tool for the agent to use

# import hugging face token
hf_token = os.getenv("HF_TOKEN")


@tool
def suggest_menu(occasion : str) -> str:
    """
    Suggest a menu based on occasion
    Args:
        occasion: The type of occaasion for the party. Allowed values are:
            - "casual": Menu for casual party.
            - "formal": Menu for formal party.
            - "superhero": Menu for superhero party.
            - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, cool-drinks."
    elif occasion == "formal":
        return "Three course meal with wine and dessert"
    elif occasion == "superhero":
        return "Buffet with high energy and healthy food"
    else:
        return "Custom menu from butler"

   
@tool
def catering_service(query:str)->str:
    """
    A tool for finding the best catering service in Gotham city

    Args:
        query: A search term for finding catering services 
    """
    services = {
        "Gotham Catering.Co" : 4.7,
        "God's Catering" : 4.5,
    }

    best_service = max(services ,key=services.get)

    return best_service

class SuperHeroParty(Tool):
    name = "super_hero_party_theme_generator"
    description = """
    This tool suggests creative superhero-themed party ideas based on a category.
    It returns a unique party theme idea."""
    inputs = {
        "category": {
            "type": "string",
            "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
    }
    }
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
            "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
            "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets."
        }
        
        return themes.get(category.lower(), "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")
    
agent = CodeAgent(
    tools=[
        DuckDuckGoSearchTool(),
        VisitWebpageTool(),
        catering_service,
        suggest_menu,
        SuperHeroParty(),
        FinalAnswerTool()
    ],
    model=InferenceClientModel(
        token=hf_token
    ),
    max_steps=10,
    verbosity_level=2
)

