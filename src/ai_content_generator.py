from typing import Dict, Any
import os
import json
from dotenv import load_dotenv
from models import PitchDeckData
from config import Config
from camel.agents import ChatAgent

load_dotenv()

class AIContentGenerator:
        
    def generate_elevator_pitch(self, pitch_data: PitchDeckData) -> str:
        
        # if self.gemini is None: # Check if Gemini model is initialized
        #     return "Error: Gemini model not initialized."
        
        prompt = f"""Create a compelling elevator pitch for {pitch_data.company_name}.
        Problem: {pitch_data.problem_statement}
        Solution: {pitch_data.solution}
        Market Size: ${pitch_data.market_size:,.2f}
        """
        try:
            response = ChatAgent(system_message=prompt, model=Config().model).step(prompt)
            return response.msg.content
        except Exception as e:
            print(f"Error generating elevator pitch from Gemini: {e}")
            return "Error generating elevator pitch. Please check the logs."
    
    def generate_executive_summary(self, pitch_data: PitchDeckData) -> str:
        # if self.gemini is None: # Check if Gemini model is initialized
        #     return "Error: Gemini model not initialized."
        
        team_description = "Experienced team"  # Default
        
        if pitch_data.team:
            try:
                roles = [member.get('role', 'undefined role') 
                        for member in pitch_data.team]
                team_description = f"{len(pitch_data.team)} members with {roles[0]} leadership"
            except (KeyError, IndexError):
                team_description = "Core team in place"
        
        prompt = f"""Create a concise executive summary for {pitch_data.company_name} covering:
        - Problem: {pitch_data.problem_statement}
        - Solution: {pitch_data.solution} 
        - Market Size: ${pitch_data.market_size:,.2f}
        - Revenue Model: {json.dumps(pitch_data.revenue_model)}
        - Key Traction: {pitch_data.traction}
        - Roadmap Highlights: {pitch_data.roadmap[:2]}
        - Team Strength: {team_description}
        """

        try:
            response = ChatAgent(system_message=prompt, model=Config().model).step(prompt)
            return response.msg.content
        except Exception as e:
            return f"Error generating executive summary. Please check the logs.{e}"