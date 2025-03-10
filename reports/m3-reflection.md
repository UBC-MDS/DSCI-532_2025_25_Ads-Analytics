# Dashboard Progress Reflection (Post-Milestone 2)

## 1. Implemented Parts Since Milestone 2
- Added missing demo.gif in README.md
- Splited the large app.py into 3 parts (app.py, layout.py, callbacks.py). Also organized src folder better by moving all charts creation related scripts to charts/
- Changed the bottom bar chart (Top 10 apps by installs) to word cloud
- Added a popularity score metric which is calculated by the average of normalized log(installs), log(reviews) and ratings.
- Filter the processed csv file and generate a new file only containing entries that top ten highest popularity score by category.
- By default there are ten categories selected, and will display the plot for these ten categories if selecting "All" in the Global Filter.
- Add a uniform color scheme so the same category will share the same color over all the plots
- Changed the density plot to box jenkos plot for better visulization to display ratings vs categories
- Adjust the margin and plot size to make all the plot the same size
- Replace the number of installs plot with the popularity score plot

## 2. Parts Not Yet Implemented
- Performance improvement
    - This will be implemented in Milestone 4, as this will be covered in next week's lecture.
- Layout Improvement
    - Could move the legend outside the plot

## 3. Differences from Proposal/Sketch
- Still maintaining same layout as proposal with further enhancements

## 4. Corner Cases or Unresolved Issues
- Still unable to resolve render deploy issues, even after reducing dataset

## 5. Deviation from Best Practices (if applicable)

## 6. Reflection on the Dashboard
- We have evolved in the dashboard app development, we now have active and interactive filters, KPI cards and the dashboard has taken a good shape

### What the Dashboard Does Well:

### Limitations or Areas for Improvement:
- Still looking into more outlook enhancements

### Potential Future Improvements or Additions:
- Having additional chart that better communicate with our audience