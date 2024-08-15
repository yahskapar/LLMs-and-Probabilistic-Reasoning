"""Generate idealized distributions alongside inputs for prompt generation.

Up to 12 idealized distributions with their own, unique descriptions are
supported. Depending on the task (e.g., percentiles, sampling, probabilities)
different artifacts are returned in order to facilitate prompt generation.
"""

import pprint
import numpy as np
from generation.idealized_generation import idealized_distributions

# Distribution configuration for questions
distribution_questions_config = [
    {
        'name': 'normal',
        'func': idealized_distributions.normal_distribution,
        'params': {'mean': 100, 'std': 10},
    },
    {
        'name': 'log_normal',
        'func': idealized_distributions.log_normal_distribution,
        'params': {'mean': 4.0, 'sigma': 0.5},
    },
    {
        'name': 'exponential',
        'func': idealized_distributions.exponential_distribution,
        'params': {'rate': 1 / 100},
    },
    {
        'name': 'power_law',
        'func': idealized_distributions.power_law_distribution,
        'params': {'alpha': 1.8, 'xmin': 100},
    },
    {
        'name': 'uniform',
        'func': idealized_distributions.uniform_distribution,
        'params': {'a': 70, 'b': 130},
    },
    {
        'name': 'gamma',
        'func': idealized_distributions.gamma_distribution,
        'params': {'shape': 2.0, 'scale': 20},
    },
    {
        'name': 'skew_normal',
        'func': idealized_distributions.skew_normal_distribution,
        'params': {'location': 100, 'scale': 10, 'skew': -10},
    },
    {
        'name': 'gumbel',
        'func': idealized_distributions.gumbel_distribution,
        'params': {'loc': 1000, 'scale': 1000},
    },
    {
        'name': 'poisson',
        'func': idealized_distributions.poisson_distribution,
        'params': {'lam': 70},
    },
    {
        'name': 'geometric',
        'func': idealized_distributions.geometric_distribution,
        'params': {'p': 0.05},
    },
    {
        'name': 'binomial',
        'func': idealized_distributions.binomial_distribution,
        'params': {'n': 1000, 'p': 0.5},
    },
    {
        'name': 'multinomial',
        'func': idealized_distributions.multinomial_distribution,
        'params': {'n': 1000, 'probs': [0.2, 0.3, 0.5]},
    },
]

# Distribution configuration with parameter ranges for generating examples
distribution_examples_config = [
    {
        'name': 'normal',
        'func': idealized_distributions.normal_distribution,
        'params': {'mean': (80, 120), 'std': (5, 20)},
    },
    {
        'name': 'log_normal',
        'func': idealized_distributions.log_normal_distribution,
        'params': {'mean': (3.0, 10.0), 'sigma': (0.3, 1.5)},
    },
    {
        'name': 'exponential',
        'func': idealized_distributions.exponential_distribution,
        'params': {'rate': (1 / 200, 1 / 50)},
    },
    {
        'name': 'power_law',
        'func': idealized_distributions.power_law_distribution,
        'params': {'alpha': (1.5, 2.0), 'xmin': (80, 200)},
    },
    {
        'name': 'uniform',
        'func': idealized_distributions.uniform_distribution,
        'params': {'a': (50, 100), 'b': (100, 150)},
    },
    {
        'name': 'gamma',
        'func': idealized_distributions.gamma_distribution,
        'params': {'shape': (1.5, 2.5), 'scale': (15, 30)},
    },
    {
        'name': 'skew_normal',
        'func': idealized_distributions.skew_normal_distribution,
        'params': {'location': (80, 120), 'scale': (5, 20), 'skew': (-10, 10)},
    },
    {
        'name': 'gumbel',
        'func': idealized_distributions.gumbel_distribution,
        'params': {'loc': (800, 1200), 'scale': (800, 1200)},
    },
    {
        'name': 'poisson',
        'func': idealized_distributions.poisson_distribution,
        'params': {'lam': (50, 90)},
    },
    {
        'name': 'geometric',
        'func': idealized_distributions.geometric_distribution,
        'params': {'p': (0.01, 0.07)},
    },
    {
        'name': 'binomial',
        'func': idealized_distributions.binomial_distribution,
        'params': {'n': (800, 1200), 'p': (0.3, 0.7)},
    },
    {
        'name': 'multinomial',
        'func': idealized_distributions.multinomial_distribution,
        # 'probs' will be set inside generate_random_params() using dirichlet
        'params': {'n': (800, 1200), 'probs': (None, None, None)},
    },
]


def generate_probabilities(min_threshold=0.1, num_categories=3):
  """Generates probabilities ensuring none are less than 0.1.

  Args:
    min_threshold: The minimum threshold for each probability.
    num_categories: The number of categories.

  Returns:
    A list of probabilities.

  Raises:
    ValueError: If the minimum threshold is too high for the number of
    categories.
  """
  # Ensure that the minimum threshold is feasible with the number of categories
  if min_threshold * num_categories > 1.0:
    raise ValueError(
        f'min_threshold {min_threshold} is too high for'
        f' {num_categories} categories.'
    )

  while True:
    # Generate probabilities using Dirichlet distribution
    probs = np.random.dirichlet(np.ones(num_categories))

    # Check if all probabilities are above the minimum threshold
    if all(probs >= min_threshold):
      break

  # Round the probabilities to two decimal places without altering the sum
  rounded_probs = np.round(probs, 3)

  # If rounding caused a sum different from 1.0, adjust the largest probability
  rounding_error = 1.0 - np.sum(rounded_probs)
  if abs(rounding_error) > 1e-9:
    # Adjust the largest probability to correct rounding error
    max_index = np.argmax(rounded_probs)
    rounded_probs[max_index] += rounding_error

  # Final check to ensure sum is exactly 1.0
  if not np.isclose(np.sum(rounded_probs), 1.0):
    raise ValueError(
        f'Rounding issue with probs: sum is {np.sum(rounded_probs)} instead of'
        ' 1.0!'
    )

  return rounded_probs


def params_equal(
    params1, params2, rate_tolerance=1e-3, general_tolerance=1e-2, debug=False
):
  """Checks if two parameter dictionaries are equal.

  Args:
    params1: The first parameter dictionary.
    params2: The second parameter dictionary.
    rate_tolerance: The tolerance for the rate parameter.
    general_tolerance: The general tolerance for all other parameters.
    debug: Whether to print debug information.

  Returns:
    True if the parameter dictionaries are equal, False otherwise.
  """
  for key in params1:
    if key in params2:
      if key == 'rate':
        # Use a different tolerance for rate
        if not np.isclose(params1[key], params2[key], atol=rate_tolerance):
          return False
      elif isinstance(params1[key], (int, float)) and isinstance(
          params2[key], (int, float)
      ):
        if not np.isclose(params1[key], params2[key], atol=general_tolerance):
          return False
      else:
        if not np.all(
            np.isclose(params1[key], params2[key], atol=general_tolerance)
        ):
          return False
    else:
      return False
  if debug:
    print(f'params1: {params1}')
    print(f'params2: {params2}')
  return True


# Function to generate random parameters within a specified range
def generate_random_params(params, question_params):
  """Generates random parameters within a specified range.

  Args:
    params: The parameter dictionary.
    question_params: The question parameter dictionaries.

  Returns:
    A dictionary of random parameters.
  """
  while True:
    random_params = {}
    for key, value in params.items():
      if isinstance(value, tuple):
        if key == 'probs':
          random_params[key] = generate_probabilities(
              min_threshold=0.1, num_categories=len(value)
          )
        else:
          generated_value = np.random.uniform(value[0], value[1])
          if isinstance(value[0], int) and isinstance(value[1], int):
            random_params[key] = int(generated_value)
          else:
            random_params[key] = round(generated_value, 3)
      else:
        random_params[key] = value

    # Check if the generated params are not equal to any question params
    equal_params = [
        q_params
        for q_params in question_params
        if params_equal(random_params, q_params)
    ]
    if not equal_params:
      break
    else:
      print(
          'Generated parameters equal to or too similar to existing question'
          f' params: {random_params}. Random param generation will be retried.'
      )

  return random_params


def generate_distributions_and_examples(
    sample_size=100000,
    task=None,
    num_examples=20,
    enable_debug=False,
    fixed_seed=1337,
    enable_approximate_as_normal=False
):
  """Generates distributions and examples for a given task.

  Args:
    sample_size: The sample size for the distribution.
    task: The task for which to generate distributions and examples.
    num_examples: The number of examples to generate for each distribution.
    enable_debug: Whether to print debug information.
    fixed_seed: The fixed seed to use for NumPy functions.
    enable_approximate_as_normal: Whether to approximate the distribution as
      normal.

  Returns:
    A dictionary of distributions and examples.

  Raises:
    ValueError: If the task is not supported.
  """
  # Initialize the dictionary to hold all distributions information
  distributions_info = {}

  if task not in ['percentiles', 'sampling', 'probabilities']:
    raise ValueError(
        f'Unsupported task: {task}. Please pick from percentiles, sampling, or'
        ' probabilities.'
    )

  # General parameters for all distribution functions
  general_params = {'sample_size': sample_size, 'task': task}

  # Collect question parameters for comparison
  question_params_list = [
      config['params'] for config in distribution_questions_config
  ]

  # Process the question distributions
  for config in distribution_questions_config:
    result = config['func'](
        **config['params'],
        **general_params,
        debug=enable_debug,
        seed=fixed_seed,
        approximate_as_normal=enable_approximate_as_normal,
    )

    # Unpack the result based on the number of returned values
    if len(result) == 3:
      description, output, intermediate_output = result
    elif len(result) == 2:
      description, output = result
      intermediate_output = (
          None  # Set intermediate_output to None if not returned
      )
    else:
      raise ValueError('Unexpected number of return values from the function')
    distributions_info[config['name']] = {
        'description': description,
        'examples': [],
    }
    if task == 'percentiles':
      distributions_info[config['name']]['target_percentile_values'] = output
      distributions_info[config['name']][
          'target_intermediate_percentile_values'
      ] = intermediate_output
    elif task == 'sampling':
      distributions_info[config['name']]['samples'] = output
    elif task == 'probabilities':
      distributions_info[config['name']]['target_ranges'] = output
      distributions_info[config['name']][
          'target_intermediate_ranges'
      ] = intermediate_output

  if num_examples != 0:
    # Generate examples for each distribution
    for config in distribution_examples_config:
      examples = []
      for _ in range(num_examples):
        params = generate_random_params(config['params'], question_params_list)

        example_seed = np.random.randint(
            0, 100000
        )  # Different seed for each example

        result = config['func'](
            **params, **general_params, debug=enable_debug, seed=example_seed
        )

        # Unpack the result based on the number of returned values
        description = None
        output = None
        if len(result) == 3:
          description, output, _ = result
        elif len(result) == 2:
          description, output = result

        if task == 'percentiles':
          examples.append({
              'description': description,
              'target_percentile_values': output,
          })
        elif task == 'sampling':
          examples.append({
              'description': description,
              'samples': output,
          })
        elif task == 'probabilities':
          examples.append({
              'description': description,
              'target_ranges': output,
          })

      distributions_info[config['name']]['examples'] = examples

  if enable_debug:
    pprint.pprint(distributions_info)
  return distributions_info
