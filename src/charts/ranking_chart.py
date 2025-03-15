import pandas as pd
import matplotlib.pyplot as plt
from flask_caching import Cache
from wordcloud import WordCloud
from dash import dcc
import plotly.graph_objects as go

cache = Cache()

#@cache.memoize()
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
        
    top_categories = df.groupby("App")["Installs"].sum().reset_index()

    top_categories = top_categories.sort_values(by="Installs", ascending=False).head(10)
    
    # Create a dictionary for the word cloud where keys are categories and values are install counts
    wordcloud_data = dict(zip(top_categories["App"], top_categories["Installs"]))
    
    wordcloud = WordCloud(width=800, height=400, background_color="white")
    wordcloud.generate_from_frequencies(wordcloud_data)
    
    # generate image
    wordcloud_img = wordcloud.to_image()

    fig = go.Figure()
    fig.add_trace(go.Image(z=wordcloud))
    fig.update_layout(
        height=400,
        xaxis={"visible": False},
        yaxis={"visible": False},
        margin={"t": 0, "b": 0, "l": 0, "r": 0},
        hovermode=False,
        paper_bgcolor="#F9F9FA",
        plot_bgcolor="#F9F9FA",
    )
    
    return fig
    