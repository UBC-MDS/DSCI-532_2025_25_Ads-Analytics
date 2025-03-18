# Milestone 4 Reflection

In this milestone (Milestone 4), our team made significant improvements to the performance, usability, and organization of the dashboard. We focused on implementing feedback from both our professor Joel and peers to enhance the user experience and ensure smoother functionality. Key improvements included splitting the code into more organized sections, transitioning to a binary data format, and optimizing the dashboard’s performance.

**Feedback and Insights**  
One particularly useful piece of feedback was about the dashboard’s response time during user interactions, especially with large datasets. Initially, the dashboard lagged when filtering by categories. To address this, we implemented data sampling, significantly speeding up performance without sacrificing too much detail. This feedback helped us prioritize user interaction speed and made us more conscious of balancing performance and data accuracy. Another key improvement was ensuring the dashboard updates smoothly when selecting multiple categories in the global filter, addressing earlier interaction issues.

**Changes and Additions**  
A major enhancement was adding a pie chart to show the distribution of categories by popularity score. This addition made it easier for users to visualize how apps are spread across categories. We also made the bubble chart zoomable, allowing for better exploration of the data. Additionally, we aligned the charts more effectively to create a cleaner and more organized layout, making the dashboard more user-friendly.

**Challenges**  
We encountered a challenge with rendering issues during deployment on render.com. Although the dashboard runs smoothly locally, there’s a noticeable lag when deployed, particularly when interacting with large datasets. Despite reducing the dataset and optimizing the code, this performance issue remains a limitation. We plan to continue investigating potential solutions to improve response time.

**Deviations from Proposal**  
One deviation from our original proposal was the addition of the "Apply" button, which allows users to control when the plot updates. This change was made based on feedback that users wanted more control over data updates. Additionally, we modified the category selection logic so that "All" cannot be selected simultaneously with other categories. After clicking "Apply," selecting "All" clears any other category selections, ensuring clearer user interaction.

**Current Dashboard Strengths and Limitations**  
The dashboard is performing well, but there are still areas for improvement. While it runs well locally, the response time on the deployed version is slower than desired. Future improvements could include better dynamic filtering options and advanced data analysis features, such as predictive analytics, to provide deeper insights for advertisement companies.

Overall, the dashboard has improved significantly, with a more organized layout, better performance, and new features. If given more time, further refinements to the responsiveness and additional interactive features would enhance the dashboard’s usefulness.
