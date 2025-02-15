# app.py
import streamlit as st
from models import PitchDeckData
from main_generator import PitchDeckGenerator
import json


def create_streamlit_app():
    st.title("AI Startup Builder & Pitch Generator")
    st.write("Generate professional pitch decks with AI-powered content and visuals")
    
    # Initialize session state
    if 'output_path' not in st.session_state:
        st.session_state.output_path = None
    
    with st.form("pitch_deck_form"):
        company_name = st.text_input("Company Name")
        problem = st.text_area("Problem Statement")
        solution = st.text_area("Solution")
        market_size = st.number_input("Total Addressable Market Size (USD)", min_value=0.0)
        
        st.subheader("Revenue Model")
        revenue_streams = st.text_area(
            "Revenue Streams (Enter as JSON)",
            value='{"stream1": 1000000, "stream2": 500000}'
        )
        
        st.subheader("Roadmap")
        roadmap = st.text_area(
            "Roadmap Milestones (Enter as JSON)",
            value='[{"milestone": "MVP", "start_date": "2024-03", "end_date": "2024-06"}]'
        )
        
        st.subheader("Team")
        team = st.text_area(
            "Team Members (Enter as JSON)",
            value='[{"name": "John Doe", "role": "CEO"}]'
        )
        
        # try:
        #     team_data = json.loads(team)
        #     if not all('name' in m and 'role' in m for m in team_data):
        #         st.error("Team members must have 'name' and 'role' fields")
        #         return
        # except json.JSONDecodeError:
        #     st.error("Invalid team JSON format")
        #     return
                
        
        traction = st.text_area("Traction Metrics")
        future_outlook = st.text_area("Future Outlook")
        
        submitted = st.form_submit_button("Generate Pitch Deck")
        
        if submitted:
            try:
                
                st.write("Debugging Input Values:") # Add this section
                st.write("revenue_streams:", revenue_streams)
                st.write("roadmap:", roadmap)
                st.write("team:", team)
                st.write("traction:", traction) # Print traction value
                st.write("--- End of Debugging ---") 
                
                pitch_data = PitchDeckData(
                    company_name=company_name,
                    problem_statement=problem,
                    solution=solution,
                    market_size=market_size,
                    revenue_model=json.loads(revenue_streams),
                    roadmap=json.loads(roadmap),
                    team=json.loads(team),
                    traction=traction if traction else "",
                    future_outlook=future_outlook
                )
                
                generator = PitchDeckGenerator()
                output_path = generator.generate_pitch_deck(pitch_data)
                st.session_state.output_path = output_path
            except Exception as e:
                st.error(f"Error generating pitch deck: {str(e)}")
                
    if st.session_state.output_path:
        with open(st.session_state.output_path, "rb") as file:
            st.download_button(
                label="Download Pitch Deck",
                data=file,
                file_name=st.session_state.output_path,
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )

if __name__ == "__main__":
    create_streamlit_app()