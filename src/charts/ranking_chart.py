import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dash import dcc
import plotly.graph_objects as go

def create_wordcloud(df, categories):
    """
    Generate a word cloud for the Top 10 App Categories by Installs.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.
        selected_type (str): "Free" or "Paid".
        min_rating (float): Minimum rating to filter apps.
    """
    if "All" not in categories:
        df = df[df["Category"].isin(categories)]
        
    top_categories = df.groupby("Category")["Installs"].sum().reset_index()

    top_categories = top_categories.sort_values(by="Installs", ascending=False).head(10)
    
    # Create a dictionary for the word cloud where keys are categories and values are install counts
    wordcloud_data = dict(zip(top_categories["Category"], top_categories["Installs"]))
    
    wordcloud = WordCloud(width=800, height=400, background_color="white")
    wordcloud.generate_from_frequencies(wordcloud_data)
    
    # generate image
    wordcloud_img = wordcloud.to_image()

    fig = go.Figure()
    fig.add_layout_image(
        dict(
            source=wordcloud_img,
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            sizex=1, sizey=1,
            opacity=1, layer="below"
        )
    )
    
    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        showlegend=False
    )
    
    return fig
    