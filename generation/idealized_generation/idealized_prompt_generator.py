"""General library for prompt generation.
"""

import bisect
import random
from templates.idealized_distributions import idealized


def generate_distribution_percentiles_stats_examples(
    distribution_description, target_percentile_values, num_shots,
    selected_outcome=None
):
  """Generates few-shot examples using distribution stats."""
  few_shot_examples = ''
  percentiles_map = {
      1: [50.0],
      3: [30.0, 50.0, 70.0],
      5: [10.0, 30.0, 50.0, 70.0, 90.0],
      7: [1.0, 10.0, 30.0, 50.0, 70.0, 90.0, 99.0],
      9: [1.0, 10.0, 20.0, 30.0, 50.0, 70.0, 80.0, 90.0, 99.0],
  }

  if num_shots == 0:
    return few_shot_examples

  percentiles = percentiles_map.get(num_shots, [])
  example_number = 1

  for percentile in percentiles:
    if selected_outcome is not None:
      # Multinomial case for a specific outcome
      values = target_percentile_values[selected_outcome]
      target_number = values.get(percentile)
      if target_number is not None:
        outcome_num = int(selected_outcome.split()[-1])
        few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
If outcome {outcome_num} appears {target_number} times, what is the percentile of this occurrence within the provided distribution?
Answer:
<answer>{percentile}</answer>
"""
        example_number += 1
    else:
      # Non-multinomial case
      target_number = target_percentile_values.get(percentile)
      if target_number is not None:
        few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
What is the percentile of {target_number} within the provided distribution?
Answer:
<answer>{percentile}</answer>
"""
        example_number += 1

  return few_shot_examples


def generate_intermediate_percentiles_stats_examples(
    distribution_description, intermediate_stats, num_shots,
    selected_outcome=None
):
  """Generates few-shot examples using intermediate stats."""
  few_shot_examples = ''
  percentiles_map = {
      1: [55.0],
      3: [35.0, 55.0, 75.0],
      5: [15.0, 35.0, 55.0, 75.0, 95.0],
      7: [5.0, 15.0, 35.0, 45.0, 55.0, 75.0, 95.0],
      9: [5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 75.0, 85.0, 95.0],
  }

  if num_shots == 0:
    return few_shot_examples

  percentiles = percentiles_map.get(num_shots, [])
  example_number = 1

  for percentile in percentiles:
    if selected_outcome is not None:
      # Multinomial case for a specific outcome
      values = intermediate_stats[selected_outcome]
      target_number = values.get(percentile)
      if target_number is not None:
        outcome_num = int(selected_outcome.split()[-1])
        few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
If outcome {outcome_num} appears {target_number} times, what is the percentile of this occurrence within the provided distribution?
Answer:
<answer>{percentile}</answer>
"""
        example_number += 1
    else:
      # Non-multinomial case
      target_number = intermediate_stats.get(percentile)
      if target_number is not None:
        few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
What is the percentile of {target_number} within the provided distribution?
Answer:
<answer>{percentile}</answer>
"""
        example_number += 1

  return few_shot_examples


def generate_few_shot_percentile_examples(
    examples, num_shots, _, selected_outcome=None
):
  """Generates few-shot examples for the percentiles task."""
  few_shot_examples = ''
  sampled_examples = random.sample(examples, min(num_shots, len(examples)))
  example_number = 1

  for _, example in enumerate(sampled_examples):
    example_description = example['description']
    target_percentile_values = example['target_percentile_values']

    if selected_outcome is not None:
      # Randomly select an outcome from the sampled example
      outcome = random.choice(list(target_percentile_values.keys()))
      outcome_num = int(
          outcome.split()[-1]
      )  # Extract the number from 'Outcome X'
      values = target_percentile_values[outcome]
      percentile, target_number = random.choice(list(values.items()))
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{example_description}
Question:
If outcome {outcome_num} appears {target_number} times, what is the percentile of this occurrence within the provided distribution?
Answer:
<answer>{percentile}</answer>
"""
    else:
      percentile, target_number = random.choice(
          list(target_percentile_values.items())
      )
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{example_description}
Question:
What is the percentile of {target_number} within the provided distribution?
Answer:
<answer>{percentile}</answer>
"""
    example_number += 1

  return few_shot_examples


def generate_percentiles_prompts(
    distributions_info,
    sample_count=10,
    shot_list=(0, 1, 3, 5, 7, 9),
    use_distribution_stats=False,
    use_intermediate_stats=False,
    use_nearest_shot=False
):
  """Generates prompts for the percentiles task.

  Args:
    distributions_info: A dict of the distribution to be asked about and
      examples.
    sample_count: The number of times to repeat each prompt.
    shot_list: List of shot counts to generate prompts for.
    use_distribution_stats: Use distribution stats as shot examples.
    use_intermediate_stats: Use intermediate stats as shot examples.

  Returns:
    prompts: A dictionary of prompts grouped by shot count and sample count.
  """
  prompts = {}

  for dist_name, dist_info in distributions_info.items():
    distribution_description = dist_info['description']
    examples = dist_info.get('examples', [])
    target_percentile_values = dist_info.get('target_percentile_values', {})
    intermediate_stats = dist_info.get(
        'target_intermediate_percentile_values', {}
    )

    if dist_name == 'multinomial':
      for outcome in target_percentile_values.keys():
        for num_shots in shot_list:
          if use_distribution_stats:
            few_shot_examples = (
                generate_distribution_percentiles_stats_examples(
                    distribution_description,
                    target_percentile_values,
                    num_shots,
                    selected_outcome=outcome,
                )
            )
          elif use_intermediate_stats:
            few_shot_examples = (
                generate_intermediate_percentiles_stats_examples(
                    distribution_description,
                    intermediate_stats,
                    num_shots,
                    selected_outcome=outcome,
                )
            )
          else:
            few_shot_examples = generate_few_shot_percentile_examples(
                examples, num_shots, dist_name, selected_outcome=outcome
            )

          for _, target_number in target_percentile_values[outcome].items():
            if use_nearest_shot:
              prompt = (
                  idealized.nearest_shot_multinomial_distribution_percentile_prompt.format(
                      few_shot_examples=few_shot_examples,
                      distribution_description=distribution_description,
                      target_number=target_number,
                      outcome_num=int(outcome.split()[-1]),
                  )
              )
            else:
              prompt = (
                  idealized.multinomial_distribution_percentile_prompt.format(
                      few_shot_examples=few_shot_examples,
                      distribution_description=distribution_description,
                      target_number=target_number,
                      outcome_num=int(outcome.split()[-1]),
                  )
              )
            prompt_name = (
                f'percentiles_{num_shots}_shots_{dist_name}_outcome_'
                f'{int(outcome.split()[-1])}_{sample_count}_samples'
            )
            if prompt_name not in prompts:
              prompts[prompt_name] = []
            # Repeat prompt based on SAMPLE_COUNT
            prompts[prompt_name].extend([prompt] * sample_count)
    else:
      for num_shots in shot_list:
        if use_distribution_stats:
          few_shot_examples = generate_distribution_percentiles_stats_examples(
              distribution_description, target_percentile_values, num_shots
          )
        elif use_intermediate_stats:
          few_shot_examples = generate_intermediate_percentiles_stats_examples(
              distribution_description, intermediate_stats, num_shots
          )
        else:
          few_shot_examples = generate_few_shot_percentile_examples(
              examples, num_shots, dist_name, selected_outcome=None
          )

        for _, target_number in target_percentile_values.items():
          if use_nearest_shot:
            prompt = (
                idealized.nearest_shot_distribution_percentile_prompt.format(
                    few_shot_examples=few_shot_examples,
                    distribution_description=distribution_description,
                    target_number=target_number,
                )
            )
          else:
            prompt = idealized.distribution_percentile_prompt.format(
                few_shot_examples=few_shot_examples,
                distribution_description=distribution_description,
                target_number=target_number,
            )
          prompt_name = (
              f'percentiles_{num_shots}_shots_{dist_name}_{sample_count}_'
              'samples'
          )
          if prompt_name not in prompts:
            prompts[prompt_name] = []
          # Repeat prompt based on SAMPLE_COUNT
          prompts[prompt_name].extend([prompt] * sample_count)

  return prompts


def generate_few_shot_sampling_examples(examples, num_shots, dist_name):
  """Generates few-shot examples for the sampling task."""
  few_shot_examples = ''

  for i in range(num_shots):
    example = random.choice(examples)
    example_description = example['description']
    samples = example['samples']

    if dist_name == 'multinomial':
      # Randomly select an outcome from the sampled example
      outcome = random.choice(list(samples.keys()))
      outcome_num = int(outcome.split()[-1])  # Extract the number from 'Outcome X'
      outcome_samples = samples[outcome]
      sample_value = random.choice(outcome_samples)
      few_shot_examples += f"""
Example {i + 1}:
Distribution:
{example_description}
Question:
Sample a number from the outcome {outcome_num} distribution and output only the numerical value.
Answer:
<answer>{sample_value}</answer>
"""
    else:
      sample_value = random.choice(samples)
      few_shot_examples += f"""
Example {i + 1}:
Distribution:
{example_description}
Question:
Sample a number from the provided distribution and output only the numerical value.
Answer:
<answer>{sample_value}</answer>
"""
  return few_shot_examples


def generate_distribution_stats_sampling_examples(
    distribution_description, samples, num_shots, selected_outcome=None
):
  """Generates few-shot examples using distribution stats."""
  few_shot_examples = ''

  for i in range(num_shots):
    if selected_outcome is not None:
      # Multinomial case for a specific outcome
      outcome_samples = samples[selected_outcome]
      sample_value = random.choice(outcome_samples)
      outcome_num = int(selected_outcome.split()[-1])
      few_shot_examples += f"""
Example {i + 1}:
Distribution:
{distribution_description}
Question:
Sample a number from the outcome {outcome_num} distribution and output only the numerical value.
Answer:
<answer>{sample_value}</answer>
"""
    else:
      # Non-multinomial case
      sample_value = random.choice(samples)
      few_shot_examples += f"""
Example {i + 1}:
Distribution:
{distribution_description}
Question:
Sample a number from the provided distribution and output only the numerical value.
Answer:
<answer>{sample_value}</answer>
"""
  return few_shot_examples


def generate_sampling_prompts(
    distributions_info,
    sample_count=1000,
    shot_list=(0, 1, 3, 5, 7, 9),
    use_distribution_stats=False,
):
  """Generates prompts for the sampling task.

  Args:
    distributions_info: A dict of the distribution to be asked about and
      examples.
    sample_count: The number of times to repeat each prompt.
    shot_list: List of shot counts to generate prompts for.
    use_distribution_stats: Use distribution stats as shot examples.

  Returns:
    prompts: A dictionary of prompts grouped by shot count and sample count.
  """
  prompts = {}

  for dist_name, dist_info in distributions_info.items():
    distribution_description = dist_info['description']
    examples = dist_info.get('examples', [])
    samples = dist_info.get('samples', {})

    for num_shots in shot_list:
      for _ in range(
          sample_count
      ):  # Loop to ensure unique samples for each prompt
        if use_distribution_stats:
          if dist_name == 'multinomial':
            for outcome in samples.keys():
              few_shot_examples = generate_distribution_stats_sampling_examples(
                  distribution_description,
                  samples,
                  num_shots,
                  selected_outcome=outcome,
              )
              outcome_num = int(outcome.split()[-1])
              prompt = idealized.multinomial_distribution_sample_prompt.format(
                  few_shot_examples=few_shot_examples,
                  distribution_description=distribution_description,
                  outcome_num=outcome_num,
              )
              prompt_name = (
                  f'sampling_{num_shots}_shots_{dist_name}_outcome_'
                  f'{outcome_num}_{sample_count}_samples'
              )
              if prompt_name not in prompts:
                prompts[prompt_name] = []
              prompts[prompt_name].append(prompt)  # Append prompt directly
          else:
            few_shot_examples = generate_distribution_stats_sampling_examples(
                distribution_description, samples, num_shots
            )
            prompt = idealized.distribution_sample_prompt.format(
                few_shot_examples=few_shot_examples,
                distribution_description=distribution_description,
            )
            prompt_name = (
                f'sampling_{num_shots}_shots_{dist_name}_{sample_count}_samples'
            )
            if prompt_name not in prompts:
              prompts[prompt_name] = []
            prompts[prompt_name].append(prompt)  # Append prompt directly
        else:
          few_shot_examples = generate_few_shot_sampling_examples(
              examples, num_shots, dist_name
          )

          if dist_name == 'multinomial':
            for outcome in samples.keys():
              outcome_num = int(outcome.split()[-1])
              prompt = idealized.multinomial_distribution_sample_prompt.format(
                  few_shot_examples=few_shot_examples,
                  distribution_description=distribution_description,
                  outcome_num=outcome_num,
              )
              prompt_name = (
                  f'sampling_{num_shots}_shots_{dist_name}_outcome_'
                  f'{outcome_num}_{sample_count}_samples'
              )
              if prompt_name not in prompts:
                prompts[prompt_name] = []
              prompts[prompt_name].append(prompt)  # Append prompt directly
          else:
            prompt = idealized.distribution_sample_prompt.format(
                few_shot_examples=few_shot_examples,
                distribution_description=distribution_description,
            )
            prompt_name = (
                f'sampling_{num_shots}_shots_{dist_name}_{sample_count}_samples'
            )
            if prompt_name not in prompts:
              prompts[prompt_name] = []
            prompts[prompt_name].append(prompt)  # Append prompt directly

  return prompts


def generate_distribution_probabilities_stats_examples(
    distribution_description, target_ranges, num_shots, selected_outcome=None
):
  """Generates few-shot examples using distribution stats and probabilities map."""
  probabilities_map = {
      1: [0.5],
      3: [0.3, 0.5, 0.7],
      5: [0.1, 0.3, 0.5, 0.7, 0.9],
      7: [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9],
      9: [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 0.9, 1.0],
  }

  few_shot_examples = ''
  example_number = 1

  def closest_probability(probs, target):
    """Find the closest probability in the list to the target value."""
    pos = bisect.bisect_left(probs, target)
    if pos == 0:
      return probs[0]
    if pos == len(probs):
      return probs[-1]
    before = probs[pos - 1]
    after = probs[pos]
    if after - target < target - before:
      return after
    else:
      return before

  if num_shots == 0:
    return few_shot_examples
  elif num_shots in probabilities_map:
    target_probs = probabilities_map[num_shots]
  else:
    raise ValueError(f'Unsupported number of shots: {num_shots}')

  for target_prob in target_probs:
    if selected_outcome is not None:
      # Multinomial case for a specific outcome
      values = target_ranges[selected_outcome]
      outcome_num = int(selected_outcome.split()[-1])
      closest_prob = closest_probability(list(values.keys()), target_prob)
      lower, upper = values[closest_prob]
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from outcome {outcome_num} is between {lower} and {upper} within the provided distribution?
Answer:
<answer>{closest_prob}</answer>
"""
    else:
      # Non-multinomial case
      closest_prob = closest_probability(
          list(target_ranges.keys()), target_prob
      )
      lower, upper = target_ranges[closest_prob]
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from the provided distribution is between {lower} and {upper}?
Answer:
<answer>{closest_prob}</answer>
"""
    example_number += 1

  return few_shot_examples


def generate_intermediate_probabilities_stats_examples(
    distribution_description,
    target_intermediate_ranges,
    num_shots,
    selected_outcome=None,
):
  """Generates few-shot examples using distribution stats and probabilities map."""
  probabilities_map = {
      1: [0.55],
      3: [0.33, 0.55, 0.75],
      5: [0.15, 0.35, 0.55, 0.75, 0.95],
      7: [0.15, 0.25, 0.35, 0.55, 0.75, 0.85, 0.95],
      9: [0.05, 0.15, 0.25, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95],
  }

  few_shot_examples = ''
  example_number = 1

  def closest_probability(probs, target):
    """Find the closest probability in the list to the target value."""
    pos = bisect.bisect_left(probs, target)
    if pos == 0:
      return probs[0]
    if pos == len(probs):
      return probs[-1]
    before = probs[pos - 1]
    after = probs[pos]
    if after - target < target - before:
      return after
    else:
      return before

  if num_shots == 0:
    return few_shot_examples
  elif num_shots in probabilities_map:
    target_probs = probabilities_map[num_shots]
  else:
    raise ValueError(f'Unsupported number of shots: {num_shots}')

  for target_prob in target_probs:
    if selected_outcome is not None:
      # Multinomial case for a specific outcome
      values = target_intermediate_ranges[selected_outcome]
      outcome_num = int(selected_outcome.split()[-1])
      closest_prob = closest_probability(list(values.keys()), target_prob)
      lower, upper = values[closest_prob]
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from outcome {outcome_num} is between {lower} and {upper} within the provided distribution?
Answer:
<answer>{closest_prob}</answer>
"""
    else:
      # Non-multinomial case
      closest_prob = closest_probability(
          list(target_intermediate_ranges.keys()), target_prob
      )
      lower, upper = target_intermediate_ranges[closest_prob]
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{distribution_description}
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from the provided distribution is between {lower} and {upper}?
Answer:
<answer>{closest_prob}</answer>
"""
    example_number += 1

  return few_shot_examples


def generate_few_shot_probabilities_examples(
    examples, num_shots, _, selected_outcome=None
):
  """Generates few-shot examples for the probabilities task."""
  few_shot_examples = ''
  sampled_examples = random.sample(examples, min(num_shots, len(examples)))
  example_number = 1

  for _, example in enumerate(sampled_examples):
    example_description = example['description']
    target_ranges = example['target_ranges']

    if selected_outcome is not None:
      # Randomly select an outcome from the sampled example
      outcome = random.choice(list(target_ranges.keys()))
      outcome_num = int(
          outcome.split()[-1]
      )  # Extract the number from 'Outcome X'
      values = target_ranges[outcome]
      prob, (lower, upper) = random.choice(list(values.items()))
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{example_description}
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from outcome {outcome_num} is between {lower} and {upper} within the provided distribution?
Answer:
<answer>{prob}</answer>
"""
    else:
      prob, (lower, upper) = random.choice(list(target_ranges.items()))
      few_shot_examples += f"""
Example {example_number}:
Distribution:
{example_description}
Question:
Considering only values including and between the 1st percentile and the 99th percentile, what is the probability that a value from the provided distribution is between {lower} and {upper}?
Answer:
<answer>{prob}</answer>
"""
    example_number += 1

  return few_shot_examples


def generate_probabilities_prompts(
    distributions_info,
    sample_count=10,
    shot_list=(0, 1, 3, 5, 7, 9),
    use_distribution_stats=False,
    use_intermediate_stats=False,
):
  """Generates prompts for the probabilities task.

  Args:
    distributions_info: A dict of the distribution to be asked about and
      examples.
    sample_count: The number of times to repeat each prompt.
    shot_list: List of shot counts to generate prompts for.
    use_distribution_stats: Use distribution stats as shot examples.
    use_intermediate_stats: Use intermediate stats as shot examples.

  Returns:
    prompts: A dictionary of prompts grouped by shot count and sample count.
  """
  prompts = {}

  for dist_name, dist_info in distributions_info.items():
    distribution_description = dist_info['description']
    examples = dist_info.get('examples', [])
    target_ranges = dist_info.get('target_ranges', {})
    target_intermediate_ranges = dist_info.get(
        'target_intermediate_ranges', {}
    )

    if dist_name == 'multinomial':
      for outcome in target_ranges.keys():
        for num_shots in shot_list:
          if use_distribution_stats:
            few_shot_examples = (
                generate_distribution_probabilities_stats_examples(
                    distribution_description,
                    target_ranges,
                    num_shots,
                    selected_outcome=outcome,
                )
            )
          elif use_intermediate_stats:
            few_shot_examples = (
                generate_intermediate_probabilities_stats_examples(
                    distribution_description,
                    target_intermediate_ranges,
                    num_shots,
                    selected_outcome=outcome,
                )
            )
          else:
            few_shot_examples = generate_few_shot_probabilities_examples(
                examples, num_shots, dist_name, selected_outcome=outcome
            )

          for _, (lower, upper) in target_ranges[outcome].items():
            prompt = (
                idealized.multinomial_distribution_probability_prompt.format(
                    few_shot_examples=few_shot_examples,
                    distribution_description=distribution_description,
                    lower_target_number=lower,
                    upper_target_number=upper,
                    outcome_num=int(outcome.split()[-1]),
                )
            )
            prompt_name = (
                f'probabilities_{num_shots}_shots_{dist_name}_outcome_'
                f'{int(outcome.split()[-1])}_{sample_count}_samples'
            )
            if prompt_name not in prompts:
              prompts[prompt_name] = []
            # Repeat prompt based on SAMPLE_COUNT
            prompts[prompt_name].extend([prompt] * sample_count)
    else:
      for num_shots in shot_list:
        if use_distribution_stats:
          few_shot_examples = (
              generate_distribution_probabilities_stats_examples(
                  distribution_description, target_ranges, num_shots
              )
          )
        elif use_intermediate_stats:
          few_shot_examples = (
              generate_intermediate_probabilities_stats_examples(
                  distribution_description,
                  target_intermediate_ranges,
                  num_shots,
              )
          )
        else:
          few_shot_examples = generate_few_shot_probabilities_examples(
              examples, num_shots, dist_name
          )

        for _, (lower, upper) in target_ranges.items():
          prompt = idealized.distribution_probability_prompt.format(
              few_shot_examples=few_shot_examples,
              distribution_description=distribution_description,
              lower_target_number=lower,
              upper_target_number=upper,
          )
          prompt_name = (
              f'probabilities_{num_shots}_shots_{dist_name}_{sample_count}_'
              'samples'
          )
          if prompt_name not in prompts:
            prompts[prompt_name] = []
          # Repeat prompt based on SAMPLE_COUNT
          prompts[prompt_name].extend([prompt] * sample_count)

  return prompts
