# Deconstructing Credit Risk: A Bayesian Network Approach [cite: 1]

This project proposes the use of Bayesian Networks (BNs) as a framework for structural interpretation and model auditing in high-dimensional tabular data, moving beyond the traditional "black-box" predictive paradigm. The analysis was developed by Sergio Beamonte González for the Artificial Intelligence Department at UPM.


---

## 📊 About the Dataset

* The project uses the Lending Club Loan Default Dataset, which is publicly available on Kaggle.
* It contains historical information about personal loans issued through Lending Club, an online peer-to-peer lending marketplace in the United States.
* The primary target variable for this analysis is the Loan Status, which indicates whether a loan defaults or not.

---

## ⚙️ Methodology

The modeling pipeline includes the following phases:

* **Data Preprocessing**: Initially, 50,000 observations were randomly selected for the analysis.
* **Discretization**: Continuous numerical variables were discretized into 5 groups using a quantile-based strategy to improve parameter estimation robustness and avoid data sparsity.
* **Feature Selection**: A Pearson correlation filter (flagging variables with correlation over 0.85) and a Mutual Information (MI) ranking were applied, reducing the set to 29 variables.
* **Structure Learning**: The best model was identified as the network generated using the Hill Climbing (Search-and-Score) algorithm with the BIC (Bayesian Information Criterion) optimization score.
* **Parameter Estimation**: Maximum Likelihood Estimation (MLE) was used because the substantial number of observations made the smoothing effect of Bayesian priors negligible.

---

## 🔍 Key Findings

* **The "Funnel" Effect of Loan Grade**: Topological analysis identifies a critical information bottleneck where the engineered feature 'Loan Grade' acts as a Markov Blanket for the target variable. It absorbs the variance of the financial history, rendering raw variables conditionally independent of the outcome.
* **Behavior Trumps Solvency**: A structurally refined model reveals that default risk is structurally determined by loan characteristics (term) and the borrower's recent volatility (such as opening multiple accounts in a short window). It is not driven linearly by income or debt-to-income (DTI) ratios.

* **Model Auditing**: Bayesian Networks proved invaluable for interpretability. They successfully identified data leakage in the dataset (post-default variables) and allowed for the visualization of the causal chain from income to credit limits.
