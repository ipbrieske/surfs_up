# Overview
In this project, we use SQLite, Jupyter Notebooks, and VSCode to analyze weather data on the island of Oahu for a surf shop startup. Our data comes from the hawaii.sqlite database, and we have leveraged SQLAlchemy to read the database using reflection. This project has been created at the request of our client in order to determine the viability of a business focused on surfing and ice cream. Such a business faces business risk stemming from increased precipitation and adverse temperatures. The initial exploratory analysis is available in climate_analysis.ipynb, and demonstrates our dataset includes temperature and precipitation readings from a number of weather stations in Oahu. This initial analysis focuses on temperatures for the months of June and December, from 2016 through 2017. 

# Results
By reflecting the sqlite database into a pandas dataframe, we have been able to make some quick observations about the temperatures during June and December:

- The lowest temperature in December was 56 degrees Fahrenheit. This was an unlikely reading, as 69 degrees proved the barrier the bottom and next quartile.
    - Temperatures even in December would be very conducive to sales of frozen novelties

- The mean temperatures for June and December were 75 and 71 degrees, respectively.
    - With a variance of only 4 degrees between the two seasonal extremes, we can say that the temperature in Oahu stays relatively consistent throughout the year, allowing for year-round sales of ice creams and board wax. 

- December temperatures are more volatile than June temperatures.
    - Standard deviation of temperature readings were higher in December (3.74) than in June (3.26). While having a low of 56 degrees, temperatures spiked to as high as 83 degrees during the winter month. This adds a certain degree of uncertainty to business conditions during the month of December. 

# Summary
Overall, we are able to say that temperatures appear to remain quite stable throughout the year in Oahu. They maintain the 'Goldilocks' range of not too hot and not too cold. This bodes well for our client's ice cream/surf shop business, as temperatures amenable to beach-going activities will drive business growth. December introduces an aspect of volatility, but the importance of these temperature variations do not bear as much weight as the variations in precipitation. 

To deepen our analysis, a similar overview of precipitations should be performed. I have taken the liberty of doing just so as seen at the end of SurfsUp_Challenge.ipynb, where I have queried the precipitation table to determine mean, median, and extreme precipitations. While precipitation appears quite low usually, a few extreme downpours occur. When it rains, it pours in Oahu it seems. Our client would be wise to monitor weather conditions regularly to avoid doing business during these extreme precipitation periods. 

Another way to deepen our analysis would be to count the number of days with precipitation above a certain threshold - say above the 75th percentile - to inform our client how many days they can expect to be closed for business per month, in order to adjust inventories and pricing accordingly. I have taken the first step in this direction by determining the number of precipitation readings in December above the 3rd quartile, but this data should be appended with dates of each reading and then grouped by each date to show the true number of days with abnormal precipitation. 