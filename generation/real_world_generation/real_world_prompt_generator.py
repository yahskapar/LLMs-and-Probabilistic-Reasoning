
"""General library for real-world prompt generation.


"""


from templates.real_world_distributions import (
    idealized_real_world,
    real_world,
    real_world_normal_approx
)

health_gt_dict = {
    'Average Step Count': {
        'target_percentile_values': {
            1.0: 2174.61,
            10.0: 4433.794,
            20.0: 5558.104,
            30.0: 6445.293,
            40.0: 7244.214,
            50.0: 8028.321,
            60.0: 8845.736,
            70.0: 9791.713,
            80.0: 11000.567,
            90.0: 12792.197,
            99.0: 17510.718
        },
        'target_ranges': {
            0.102: (7635.28, 8418.632),
            0.204: (7258.529, 8827.968),
            0.306: (6867.371, 9267.069),
            0.408: (6475.844, 9750.122),
            0.51: (6049.556, 10295.755),
            0.612: (5615.236, 10912.331),
            0.714: (5121.244, 11654.698),
            0.816: (4540.99, 12599.002),
            0.918: (3762.946, 14040.506),
            1.0: (2174.624, 17510.715)
        }
    },
    'Average Resting Heart Rate': {
        'target_percentile_values': {
            1.0: 52.286,
            10.0: 57.838,
            20.0: 60.905,
            30.0: 63.324,
            40.0: 65.49,
            50.0: 67.552,
            60.0: 69.692,
            70.0: 71.971,
            80.0: 74.651,
            90.0: 78.33,
            99.0: 85.438
        },
        'target_ranges': {
            0.102: (66.533, 68.593),
            0.204: (65.529, 69.652),
            0.306: (64.483, 70.719),
            0.408: (63.411, 71.87),
            0.51: (62.275, 73.109),
            0.612: (61.06, 74.471),
            0.714: (59.7, 76.052),
            0.816: (58.127, 77.973),
            0.918: (56.125, 80.6),
            1.0: (52.286, 85.437)
        }
    },
    'Average Sleep Minutes': {
        'target_percentile_values': {
            1.0: 280.833,
            10.0: 331.325,
            20.0: 354.023,
            30.0: 369.714,
            40.0: 382.807,
            50.0: 394.37,
            60.0: 405.83,
            70.0: 417.892,
            80.0: 431.841,
            90.0: 450.636,
            99.0: 493.97
        },
        'target_ranges': {
            0.102: (388.837, 399.956),
            0.204: (383.053, 405.594),
            0.306: (376.862, 411.435),
            0.408: (370.266, 417.4),
            0.51: (363.193, 423.8),
            0.612: (355.048, 430.84),
            0.714: (345.566, 439.116),
            0.816: (333.671, 448.76),
            0.918: (316.5, 462.952),
            1.0: (280.833, 493.97)
        }
    },
    'Average AZM Count': {
        'target_percentile_values': {
            1.0: 7.286,
            10.0: 13.788,
            20.0: 19.158,
            30.0: 24.212,
            40.0: 29.466,
            50.0: 35.226,
            60.0: 42.0,
            70.0: 50.431,
            80.0: 62.089,
            90.0: 82.821,
            99.0: 153.72
        },
        'target_ranges': {
            0.102: (32.327, 38.413),
            0.204: (29.563, 41.859),
            0.306: (27.005, 45.641),
            0.408: (24.434, 50.072),
            0.51: (21.923, 55.143),
            0.612: (19.473, 61.21),
            0.714: (16.934, 69.305),
            0.816: (14.239, 80.5),
            0.918: (11.343, 98.569),
            1.0: (7.286, 153.72)
        }
    }
}

finance_gt_dict = {
    'Monthly Gross Rent': {
        'target_percentile_values': {
            1.0: 331.0,
            10.0: 666.0,
            20.0: 813.0,
            30.0: 937.0,
            40.0: 1055.0,
            50.0: 1187.0,
            60.0: 1355.0,
            70.0: 1548.0,
            80.0: 1800.0,
            90.0: 2235.0,
            99.0: 3635.0
        },
        'target_ranges': {
            0.103: (1118.0, 1263.0),
            0.205: (1058.0, 1350.0),
            0.308: (1000.0, 1440.0),
            0.408: (942.0, 1539.0),
            0.511: (882.0, 1650.0),
            0.614: (820.0, 1782.0),
            0.715: (755.0, 1950.0),
            0.818: (680.0, 2189.0),
            0.918: (580.0, 2597.0),
            1.0: (331.0, 3635.0)
        }
    },
    'Annual Electricity Cost': {
        'target_percentile_values': {
            1.0: 360.0,
            10.0: 720.0,
            20.0: 960.0,
            30.0: 1200.0,
            40.0: 1320.0,
            50.0: 1560.0,
            60.0: 1800.0,
            70.0: 2160.0,
            80.0: 2520.0,
            90.0: 3240.0,
            99.0: 4800.0
        },
        'target_ranges': {
            0.21: (1440.0, 1800.0),
            0.244: (1320.0, 1800.0),
            0.387: (1200.0, 2040.0),
            0.425: (1200.0, 2160.0),
            0.562: (1080.0, 2400.0),
            0.634: (960.0, 2520.0),
            0.725: (840.0, 2880.0),
            0.816: (720.0, 3240.0),
            0.908: (600.0, 3600.0),
            1.0: (360.0, 4800.0)
        }
    },
    'Annual Water Cost': {
        'target_percentile_values': {
            1.0: 20.0,
            10.0: 50.0,
            20.0: 90.0,
            30.0: 180.0,
            40.0: 360.0,
            50.0: 480.0,
            60.0: 600.0,
            70.0: 780.0,
            80.0: 1000.0,
            90.0: 1200.0,
            99.0: 2400.0
        },
        'target_ranges': {
            0.103: (420.0, 580.0),
            0.22: (360.0, 600.0),
            0.307: (270.0, 700.0),
            0.409: (190.0, 780.0),
            0.518: (120.0, 870.0),
            0.606: (100.0, 980.0),
            0.721: (70.0, 1100.0),
            0.848: (50.0, 1200.0),
            0.923: (40.0, 1500.0),
            1.0: (20.0, 2400.0)
        }
    },
    'Annual Household Income': {
        'target_percentile_values': {
            1.0: 0.0,
            10.0: 14400.0,
            20.0: 24500.0,
            30.0: 33600.0,
            40.0: 42900.0,
            50.0: 52800.0,
            60.0: 64800.0,
            70.0: 79000.0,
            80.0: 99000.0,
            90.0: 132400.0,
            99.0: 267000.0
        },
        'target_ranges': {
            0.103: (47400.0, 58000.0),
            0.205: (42200.0, 64000.0),
            0.307: (38000.0, 70000.0),
            0.405: (33200.0, 77700.0),
            0.507: (29000.0, 86000.0),
            0.606: (24200.0, 96900.0),
            0.711: (19600.0, 110000.0),
            0.808: (14400.0, 128600.0),
            0.91: (8600.0, 160000.0),
            1.0: (0.0, 267000.0)
        }
    }
}


climate_gt_dict = {
    'Average Temperature': {
        'target_percentile_values': {
            1.0: -21.7,
            10.0: -6.4,
            20.0: -0.4,
            30.0: 3.8,
            40.0: 8.0,
            50.0: 11.8,
            60.0: 15.3,
            70.0: 18.9,
            80.0: 22.8,
            90.0: 26.8,
            99.0: 30.9
        },
        'target_ranges': {
            0.106: (10.0, 13.6),
            0.208: (8.1, 15.3),
            0.308: (6.1, 17.0),
            0.411: (4.0, 18.8),
            0.511: (1.9, 20.6),
            0.613: (-0.1, 22.6),
            0.715: (-2.5, 24.7),
            0.818: (-5.7, 26.6),
            0.921: (-10.7, 28.2),
            1.0: (-21.7, 30.9)
        }
    },
    'Annual Precipitation': {
        'target_percentile_values': {
            1.0: 17.8,
            10.0: 178.47,
            20.0: 293.6,
            30.0: 402.2,
            40.0: 517.8,
            50.0: 647.5,
            60.0: 802.2,
            70.0: 975.6,
            80.0: 1216.46,
            90.0: 1526.86,
            99.0: 2025.849
        },
        'target_ranges': {
            0.102: (582.23, 717.57),
            0.204: (520.46, 799.1),
            0.306: (462.9, 884.01),
            0.408: (406.6, 968.46),
            0.51: (352.15, 1071.75),
            0.612: (299.6, 1199.22),
            0.714: (247.6, 1341.98),
            0.816: (188.44, 1497.18),
            0.918: (114.3, 1675.48),
            1.0: (17.8, 2025.6)
        }
    },
    'Average Wind Speed': {
        'target_percentile_values': {
            1.0: 0.5,
            10.0: 1.3,
            20.0: 1.8,
            30.0: 2.2,
            40.0: 2.6,
            50.0: 3.0,
            60.0: 3.5,
            70.0: 4.0,
            80.0: 4.7,
            90.0: 5.7,
            99.0: 8.2
        },
        'target_ranges': {
            0.122: (2.8, 3.2),
            0.251: (2.6, 3.5),
            0.314: (2.5, 3.7),
            0.45: (2.2, 4.0),
            0.526: (2.1, 4.3),
            0.627: (1.8, 4.6),
            0.739: (1.6, 5.1),
            0.837: (1.3, 5.6),
            0.923: (1.0, 6.4),
            1.0: (0.5, 8.2)
        }
    },
    'Average Relative Humidity': {
        'target_percentile_values': {
            1.0: 23.0,
            10.0: 45.0,
            20.0: 55.0,
            30.0: 62.0,
            40.0: 67.0,
            50.0: 71.0,
            60.0: 75.0,
            70.0: 79.0,
            80.0: 83.0,
            90.0: 88.0,
            99.0: 96.0
        },
        'target_ranges': {
            0.127: (69.0, 73.0),
            0.227: (67.0, 75.0),
            0.322: (65.0, 77.0),
            0.432: (62.0, 79.0),
            0.532: (59.0, 81.0),
            0.623: (56.0, 83.0),
            0.725: (51.0, 85.0),
            0.827: (46.0, 88.0),
            0.921: (38.0, 91.0),
            1.0: (23.0, 96.0)
        }
    }
}


# Function to generate the prompts
def generate_real_world_percentiles_prompts(sample_count=10):
  """Generates prompts for the percentiles task.

  Args:
      sample_count: The number of times to repeat each prompt.

  Returns:
      prompts: A dictionary of prompts grouped by sample count.
  """
  prompts = {}

  idealized_template_mapping = {
      'Average Step Count': idealized_real_world.idealized_avg_step_count_percentile_prompt,
      'Average Resting Heart Rate': idealized_real_world.idealized_avg_resting_heart_rate_prompt,
      'Average Sleep Minutes': idealized_real_world.idealized_avg_sleep_minutes_prompt,
      'Average AZM Count': idealized_real_world.idealized_avg_activity_zone_minutes_prompt,
      'Annual Household Income': (
          idealized_real_world.idealized_annual_household_income_percentile_prompt
      ),
      'Monthly Gross Rent': idealized_real_world.idealized_monthly_rentgrs_percentile_prompt,
      'Annual Electricity Cost': idealized_real_world.idealized_annual_costelec_percentile_prompt,
      'Annual Water Cost': idealized_real_world.idealized_annual_costwatr_percentile_prompt,
      'Average Temperature': idealized_real_world.idealized_average_temperature_percentile_prompt,
      'Annual Precipitation': idealized_real_world.idealized_annual_precipitation_percentile_prompt,
      'Average Wind Speed': idealized_real_world.idealized_average_wind_speed_percentile_prompt,
      'Average Relative Humidity': (
          idealized_real_world.idealized_average_relative_humidity_percentile_prompt
      ),
  }

  real_world_template_mapping = {
      'Average Step Count': real_world.avg_step_count_percentile_prompt,
      'Average Resting Heart Rate': real_world.avg_resting_heart_rate_prompt,
      'Average Sleep Minutes': real_world.avg_sleep_minutes_prompt,
      'Average AZM Count': real_world.avg_activity_zone_minutes_prompt,
      'Annual Household Income': (
          real_world.annual_household_income_percentile_prompt
      ),
      'Monthly Gross Rent': real_world.monthly_rentgrs_percentile_prompt,
      'Annual Electricity Cost': real_world.annual_costelec_percentile_prompt,
      'Annual Water Cost': real_world.annual_costwatr_percentile_prompt,
      'Average Temperature': real_world.average_temperature_percentile_prompt,
      'Annual Precipitation': real_world.annual_precipitation_percentile_prompt,
      'Average Wind Speed': real_world.average_wind_speed_percentile_prompt,
      'Average Relative Humidity': (
          real_world.average_relative_humidity_percentile_prompt
      ),
  }

  real_world_normal_approx_template_mapping = {
      'Average Step Count': real_world_normal_approx.avg_step_count_percentile_prompt,
      'Average Resting Heart Rate': real_world_normal_approx.avg_resting_heart_rate_prompt,
      'Average Sleep Minutes': real_world_normal_approx.avg_sleep_minutes_prompt,
      'Average AZM Count': real_world_normal_approx.avg_activity_zone_minutes_prompt,
      'Annual Household Income': (
          real_world_normal_approx.annual_household_income_percentile_prompt
      ),
      'Monthly Gross Rent': real_world_normal_approx.monthly_rentgrs_percentile_prompt,
      'Annual Electricity Cost': real_world_normal_approx.annual_costelec_percentile_prompt,
      'Annual Water Cost': real_world_normal_approx.annual_costwatr_percentile_prompt,
      'Average Temperature': real_world_normal_approx.average_temperature_percentile_prompt,
      'Annual Precipitation': real_world_normal_approx.annual_precipitation_percentile_prompt,
      'Average Wind Speed': real_world_normal_approx.average_wind_speed_percentile_prompt,
      'Average Relative Humidity': (
          real_world_normal_approx.average_relative_humidity_percentile_prompt
      ),
  }

  template_mappings = {
      'idealized': idealized_template_mapping,
      'real_world': real_world_template_mapping,
      'real_world_normal_approx': real_world_normal_approx_template_mapping
  }

  for gt_dict in [health_gt_dict, finance_gt_dict, climate_gt_dict]:
    for dist_name, dist_info in gt_dict.items():
      target_percentile_values = dist_info.get('target_percentile_values', {})
      for template_name, template in template_mappings.items():
        master_template = template[dist_name]
        for target_number in target_percentile_values.values():
          prompt = master_template.format(target_number=target_number)
          prompt_name = (
              f'percentiles_zero_shot_{template_name}_{dist_name.replace(" ", "_").lower()}'
              + f'_{sample_count}_samples'
          )
          if prompt_name not in prompts:
            prompts[prompt_name] = []
          # Repeat prompt based on SAMPLE_COUNT
          prompts[prompt_name].extend([prompt] * sample_count)

  return prompts
