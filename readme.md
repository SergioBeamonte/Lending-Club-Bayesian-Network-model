# [cite_start]Deconstructing Credit Risk: A Bayesian Network Approach [cite: 1]

[cite_start]This project proposes the use of Bayesian Networks (BNs) as a framework for structural interpretation and model auditing in high-dimensional tabular data, moving beyond the traditional "black-box" predictive paradigm[cite: 19]. [cite_start]The analysis was developed by Sergio Beamonte González for the Artificial Intelligence Department at UPM[cite: 5, 10, 11].



---

## 📊 About the Dataset

* [cite_start]The project uses the Lending Club Loan Default Dataset, which is publicly available on Kaggle[cite: 31].
* [cite_start]It contains historical information about personal loans issued through Lending Club, an online peer-to-peer lending marketplace in the United States[cite: 32].
* [cite_start]The primary target variable for this analysis is the Loan Status, which indicates whether a loan defaults or not[cite: 49, 58].

---

## ⚙️ Methodology

The modeling pipeline includes the following phases:

* [cite_start]**Data Preprocessing**: Initially, 50,000 observations were randomly selected for the analysis[cite: 67].
* [cite_start]**Discretization**: Continuous numerical variables were discretized into 5 groups using a quantile-based strategy to improve parameter estimation robustness and avoid data sparsity[cite: 72, 73].
* [cite_start]**Feature Selection**: A Pearson correlation filter (flagging variables with correlation over 0.85) and a Mutual Information (MI) ranking were applied, reducing the set to 29 variables[cite: 80, 81, 83].
* [cite_start]**Structure Learning**: The best model was identified as the network generated using the Hill Climbing (Search-and-Score) algorithm with the BIC (Bayesian Information Criterion) optimization score[cite: 108].
* [cite_start]**Parameter Estimation**: Maximum Likelihood Estimation (MLE) was used because the substantial number of observations made the smoothing effect of Bayesian priors negligible[cite: 105, 106].

---

## 🔍 Key Findings

* [cite_start]**The "Funnel" Effect of Loan Grade**: Topological analysis identifies a critical information bottleneck where the engineered feature 'Loan Grade' acts as a Markov Blanket for the target variable[cite: 23]. [cite_start]It absorbs the variance of the financial history, rendering raw variables conditionally independent of the outcome[cite: 333].
* [cite_start]**Behavior Trumps Solvency**: A structurally refined model reveals that default risk is structurally determined by loan characteristics (term) and the borrower's recent volatility (such as opening multiple accounts in a short window)[cite: 337]. [cite_start]It is not driven linearly by income or debt-to-income (DTI) ratios[cite: 336].
* [cite_start]**Model Auditing**: Bayesian Networks proved invaluable for interpretability[cite: 339]. [cite_start]They successfully identified data leakage in the dataset (post-default variables) and allowed for the visualization of the causal chain from income to credit limits[cite: 340].