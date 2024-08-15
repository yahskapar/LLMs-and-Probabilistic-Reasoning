"""Prompt templates for idealized data prompt generation.

These are the templates used to generate the idealized data prompts. Note that
there is a generic template and then a multinomial template, primarily since in
the multinomial case we need to consider outcomes individually.
"""


distribution_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Answer with just a numerical response from 0 to 100. Make sure your final answer is enclosed by xml tags <answer> and </answer>

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:

{distribution_description}

## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution?
Answer:
"""

multinomial_distribution_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a multinomial distribution. Answer with just a numerical response from 0 to 100. Make sure your final answer is enclosed by xml tags <answer> and </answer>

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:
{distribution_description}

## Here is your question:
Question:
If outcome {outcome_num} appears {target_number} times, what is the percentile of this occurrence within the provided distribution?
Answer:
"""


nearest_shot_distribution_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a specific distribution. Answer with just a numerical response from 0 to 100. Make sure your final answer is enclosed by xml tags <answer> and </answer>

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:

{distribution_description}

## Here is your question:
Question:
What is the percentile of the value {target_number} within the provided distribution? Do not answer the question directly, instead pick the nearest example's answer provided above as your answer.
Answer:
"""


nearest_shot_multinomial_distribution_percentile_prompt = """
## You are an expert on statistics. Your task is to estimate the percentile of a number within a multinomial distribution. Answer with just a numerical response from 0 to 100. Make sure your final answer is enclosed by xml tags <answer> and </answer>

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:
{distribution_description}

## Here is your question:
Question:
If outcome {outcome_num} appears {target_number} times, what is the percentile of this occurrence within the provided distribution? Do not answer the question directly, instead pick the nearest example's answer provided above as your answer.
Answer:
"""

distribution_sample_prompt = """
## You are an expert on statistics. Your task is to sample a number from a given distribution. Do not write any code or use any additional tools to perform the sampling. Answer with just a numerical response. Make sure your final answer is enclosed by xml tags <answer> and </answer>

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:
{distribution_description}

## Instruction: Sample a number from the given distribution and output only the numerical value.
"""


multinomial_distribution_sample_prompt = """
## You are an expert on statistics. Your task is to sample a number from a given distribution. Do not write any code or use any additional tools to perform the sampling. Answer with just a numerical response. Make sure your final answer is enclosed by xml tags <answer> and </answer>

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:
{distribution_description}

## Instruction: Sample a number from the outcome {outcome_num} distribution and output only the numerical value.
"""


distribution_probability_prompt = """
## You are an expert on statistics. Your task is to estimate the probability of being in a range of values within a given distribution. Answer with just a numerical response from 0 to 1, representing the probability. Make sure your final answer is enclosed by xml tags <answer> and </answer>.

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:
{distribution_description}

## Here is your question:
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from the provided distribution is between {lower_target_number} and {upper_target_number}?
Answer:
"""


multinomial_distribution_probability_prompt = """
## You are an expert on statistics. Your task is to estimate the probability of being in a range of values within a given distribution. Answer with just a numerical response from 0 to 1, representing the probability. Make sure your final answer is enclosed by xml tags <answer> and </answer>.

## Here are some examples to help you understand the task:

{few_shot_examples}

## Consider the following distribution:
{distribution_description}

## Here is your question:
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from the outcome {outcome_num} distribution is between {lower_target_number} and {upper_target_number}?
Answer:
"""
