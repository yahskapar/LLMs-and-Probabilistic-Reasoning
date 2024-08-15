"""Prompt templates for real-world data prompt generation.

These are the templates used to generate the real-world data prompts.
"""


avg_step_count_percentile_prompt = """
## You are an expert on population health and wearable fitness devices. Your task is to estimate the percentile of a given average step count value for a population that regularly uses Fitbit devices and is active on a daily basis. The data is filtered for individuals aged 18-65. The data is age-balanced and gender-balanced, and pertains to the U.S. population only. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a normal distribution of this data:


  Mean: 8366.971
  Standard Deviation: 3291.940


## Here is your question:
Question:
What is the percentile of the average step count value {target_number} steps for users of Fitbit devices? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


avg_resting_heart_rate_prompt = """
## You are an expert on population health and wearable fitness devices. Your task is to estimate the percentile of a given average resting heart rate value for a population that regularly uses Fitbit devices and is active on a daily basis. The data is filtered for individuals aged 18-65. The data is age-balanced and gender-balanced, and pertains to the U.S. population only. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a normal distribution of this data:


  Mean: 67.86
  Standard Deviation: 7.72


## Here is your question:
Question:
What is the percentile of the average resting heart rate value {target_number} beats per minute for users of Fitbit devices? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


avg_sleep_minutes_prompt = """
## You are an expert on population health and wearable fitness devices. Your task is to estimate the percentile of a given average sleep minutes count value for a population that regularly uses Fitbit devices and is active on a daily basis. The data is filtered for individuals aged 18-65. The data is age-balanced and gender-balanced, and pertains to the U.S. population only. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a skew-normal distribution of this data:


  Mean: 392.62
  Standard Deviation: 45.97


## Here is your question:
Question:
What is the percentile of the average sleep minutes count value {target_number} minutes for users of Fitbit devices? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


avg_activity_zone_minutes_prompt = """
## You are an expert on population health and wearable fitness devices. Your task is to estimate the percentile of a given average exercise minutes count value for a population that regularly uses Fitbit devices and is active on a daily basis. The data is filtered for individuals aged 18-65. The data is age-balanced and gender-balanced, and pertains to the U.S. population only. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a log-normal distribution of this data:


  Mean: 43.20
  Standard Deviation: 30.50


## Here is your question:
Question:
What is the percentile of the average exercise minutes count value {target_number} minutes for users of Fitbit devices? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


annual_household_income_percentile_prompt = """
## You are an expert on finance and statistics. Your task is to estimate the percentile of a given annual household income within the population using data from the year 2018 in the United States, sourced from the Census Bureau’s American Community Survey (ACS) Public Use Microdata Sample (PUMS). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a Gumbel distribution of this data:


  Mean: 66028.713
  Standard Deviation: 53616.018


## Here is your question:
Question:
What is the percentile of an annual household income value of ${target_number}? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


monthly_rentgrs_percentile_prompt = """
## You are an expert on finance and statistics. Your task is to estimate the percentile of a given monthly gross rent within the population using data from the year 2018 in the United States, sourced from the Census Bureau’s American Community Survey (ACS) Public Use Microdata Sample (PUMS). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a Gumbel distribution of this data:


  Mean: 1347.261
  Standard Deviation: 674.234


## Here is your question:
Question:
What is the percentile of a monthly gross rent of ${target_number}? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


annual_costelec_percentile_prompt = """
## You are an expert on finance and statistics. Your task is to estimate the percentile of a given annual electricity cost within the population using data from the year 2018 in the United States, sourced from the Census Bureau’s American Community Survey (ACS) Public Use Microdata Sample (PUMS). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a skew-normal distribution of this data:


  Mean: 1792.453
  Standard Deviation: 997.107


## Here is your question:
Question:
What is the percentile of an annual electricity cost of ${target_number}? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


annual_costwatr_percentile_prompt = """
## You are an expert on finance and statistics. Your task is to estimate the percentile of a given annual water cost within the population using data from the year 2018 in the United States, sourced from the Census Bureau’s American Community Survey (ACS) Public Use Microdata Sample (PUMS). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe an exponential distribution of this data:


  Mean: 584.638
  Standard Deviation: 520.797


## Here is your question:
Question:
What is the percentile of an annual water cost of ${target_number}? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


average_temperature_percentile_prompt = """
## You are an expert on climate science and statistics. Your task is to estimate the percentile of a given average temperature value using data from U.S. weather stations in the year 2018, sourced from the National Oceanic and Atmospheric Administration (NOAA) Global Historical Climatology Network Daily (GHCNd). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a normal distribution of this data:


  Mean: 10.643
  Standard Deviation: 12.628


## Here is your question:
Question:
What is the percentile of an average temperature of {target_number} degrees Celsius? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


annual_precipitation_percentile_prompt = """
## You are an expert on climate science and statistics. Your task is to estimate the percentile of a given annual precipitation value using data from U.S. weather stations in the year 2018, sourced from the National Oceanic and Atmospheric Administration (NOAA) Global Historical Climatology Network Daily (GHCNd). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a skew-normal distribution of this data:


  Mean: 754.201
  Standard Deviation: 505.754


## Here is your question:
Question:
What is the percentile of an annual precipitation value of {target_number} millimeters? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


average_wind_speed_percentile_prompt = """
## You are an expert on climate science and statistics. Your task is to estimate the percentile of a given average wind speed value using data from U.S. weather stations in the year 2018, sourced from the National Oceanic and Atmospheric Administration (NOAA) Global Historical Climatology Network Daily (GHCNd). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a log-normal distribution of this data:


  Mean: 3.303
  Standard Deviation: 1.723


## Here is your question:
Question:
What is the percentile of an average wind speed of {target_number} meters per second? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


average_relative_humidity_percentile_prompt = """
## You are an expert on climate science and statistics. Your task is to estimate the percentile of a given average relative humidity value using data from U.S. weather stations in the year 2018, sourced from the National Oceanic and Atmospheric Administration (NOAA) Global Historical Climatology Network Daily (GHCNd). Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following parameters that describe a skew-normal distribution of this data:


  Mean: 68.599
  Standard Deviation: 16.688


## Here is your question:
Question:
What is the percentile of an average relative humidity of {target_number}%? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""
