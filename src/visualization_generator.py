import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, List, Any

class VisualizationGenerator:
    def create_market_size_chart(self, market_data):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=list(market_data.keys()),
            y=list(market_data.values()),
            text=[f'${x/1e6:.1f}M' for x in market_data.values()],
            marker_color=['#2962FF', '#546E7A', '#00C853']  # Blue, Gray, Green
        ))
        fig.update_layout(
            template='plotly_white',
            title_font_size=20,
            hoverlabel=dict(bgcolor="white")
        )
        return fig
    
    def create_revenue_projection(self, revenue_data: Dict[str, float]) -> go.Figure:
        df = pd.DataFrame(list(revenue_data.items()), columns=['Stream', 'Revenue'])
        fig = px.pie(df, values='Revenue', names='Stream',
                     title='Revenue Distribution',
                     color_discrete_sequence=['#2962FF', '#00C853'])
        return fig
    
    def create_roadmap_timeline(self, milestones: List[Dict[str, Any]]) -> go.Figure:
        df = pd.DataFrame(milestones)
        fig = px.timeline(df, x_start='start_date', x_end='end_date',
                         y='milestone', title='Product Roadmap',
                         color_discrete_sequence=['#2962FF'])
        return fig
    
    def create_solution_diagram(self):
        fig = go.Figure(go.Indicator(
            mode="number+gauge",
            value=50,
            domain={'x': [0.1, 1], 'y': [0.1, 1]},
            title={'text': "Cost Savings %"},
            gauge={'shape': "bullet"}
        ))
        return fig

    def create_financial_forecast(self):
        years = [2024, 2025, 2026]
        revenue = [1.2, 3.5, 8.0]  # In millions
        fig = px.line(x=years, y=revenue, title="Revenue Projection (Millions USD)")
        fig.update_traces(line_color='#2962FF')
        return fig