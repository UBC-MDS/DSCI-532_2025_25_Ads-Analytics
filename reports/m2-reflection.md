# Reflection on Current Implementation
In this milestone, we've made substantial progress in developing the dashboard, focusing on interactivity and data visualization. Below is a summary of our achievements, pending tasks, and reflections on the dashboard’s current state.

## What Has Been Implemented:
### Category Filter: 
We introduced a filter allowing users to select specific app categories or view all categories. This enhances interactivity, enabling users to focus on the most relevant categories.

### Updated Filters: 
The global filters now default to 'All', making it easier for users to explore the entire dataset. The filters allow selection of:
    App Type (Free or Paid)
    Content Rating (e.g., Everyone, Teen)
    Category (specific or all)

### Revised Layout: 
The dashboard layout has been updated to align with the initial proposal from Milestone 1, providing a more intuitive user experience.

### Visualizations:
Top 10 Categories by Install Plot: Displays the most popular app categories based on install counts.
Reviews vs. Installs for Top Apps: A scatter plot illustrating the relationship between app reviews and install counts.
Average Ratings by Category Plot: A bar chart comparing average ratings across categories.
Average Number of Reviews Plot: A bar chart comparing average reviews across categories.

### Interactive Filters: 
The four visualizations update dynamically as users apply filters, offering real-time insights based on selected app type, category, and content rating. Visual elements like color coding and bubble sizes enhance data interpretation.
Deployment: The dashboard is deployed successfully on Render, enabling real-time interactivity for users.

## What Is Not Yet Implemented:
### Comprehensive Data Analysis: 
While the visualizations allow for deeper analysis of app feature relationships between reviews, ratings, and installs has not been fully explored.

### Advanced Visualizations: 
Future versions may include advanced visualizations in different plots and demonstrate trends across different categories.

## Challenges and Limitations:
### Memory Issues: 
We encountered "Worker Timeout. Perhaps out of memory" errors during deployment, primarily due to the large dataset. To resolve this, we reduced the dataset size, but we plan to optimize data handling in future milestones for better performance.

### Dashboard Layout and User Interaction: 
Add more functionalities could improve user experience but slow down the render time.

## Deviations from Initial Proposal:
### Data Size Reduction: 
Initially, the dashboard used a large dataset, which caused performance issues. We reduced the dataset to maintain smooth functionality, but intend to enhance data processing strategies moving forward.
### Visualization Adjustments: 
While we originally planned for a combination of bar charts and line graphs, we opted for scatter plots and histograms based on user feedback and better alignment with the project goals.

## Future Improvements:
### Performance Enhancements: 
Implementing data optimization techniques to reduce memory usage and improve loading times.
### Deeper Analytics: 
Adding more complex analysis features, like correlation studies between app ratings, installs, and reviews.
### Additional Filters: 
Expanding filtering options to further refine user queries.

## Conclusion:
The dashboard currently serves as a powerful tool for advertisement companies to assess app performance and make data-driven decisions for ad placements. While the core features are functioning well, we will continue to optimize performance and enhance visualizations in the next milestone.


