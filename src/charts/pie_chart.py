import altair as alt
import pandas as pd

def create_pie(df, categories):
    """
    Generate an interactive Altair pie chart for the Top 10 App Categories by popularity score.

    Parameters:
        df (pd.DataFrame): The DataFrame containing app data.
        categories (list): A list of selected categories for filtering the data. 
                       If 'All' is included, the data will not be filtered by category.

    Returns:
        object of the Altair chart
    """
    category_to_color = {
    'GAME': "#1f77b4",
    'ENTERTAINMENT': "#ff7f0e",
    'PHOTOGRAPHY': "#2ca02c",
    'VIDEO_PLAYERS': "#d62728",
    'SHOPPING': "#9467bd",
    'SOCIAL': "#8c564b",
    'COMMUNICATION': "#e377c2",
    'HOUSE_AND_HOME': "#7f7f7f",
    'WEATHER': "#bcbd22",
    'EDUCATION': "#17becf"
    }
    
    category_counts = df.groupby('Category').size().reset_index(name='Count')
    total_apps = category_counts['Count'].sum()
    category_counts['Percentage'] = (category_counts['Count'] / total_apps) * 100

    pie_chart = alt.Chart(category_counts).mark_arc().encode(
        theta=alt.Theta(field="Count", type="quantitative"),  
        color=alt.Color("Category:N", scale=alt.Scale(domain=list(category_to_color.keys()), range=list(category_to_color.values())), legend=None),
        tooltip=[alt.Tooltip(field="Category", type="nominal"), 
                 alt.Tooltip(field="Count", type="quantitative"), 
                 alt.Tooltip(field="Percentage", type="quantitative", title="Percentage", format=".1f")]
    ).properties(
        title="App Count per Category",
        height=350,
        width=300
    )

    pie_chart_with_labels = pie_chart.mark_arc().encode(
        text=alt.Text(field="Percentage", type="quantitative", format=".1f"),  
        size=alt.value(100),  
    ).properties(
        title="App Count per Category with Percentage"
    )
    pie_chart = pie_chart+pie_chart_with_labels
    
    final_chart = pie_chart.encode(
    text=alt.Text(field="Percentage", type="quantitative", format=".1f")  # Add '%' symbol to the labels
)
    return final_chart