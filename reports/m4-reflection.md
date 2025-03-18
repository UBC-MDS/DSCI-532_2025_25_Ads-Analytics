# Milestone 4 Reflection

In Milestone 4, our team focused on improving the performance, usability, and organization of the dashboard. We implemented feedback from our professor and peers, refined the code, and made visual and functional enhancements to the dashboard. The main improvements included optimizing performance, fixing rendering issues, and enhancing the user interface.

**Feedback and Insights**  
A key piece of feedback was regarding the dashboard’s responsiveness during user interactions, especially with large datasets. Initially, the dashboard lagged when filtering by categories. To address this, we implemented data sampling, which sped up performance without compromising too much on accuracy. This insight helped us prioritize user interaction speed and balance it with the need for accurate data display. Additionally, we fixed the issue where selecting "All" and other specific categories simultaneously did not clear "All." After clicking "Apply," "All" is now automatically cleared if other categories are selected, improving clarity and user experience.

**Changes and Additions**  
We made several key changes to enhance the dashboard’s functionality and user interface:
- We removed unnecessary columns from the dataset, reducing clutter and simplifying the analysis.
- We cleaned up and refactored the `src` code to improve maintainability and performance.
- The filter widget was adjusted to stretch to the bottom of the page for a cleaner layout.
- We added a favicon, tab title, and footer for a more polished look.
- The X-axis was adjusted for better visualization, and a "no data" message was added when no filter is selected, improving clarity for users.

Additionally, we enhanced the visualizations by introducing more advanced charts, including word clouds, pie charts, and scatter plots. These updates allowed us to move beyond the basic density plots and histograms originally planned and provide a more comprehensive and engaging data analysis experience.

**Challenges**  
While we made several performance improvements, we still faced challenges with rendering issues during deployment on render.com. Although the dashboard runs smoothly locally, there is a noticeable lag when deployed, particularly when interacting with large datasets. We plan to continue investigating and optimizing the deployment to reduce this lag.

**Deviations from Proposal/Sketch**  
In our proposal, we initially planned to include basic visualizations such as density plots and histograms. However, in the final dashboard, we incorporated more advanced charts, including word clouds, box plots, pie charts, scatter plots, and bar charts. This deviation from the original plan allowed us to provide a more in-depth visual analysis of the data, making the dashboard more informative and engaging for our target audience.

**Current Dashboard Strengths and Limitations**  
The dashboard is performing well, with a more organized layout, improved speed, and additional features. However, the longer response time on the deployed version remains a limitation. Future improvements could include deploying the dashboard to a different hosting service for better performance, as well as adding more interactive features and advanced data analysis tools like predictive analytics.

Overall, the dashboard has improved significantly since Milestone 3, with better performance, enhanced visuals, and a more user-friendly layout. If given more time, further optimizations to responsiveness and additional features could make the dashboard even more valuable to advertisement companies.
