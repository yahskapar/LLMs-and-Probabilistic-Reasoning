"""Prompt templates for real-world data prompt generation.

These are the templates with idealized distributions described in place of the
corresponding real-world distributions.
"""


idealized_avg_step_count_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100.  Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Normal Distribution
  Mean: 8366.971
  Standard Deviation: 3291.940


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_avg_resting_heart_rate_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Normal Distribution
  Mean: 67.882
  Standard Deviation: 7.723


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_avg_sleep_minutes_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Skew-Normal Distribution
  Characteristics: A generalization of the normal distribution to accommodate skewness.
  Location: 427.930 (Shifts the distribution along the x-axis.)
  Scale: 58.050 (Controls the spread of the distribution.)
  Skew: -1.177 (Determines the direction and degree of skewness.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_avg_activity_zone_minutes_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Log-Normal Distribution
  Characteristics: This distribution models values that are the result of the multiplicative product of many independent random variables, such as income levels, stock prices, or city sizes.
  Log Mean (mu): 3.543
  Log Sigma (sigma): 0.677
  These parameters mean that the natural logarithm of the values follows a normal distribution with the specified mean and standard deviation.


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_annual_household_income_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Gumbel Distribution
  Characteristics: Often used to model the distribution of extreme values.
  Location: 43788.542 (Centers the distribution.)
  Scale: 35382.156 (Controls the spread of the distribution.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_monthly_rentgrs_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Gumbel Distribution
  Characteristics: Often used to model the distribution of extreme values.
  Location: 1053.066 (Centers the distribution.)
  Scale: 488.890 (Controls the spread of the distribution.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_annual_costelec_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Skew-Normal Distribution
  Characteristics: A generalization of the normal distribution to accommodate skewness.
  Location: 509.827 (Shifts the distribution along the x-axis.)
  Scale: 1624.607 (Controls the spread of the distribution.)
  Skew: 7.105 (Determines the direction and degree of skewness.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_annual_costwatr_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Exponential Distribution
  Characteristics: Models the intervals or amounts in a process where changes occur continuously and independently at a constant average rate.
  Rate: 0.00172 (This corresponds to an average of 581.395 units per interval.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_average_temperature_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Normal Distribution
  Mean: 10.643
  Standard Deviation: 12.628


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_annual_precipitation_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Skew-Normal Distribution
  Characteristics: A generalization of the normal distribution to accommodate skewness.
  Location: 60.505 (Shifts the distribution along the x-axis.)
  Scale: 858.484 (Controls the spread of the distribution.)
  Skew: 13.395 (Determines the direction and degree of skewness.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_average_wind_speed_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Log-Normal Distribution
  Characteristics: This distribution models values that are the result of the multiplicative product of many independent random variables, such as income levels, stock prices, or city sizes.
  Log Mean (mu): 1.558
  Log Sigma (sigma): 0.340
  These parameters mean that the natural logarithm of the values follows a normal distribution with the specified mean and standard deviation.


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""


idealized_average_relative_humidity_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.

## Consider the following distribution:


  Distribution Type: Skew-Normal Distribution
  Characteristics: A generalization of the normal distribution to accommodate skewness.
  Location: 89.849 (Shifts the distribution along the x-axis.)
  Scale: 27.019 (Controls the spread of the distribution.)
  Skew: -4.939 (Determines the direction and degree of skewness.)


## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not use any additional tools such as code generation or search engines. Answer with just a numerical response from 0 to 100. Make sure your answer is enclosed by xml tags <answer> and </answer>.
Answer:
"""
