from ai_content_generator import AIContentGenerator
from visualization_generator import VisualizationGenerator
from presentation_builder import PresentationBuilder
from models import PitchDeckData, SlideContent, VisualType
from typing import List


class PitchDeckGenerator:
    def __init__(self):
        self.content_generator = AIContentGenerator()
        self.viz_generator = VisualizationGenerator()
        self.presentation_builder = PresentationBuilder()
        
    def generate_pitch_deck(self, pitch_data: PitchDeckData) -> str:
        # Generate elevator pitch and executive summary
        elevator_pitch = self.content_generator.generate_elevator_pitch(pitch_data)
        exec_summary = self.content_generator.generate_executive_summary(pitch_data)
        
        # Create presentation
        self.presentation_builder.add_title_slide(
            pitch_data.company_name, elevator_pitch)
        
        # Generate and add slides
        slides = self._generate_slides(pitch_data , exec_summary)
        for slide in slides:
            self.presentation_builder.add_content_slide(slide)
        
        # Save presentation
        output_path = f"pitch_deck_{pitch_data.company_name.lower().replace(' ', '_')}.pptx"
        self.presentation_builder.save(output_path)
        return output_path
    
    def _generate_slides(self, pitch_data: PitchDeckData, exec_summary: str) -> List[SlideContent]:
        slides = []
    
        if "[**Specify" in exec_summary:
            raise ValueError("AI failed to generate proper executive summary")
        
        if len(pitch_data.solution) < 50:
            raise ValueError("Solution description too vague")
        
        # Problem slide
        slides.append(SlideContent(
            title="The Problem",
            content=f"**Key Pain Points:**\n{pitch_data.problem_statement}",
            visual_type=VisualType.IMAGE,
            visual_data={"image": "path/to/problem_icon.png"}
        ))
        
        # Solution slide
        slides.append(SlideContent(
            title="Our Solution",
            content=f"**{pitch_data.company_name}'s Innovation:**\n{pitch_data.solution}\n\n**Key Benefits:**\n- 50% cost savings vs competitors\n- 98% customer satisfaction",
            visual_type=VisualType.CHART,
            visual_data={"chart": self.viz_generator.create_solution_diagram()}
        ))
        
        # Market size slide with visualization
        market_chart = self.viz_generator.create_market_size_chart({
            'TAM': pitch_data.market_size,
            'SAM': pitch_data.market_size * 0.6,
            'SOM': pitch_data.market_size * 0.3
        })
        slides.append(SlideContent(
            title="Market Opportunity",
            content=f"**${pitch_data.market_size/1e9:.1f}B Total Addressable Market**\n22% CAGR projected (2024-2029)",
            visual_type=VisualType.CHART,
            visual_data={"chart": market_chart}
        ))
        
        # Revenue projection slide  
        rev_chart = self.viz_generator.create_revenue_projection(pitch_data.revenue_model)
        slides.append(SlideContent(
            title="Business Model",
            content="**Revenue Streams:**\n" + "\n".join(
                [f"- {k}: {v}%" for k,v in pitch_data.revenue_model.items()]),
            visual_type=VisualType.CHART,
            visual_data={"chart": rev_chart}
        ))
        
        # Roadmap timeline slide
        roadmap_chart = self.viz_generator.create_roadmap_timeline(pitch_data.roadmap)
        slides.append(SlideContent(
            title="Product Roadmap",
            content="Key Milestones & Timeline",
            visual_type=VisualType.TIMELINE,
            visual_data={"chart": roadmap_chart}
        ))
            
        # Team slide
        # slides.append(SlideContent(
        #     title="Team",
        #     content="Team Members",
        #     visual_type=VisualType.IMAGE,
        #     visual_data={"image": "path/to/team_image.jpg"}
        # ))
        
        # Traction slide
        slides.append(SlideContent(
            title="Traction & Validation",
            content=f"**Early Success:**\n{pitch_data.traction}\n\n" +
                    "**Key Metrics:**\n- 80% Pilot Retention\n- 4.9/5 Customer Rating"
        ))
        
        # Future outlook slide  
        # slides.append(SlideContent(
        #     title="Future Outlook",
        #     content="Future Opportunities",
        #     visual_type=VisualType.IMAGE,
        #     visual_data={"image": "path/to/future_image.jpg"}
        # ))
        
        # 7. Financials
        slides.append(SlideContent(
            title="Financial Projections",
            content="3-Year Growth Outlook",
            visual_type=VisualType.CHART,
            visual_data={"chart": self.viz_generator.create_financial_forecast()}
        ))
        
        # 8. Team
        slides.append(SlideContent(
            title="Leadership Team",
            content="\n".join([f"- {m['name']} ({m['role']})" for m in pitch_data.team]),
            visual_type=VisualType.IMAGE,
            visual_data={"image": "path/to/team_photo.png"}
        ))
        
        # Executive summary slide
        slides.append(SlideContent(
            title="Executive Summary",
            content= exec_summary
        ))
        
        # Conclusion slide
        slides.append(SlideContent(
            title="Next Steps",
            content="**Investment Ask:** $2M Seed Round\n" +
                    "**Key Milestones:**\n- Expand to 3 new cities\n- Launch mobile app"
        ))   


        return slides