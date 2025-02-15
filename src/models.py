# models.py
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum

class VisualType(Enum):
    CHART = "chart"
    IMAGE = "image"
    TIMELINE = "timeline"
    GRAPH = "graph"

@dataclass
class SlideContent:
    title: str
    content: str
    visual_type: Optional[VisualType] = None
    visual_data: Optional[Dict[str, Any]] = None
    
@dataclass
class PitchDeckData:
    company_name: str
    problem_statement: str
    solution: str
    market_size: float
    revenue_model: Dict[str, float]
    roadmap: List[Dict[str, Any]]
    team: List[Dict[str, str]]
    traction: str
    future_outlook: str