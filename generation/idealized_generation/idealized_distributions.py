"""Definitions of idealized distributions to use for definition.

These functions are called to generate formal descriptions for distributions, as
well as to sample from the corresponding distribution and return artifacts.
"""


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import seaborn as sns


# Constants for percentiles
percentiles_list = [
    1.0,
    10.0,
    20.0,
    30.0,
    40.0,
    50.0,
    60.0,
    70.0,
    80.0,
    90.0,
    99.0,
]


# Constants for percentiles
intermediate_percentiles_list = [
    5.0,
    15.0,
    25.0,
    35.0,
    45.0,
    55.0,
    65.0,
    75.0,
    85.0,
    95.0,
]


# Predefined probabilities
predefined_probabilities = [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
]


# Predefined probabilities
predefined_intermediate_probabilities = [
    0.05,
    0.15,
    0.25,
    0.35,
    0.45,
    0.55,
    0.65,
    0.75,
    0.85,
    0.95,
]


def calculate_target_percentile_values(samples, target_percentiles=None):
  """Calculate the target percentile values for given percentiles.

  Args:
    samples: The samples from the distribution.
    target_percentiles: A list of the percentiles to calculate.

  Returns:
    dict: A dictionary with 'percentile' 'percentile_value' keys containing the
  percentiles and their corresponding values.
  """

  percentile_values = np.percentile(samples, target_percentiles)
  return {
      round(percentile, 3): round(value, 3)
      for percentile, value in zip(target_percentiles, percentile_values)
  }


def calculate_probability_within_range(samples, lower_bound, upper_bound):
  """Calculate the probability that a value falls within a given range.

  Samples are constrained to the 1st and 99th percentiles.

  Args:
    samples: The samples from the distribution.
    lower_bound: The lower bound of the range.
    upper_bound: The upper bound of the range.

  Returns:
    float: The probability that a value falls within the range.
  """
  # Constrain the samples to the values between the 1st and 99th percentiles
  lower_percentile = np.percentile(samples, 1)
  upper_percentile = np.percentile(samples, 99)
  constrained_samples = samples[
      (samples >= lower_percentile) & (samples <= upper_percentile)
  ]

  # Count the number of samples within the range
  count_within_range = np.sum(
      (constrained_samples >= lower_bound)
      & (constrained_samples <= upper_bound)
  )
  # Calculate the probability
  probability = count_within_range / len(constrained_samples)
  return probability


def calculate_target_ranges(samples, target_probabilities=None):
  """Calculate the target ranges for given probabilities.

  Args:
    samples: The samples from the distribution.
    target_probabilities: A list of the probabilities to calculate.

  Returns:
    dict: A dictionary with probabilities as keys and their corresponding range
    values as tuples.
  """
  # Constrain the samples to the values between the 1st and 99th percentiles
  lower_bound = np.percentile(samples, 1)
  upper_bound = np.percentile(samples, 99)
  constrained_samples = samples[
      (samples >= lower_bound) & (samples <= upper_bound)
  ]

  target_ranges = {}
  for prob in target_probabilities:
    lower_quantile = np.percentile(constrained_samples, (1 - prob) / 2 * 100)
    upper_quantile = np.percentile(constrained_samples, (1 + prob) / 2 * 100)
    actual_prob = calculate_probability_within_range(
        constrained_samples, lower_quantile, upper_quantile
    )
    target_ranges[round(actual_prob, 3)] = (
        round(lower_quantile, 3),
        round(upper_quantile, 3),
    )
  return target_ranges


def normal_distribution(
    mean, std, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a normal distribution.

  Args:
    mean: The mean of the distribution.
    std: The standard deviation of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables, plot)
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """

  description = f"""
  Distribution Type: Normal Distribution
  Mean: {mean}
  Standard Deviation: {std}
  """

  np.random.seed(seed)
  samples = np.random.normal(mean, std, size=sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    print(
        'The description will not be changed since this is a normal'
        ' distribution.'
    )

  if debug:
    sns.histplot(samples, kde=True)
    plt.title(f'Normal Distribution w/ Mean of {mean} and Std of {std}')
    plt.xlabel('Number of Events')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(f'Returned {len(samples)} samples drawn for a normal distribution.')
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def log_normal_distribution(
    mean, sigma, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a log-normal distribution.

  Args:
    mean: The mean of the distribution.
    sigma: The standard deviation of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Log-Normal Distribution
  Characteristics: This distribution models values that are the result of the multiplicative product of many independent random variables, such as income levels, stock prices, or city sizes.
  Log Mean (mu): {mean}
  Log Sigma (sigma): {sigma}
  These parameters mean that the natural logarithm of the values follows a normal distribution with the specified mean and standard deviation.
  """

  np.random.seed(seed)
  samples = np.random.lognormal(mean, sigma, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Log-Normal Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100)
    plt.title(f'Log-Normal Distribution w/ Mean of {mean} and Sigma of {sigma}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a log-normal'
          ' distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def exponential_distribution(
    rate, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate an exponential distribution.

  Args:
    rate: The rate of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Exponential Distribution
  Characteristics: Models the time between events in a process where events occur continuously and independently at a constant average rate.
  Rate: {rate} (The average number of events per unit time is {1/rate:.2f}.)
  """

  np.random.seed(seed)
  samples = np.random.exponential(1 / rate, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Exponential Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100)
    plt.title(f'Exponential Distribution w/ Rate = {rate}')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for an exponential'
          ' distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def power_law_distribution(
    alpha, xmin, sample_size=1000000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a power law distribution.

  Args:
    alpha: The alpha parameter of the distribution.
    xmin: The xmin parameter of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Power Law Distribution
  Characteristics: Known for its heavy tails suitable for describing phenomena with a high incidence of extreme values.
  Alpha: {alpha} (Controls the tail heaviness—the smaller the alpha, the fatter the tail.)
  Xmin: {xmin} (Minimum value for which the power law behavior holds.)
  """

  np.random.seed(seed)
  samples = (
      xmin - 0.5
  ) * (1 - np.random.uniform(0, 1, sample_size)) ** (-1 / (alpha - 1))
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Power Law Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100, log_scale=True)
    plt.title(f'Power Law Distribution w/ Alpha = {alpha} and Xmin = {xmin}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a power law'
          ' distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def uniform_distribution(
    a, b, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a uniform distribution.

  Args:
    a: The minimum value of the distribution.
    b: The maximum value of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Uniform Distribution
  Characteristics: All values within the interval have equal probability of occurring.
  Min: {a} (Minimum value of the distribution.)
  Max: {b} (Maximum value of the distribution.)
  """

  np.random.seed(seed)
  samples = np.random.uniform(a, b, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Uniform Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100)
    plt.title(f'Uniform Distribution: Min={a}, Max={b}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a uniform distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def gamma_distribution(
    shape, scale, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a gamma distribution.

  Args:
    shape: The shape parameter of the distribution.
    scale: The scale parameter of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Gamma Distribution
  Characteristics: Used to model waiting times and life data among other things.
  Shape: {shape} (Controls the skewness of the distribution.)
  Scale: {scale} (Controls the spread of the distribution.)
  """

  np.random.seed(seed)
  samples = np.random.gamma(shape, scale, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Gamma Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100)
    plt.title(f'Gamma Distribution: Shape={shape}, Scale={scale}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(f'Returned {len(samples)} samples drawn for a gamma distribution.')
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def skew_normal_distribution(
    location, scale, skew, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a skew-normal distribution.

  Args:
    location: The location parameter of the distribution.
    scale: The scale parameter of the distribution.
    skew: The skew parameter of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Skew-Normal Distribution
  Characteristics: A generalization of the normal distribution to accommodate skewness.
  Location: {location} (Shifts the distribution along the x-axis.)
  Scale: {scale} (Controls the spread of the distribution.)
  Skew: {skew} (Determines the direction and degree of skewness.)
  """

  np.random.seed(seed)
  samples = scipy.stats.skewnorm.rvs(
      a=skew, loc=location, scale=scale, size=sample_size
  )
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Skew-Normal Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100)
    plt.title(
        f'Skew-Normal Distribution: Location={location}, Scale={scale},'
        f' Skew={skew}'
    )
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a skew-normal'
          ' distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def gumbel_distribution(
    loc, scale, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a Gumbel distribution.

  Args:
    loc: The location parameter of the distribution.
    scale: The scale parameter of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Gumbel Distribution
  Characteristics: Often used to model the distribution of extreme values.
  Location: {loc} (Centers the distribution.)
  Scale: {scale} (Controls the spread of the distribution.)
  """

  np.random.seed(seed)
  samples = np.random.gumbel(loc, scale, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Gumbel Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=True, bins=100)
    plt.title(f'Gumbel Distribution: Location={loc}, Scale={scale}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(f'Returned {len(samples)} samples drawn for a Gumbel distribution.')
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def poisson_distribution(
    lam, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a Poisson distribution.

  Args:
    lam: The lambda parameter of the distribution.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Poisson Distribution
  Characteristics: Suitable for modeling the number of events happening in a fixed interval of time or space.
  Lambda: {lam} (Average rate of events per interval.)
  """

  np.random.seed(seed)
  samples = np.random.poisson(lam, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Poisson Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=False, bins=30)
    plt.title(f'Poisson Distribution: Lambda={lam}')
    plt.xlabel('Number of Events')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a Poisson distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def geometric_distribution(
    p, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a geometric distribution.

  Args:
    p: The probability of success.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Geometric Distribution
  Characteristics: Models the number of trials until the first success.
  Probability of Success: {p}
  """

  np.random.seed(seed)
  samples = np.random.geometric(p, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Geometric Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=False, discrete=True)
    plt.title(f'Geometric Distribution: Probability of Success={p}')
    plt.xlabel('Number of Trials')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a geometric distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def binomial_distribution(
    n, p, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a binomial distribution.

  Args:
    n: The number of trials.
    p: The probability of success.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for the distribution.
  """
  description = f"""
  Distribution Type: Binomial Distribution
  Characteristics: Describes the number of successes in a fixed number of trials with a given probability of success.
  Trials: {n} (Total number of trials.)
  Probability of Success: {p} (Probability of success in each trial.)
  """

  np.random.seed(seed)
  samples = np.random.binomial(n, p, sample_size)
  samples = np.round(samples, 3)

  if approximate_as_normal:
    dist_mean = np.mean(samples)
    dist_std = np.std(samples)
    description = f"""
    Distribution Type: Normal Distribution
    Mean: {dist_mean}
    Standard Deviation: {dist_std}
    """

  if debug:
    sns.histplot(samples, kde=False, discrete=True, bins=n + 1)
    plt.title(f'Binomial Distribution: Trials={n}, Probability of Success={p}')
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

  if task == 'percentiles':
    target_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=percentiles_list
    )
    target_intermediate_percentile_values = calculate_target_percentile_values(
        samples, target_percentiles=intermediate_percentiles_list
    )
    if debug:
      print(description)
      print('Percentiles and their corresponding values:')
      for percentile, value in target_percentile_values.items():
        if percentile == 1:
          print(f'{percentile}st Percentile: {value}')
        else:
          print(f'{percentile}th Percentile: {value}')
    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    if debug:
      print(description)
      print(
          f'Returned {len(samples)} samples drawn for a binomial distribution.'
      )
      example_samples = np.random.choice(samples, 10)
      print(f'Example samples: {example_samples}')
    return description, samples
  elif task == 'probabilities':
    target_ranges = calculate_target_ranges(samples, predefined_probabilities)
    target_intermediate_ranges = calculate_target_ranges(
        samples, predefined_intermediate_probabilities
    )
    if debug:
      print(description)
      print('Probabilities and their corresponding ranges:')
      for prob, (lower, upper) in target_ranges.items():
        print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )


def multinomial_distribution(
    n, probs, sample_size=100000, seed=1337, task=None, debug=False,
    approximate_as_normal=False
):
  """Generate a multinomial distribution.

  Args:
    n: The number of trials.
    probs: The probabilities of each outcome.
    sample_size: The number of samples to generate.
    seed: Fixed seed for reproducibility.
    task: The task this distribution will be used for.
    debug: Whether or not to print debugging information (e.g., variables,
      plot).
    approximate_as_normal: Whether to approximate the distribution as normal.

  Returns:
    For all tasks:
      description: A description of the distribution.
    For percentiles task:
      target_percentile_values: A dictionary of target percentile values for
      each outcome.
    For sampling task:
      samples: The samples from the distribution.
    For probabilities task:
      target_ranges: A dictionary of target ranges for each outcome.
  """
  description = f"""
  Distribution Type: Multinomial Distribution
  Characteristics: Generalizes the binomial distribution for scenarios where each trial can result in more than two outcomes.
  Trials: {n} (Total number of trials.)
  Probabilities: {probs}
  """

  np.random.seed(seed)
  samples = np.random.multinomial(n, probs, size=sample_size)
  samples = np.round(samples, 3)

  if debug:
    for i in range(len(probs)):
      sns.histplot(
          samples[:, i],
          kde=False,
          discrete=True,
          color=np.random.rand(3,),
          label=f'Outcome {i+1}',
      )
    plt.title(f'Multinomial Distribution: Trials={n}, Probabilities={probs}')
    plt.xlabel('Number of Outcomes')
    plt.ylabel('Frequency')
    plt.legend(title='Outcomes')
    plt.grid(True)
    plt.show()

  if approximate_as_normal:
    # Calculate the mean and standard deviation for each outcome
    normal_means = [n * p for p in probs]
    normal_stds = [np.sqrt(n * p * (1 - p)) for p in probs]
    description = f"""
    Distribution Type: Normal Distribution (For each outcome)
    Characteristics: This distribution approximates the multinomial distribution for each outcome using the calculated means and standard deviations based on the probabilities.
    Means: {normal_means}
    Standard Deviations: {normal_stds}
    """

  if task == 'percentiles':
    target_percentile_values = {}
    target_intermediate_percentile_values = {}

    for i in range(len(probs)):
      target_percentile_values[f'Outcome {i+1}'] = (
          calculate_target_percentile_values(samples[:, i], percentiles_list)
      )
      target_intermediate_percentile_values[f'Outcome {i+1}'] = (
          calculate_target_percentile_values(
              samples[:, i], intermediate_percentiles_list
          )
      )

    if debug:
      print(description)
      for outcome, values in target_percentile_values.items():
        print(f'{outcome} Percentiles and their corresponding values:')
        for percentile, value in values.items():
          if percentile == 1:
            print(f'{percentile}st Percentile: {value}')
          else:
            print(f'{percentile}th Percentile: {value}')
      for outcome, values in target_intermediate_percentile_values.items():
        print(
            f'{outcome} Intermediate Percentiles and their corresponding'
            ' values:'
        )
        for percentile, value in values.items():
          if percentile == 1:
            print(f'{percentile}st Percentile: {value}')
          else:
            print(f'{percentile}th Percentile: {value}')

    return (
        description,
        target_percentile_values,
        target_intermediate_percentile_values,
    )
  elif task == 'sampling':
    samples_per_outcome = {
        f'Outcome {i+1}': samples[:, i] for i in range(len(probs))
    }
    if debug:
      print(description)
      print('Returned samples drawn for a multinomial distribution:')
      for outcome, outcome_samples in samples_per_outcome.items():
        random_samples = np.random.choice(outcome_samples, 10, replace=False)
        print(f'{outcome}: {random_samples} (10 random samples)')
    return description, samples_per_outcome
  elif task == 'probabilities':
    target_ranges = {}
    target_intermediate_ranges = {}
    for i in range(len(probs)):
      target_ranges[f'Outcome {i+1}'] = calculate_target_ranges(
          samples[:, i], predefined_probabilities
      )
    for i in range(len(probs)):
      target_intermediate_ranges[f'Outcome {i+1}'] = calculate_target_ranges(
          samples[:, i], predefined_intermediate_probabilities
      )
    if debug:
      print(description)
      for outcome, ranges in target_ranges.items():
        print(f'{outcome} Probabilities and their corresponding ranges:')
        for prob, (lower, upper) in ranges.items():
          print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
      for outcome, ranges in target_intermediate_ranges.items():
        print(
            f'{outcome} Intermediate Probabilities and their corresponding'
            ' ranges:'
        )
        for prob, (lower, upper) in ranges.items():
          print(f'Probability {prob:.3f}: Range ({lower}, {upper})')
    return description, target_ranges, target_intermediate_ranges
  else:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )
