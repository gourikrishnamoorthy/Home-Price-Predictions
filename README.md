# Ames Housing Project

Data Source and data dictionary --> https://www.kaggle.com/c/dsi-us-10-project-2-regression-challenge/data

# GOAL - Way to predict a house price ~ actuals

 -- Choose attributes to formulate algorithms using past data
 -- To test the theory , use the algorithm found, to predict the price of known houses and check how it fared by measuring errors.
 -- Tweak the algorithm to reduce the errors as much as possible
 -- Keep testing to the extent possible to find the best fit model (repeat)
 -- Actual predictions using the model(s) within a threshold of +/- $20,000
 -- Publish and present the findings
 
# How to begin?

 -- Data cleaning
 -- Checking for missing values
 -- checking for incorrect values
 -- start exploring the data using data dictionary
 -- plot the distribution of your feature
 
# Predictions

  -- Base line predictions using mean
  -- Predictions using linear Regression. (Note: Tried RidgeCV, Lasso, but the scores did not improve so removed those from the list)
  -- Feature Selections using co-relation, statsmodels (OLS) 
  -- model creation
  -- using metrics to score the model
  -- using the model to test kaggle 
  

## Business Recommendations
- Features appear to add the most value to a home : Overall quality , living area , age of the house, lot area, have a wood deck , open porch , ratio of bedroom to bathroom , garage area 
- Which features hurt the value of a home the most : Pool related data did not impact the housing prices.
- What are things that homeowners could improve in their homes to increase the value? - mostly over all quality of the house, remodelling helped house prices.
- What neighborhoods seem like they might be a good investment? Stone Brook, North Ames, North Ridge
- Do you feel that this model will generalize to other cities? How could you revise your model to make it more universal OR what date would you need from another city to make a comparable model? - Cannot generalise to other cities. It can be only used as a baseline to think.
 
 
## Presentation : 

   [Link](Predicting_home_prices_for_Ames_Iowa.pdf)





