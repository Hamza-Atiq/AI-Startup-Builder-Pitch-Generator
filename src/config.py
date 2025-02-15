from camel.models import ModelFactory
from camel.types import ModelPlatformType , ModelType
from camel.configs import GeminiConfig
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class Config:
    
    def __init__(self):
        self.model = ModelFactory.create(
            model_platform=ModelPlatformType.GEMINI,
            model_type= ModelType.GEMINI_2_0_FLASH,
            model_config_dict = GeminiConfig().as_dict()
        )

        
        
        
        
    


