## U.S. Economic Dashboard using PowerBI

Built an ETL data pipeline that extracts state-level economic data from the last decade using BLS, Census, and BEA API's. Transfered data to a database in Microsoft SQL Server and connected the server to PowerBI to create a user interactive dashboard. The dashboard is filtered by 7 metrics over 10 years.

For code to work, user must obtain their own API key. To view pbix file, user must have Microsoft PowerBI installed. URL to launch dashboard: ecodashboard.streamlit.app.
[Launch dashboard here.](ecodashboard.streamlit.app)

## Overview

The time period between the early 2010's into present time is an intresting time for the U.S economy, as it is marked by significant global and domestic events, making it a crucial decade for tracking economic and financial performance. Several key factors shaped this period inlcuding: The Recovery of the Great Recession, the Rise of Technology and Automation, U.S.-China Trade Relations, the COVID-19 Pandemic, and record-breaking inflation rates. In this report, we will be tracking economic data for each state from 2011-2022.

## Metrics tracked

1. GDP (Gross Domestic Product):  reflects the overall economic output and growth, essential for understanding a state’s economic performance
   - Formula: Consumer Spending + Business Investment + Government Spending + Net Exports (Exports - Imports)
     
2. Median Household Income: shows how wealth is distributed and whether people’s living standards are improving

3. Cost of Living:  measures the average cost of essential goods and services, such as housing, food, healthcare, and transportation, relative to a base (often 100). Affects purchasing power and the real value of wages
   - Formula: (∑(Price of good/service*weight))/(Total Weights)

4. Poverty Rate: poverty rate represents the percentage of the population whose income falls below the poverty threshold, reveals economic inequality and the financial challenges faced by a significant portion of the population
   - Formula: (Number of people below the poverty line/Total Population) * 100
​
5. Unemployment Rate:  percentage of the labor force that is unemployed but actively seeking work, indicator of labor market's strength
   - Formula: (Unemployed/Labor Force) * 100
​
6. LFPR (Labor Force Participation Rate):  measures the percentage of the working-age population (16 years and older) that is employed
   - Formula: (Labor Force/Working Age Population) * 100

7. Job Growth: refers to the percentage increase in the number of jobs available in a state over a specific time period, reflecting the expansion of employment opportunities
   - Formula: ((Jobs At End of Period - Jobs at Beginning of Period) / Jobs at Beginning of Period) * 100
