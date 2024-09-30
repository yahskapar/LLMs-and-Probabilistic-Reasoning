<p align="center">
:fire: Remember to :star: this repo if you find it useful and cite our work if you use in your work! :fire:
</p>
<p align="center">
:fire: If you have any questions or concerns, please create an <a href="https://github.com/yahskapar/LLMs-and-Probabilistic-Reasoning/issues">issue</a> :memo:! :fire:
</p>

# LLMs-and-Probabilistic-Reasoning

This repository contains the data and software artifacts for the EMNLP 2024 (Main) paper ["What Are the Odds? Language Models Are Capable of Probabilistic Reasoning"](https://arxiv.org/abs/2406.12830).

## :notebook: Overview

This repository is organized into several key components:

1. **Generation**:
   - `idealized_generation/`: Contains scripts for generating idealized distributions and prompts.
   - `real_world_generation/`: Scripts for generating distributions and prompts based on real-world data.

2. **Sample Results from Paper**:
   - This folder contains the sample results presented in the paper, organized by experiment type.

3. **Templates**:
   - Contains template code used for generating idealized and real-world distirbutions.

4. **Notebook**:
   - `EMNLP_2024_tutorial.ipynb`: A Jupyter notebook that provides an interactive tutorial on using the provided scripts to generate datasets and load results from the paper (which can be found in `sample_results_from_paper/`.)

## :wrench: Setup and Usage

This section is a work-in-progress. For the time being, please refer to the tutorial notebook (`EMNLP_2024_tutorial.ipynb`).

## :zap: Additional Results

Additional model-wise results are provided below for tables 1 and 2 from the paper.

**Aggregated  zero-shot  task  performanceacross different LMs** (Table 1):

| Model            | Percentiles (%)       | Sampling (K-S)       | Probabilities (%)    |
|------------------|-----------------------|----------------------|----------------------|
| Llama3-70B       | 26.6 ± 3.76            | 0.63 ± 0.07          | 32.5 ± 2.33          |
| GPT3.5-Turbo     | 25.7 ± 3.11            | 0.73 ± 0.07          | 32.7 ± 2.38          |
| **GPT4-Turbo**   | **14.9** ± **2.39**    | **0.59** ± **0.08**  | 21.0 ± 2.11          |
| Gemini 1.0 Ultra | 16.5 ± 2.67            | 0.76 ± 0.09          | **19.4** ± **2.26**  |


**Zero-shot performance by domain and context category across different LMs** (Table 2):

| Model        | Health Idealized   | Health Real World Con. | Health Norm. Approx. | Finance Idealized  | Finance Real World Con. | Finance Norm. Approx. | Climate Idealized  | Climate Real World Con. | Climate Norm. Approx. |
|--------------|--------------------|------------------------|----------------------|--------------------|-------------------------|-----------------------|--------------------|-------------------------|-----------------------|
| Llama3_8B    | 20.50 +/- 5.56      | 19.40 +/- 1.33         | 17.98 +/- 1.02       | 26.05 +/- 1.97     | 20.49 +/- 0.83          | 24.43 +/- 1.70        | 26.94 +/- 2.16     | 15.63 +/- 2.53          | 13.72 +/- 2.10        |
| Llama3_70B   | 14.8 +/- 6.01       | 15.3 +/- 4.03          | 8.61 +/- 1.97        | 23.9 +/- 4.02      | 19.8 +/- 6.56           | 6.24 +/- 0.78         | 23.5 +/- 5.71      | 20.2 +/- 5.29           | 8.87 +/- 0.99         |
| Gemma2 9B    | 16.14 +/- 5.70      | 19.08 +/- 8.07         | 18.97 +/- 7.69       | 27.05 +/- 5.74     | **7.36 +/- 0.73**           | 7.59 +/- 0.99         | 25.09 +/- 4.49     | 7.55 +/- 0.76           | 9.26 +/- 1.41         |
| Gemma2 27B   | 13.28 +/- 5.68      | 5.02 +/- 0.56          | 5.09 +/- 0.51        | 16.08 +/- 6.32     | 7.90 +/- 1.20           | 7.74 +/- 1.16         | **11.84 +/- 0.85**     | **5.82 +/- 1.08**           | 5.10 +/- 1.10         |
| Mistral_8x7B | 15.13 +/- 3.96      | 11.22 +/- 1.64         | 9.64 +/- 1.55        | 21.63 +/- 2.31     | 11.30 +/- 2.63          | 12.28 +/- 4.09        | 26.05 +/- 5.21     | 11.29 +/- 1.94          | 10.90 +/- 1.82        |
| GPT3.5-Turbo | 20.5 +/- 9.62       | 20.3 +/- 8.51          | 6.81 +/- 0.68        | 17.7 +/- 4.54      | 20.4 +/- 2.88           | 7.55 +/- 0.77         | 22.7 +/- 6.88      | 25.7 +/- 6.32           | 7.90 +/- 0.22         |
| GPT4-Turbo   | **11.0 +/- 4.94**       | **4.92 +/- 3.18**          | **3.15 +/- 0.76**        | **8.99 +/- 1.18**      | 10.7 +/- 3.24           | **5.50 +/- 0.48**         | 18.5 +/- 6.53      | 15.2 +/- 5.13           | **4.94 +/- 0.58**         |
| Gemini Pro   | 25.30 +/- 8.41      | 11.51 +/- 1.06         | 10.42 +/- 1.32       | 29.35 +/- 3.72     | 11.77 +/- 0.92          | 10.10 +/- 1.01        | 26.20 +/- 5.44     | 18.67 +/- 2.01          | 16.53 +/- 1.94        |
| Gemini Ultra | 12.8 +/- 4.43       | 10.3 +/- 2.49          | 5.89 +/- 1.09        | 14.0 +/- 4.47      | 10.5 +/- 2.75           | 7.62 +/- 1.06         | 16.9 +/- 3.86      | 10.5 +/- 0.79           | 7.43 +/- 1.11         |


# :scroll: Citation
If you find our [paper](https://arxiv.org/abs/2406.12830) or any codes in this repo useful, please cite our work.

```
@article{paruchuri2024odds,
  title={What Are the Odds? Language Models Are Capable of Probabilistic Reasoning},
  author={Paruchuri, Akshay and Garrison, Jake and Liao, Shun and Hernandez, John and Sunshine, Jacob and Althoff, Tim and Liu, Xin and McDuff, Daniel},
  journal={arXiv preprint arXiv:2406.12830},
  year={2024}
}
```