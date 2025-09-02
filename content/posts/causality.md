---
title: "Causality"
date: 2025-09-02T13:09:03-04:00
draft: false
tags: ['causal analysis']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# When do we use causal analysis?
The gold standard for establishing causal relationships is a controlled experiment.
But, sometimes these experiments are not feasible for two primary reasons:
- The experiment itself is unethical (e.g. giving people cigarettes to see if it causes cancer)
- The experiment is expensive or logistically impossible (e.g. studying the long-term effects of economic policies across entire countries)

When these become the case, we try to establish causality from observational data.

# Why can't we use OLS methods?

While OLS regression is excellent for prediction and identifying correlations, it faces fundamental challenges when we want to make causal claims. The core issue is confounding variables, or factors that influence both our treatment variable and our outcome variable, creating spurious relationships.
OLS assumes that once we control for the variables in our model, the remaining variation in our treatment variable is "as good as random." But this assumption often fails in practice because:

- Omitted variable bias: We can never be sure we've included all relevant confounders in our model
- Simultaneity: Variables might influence each other bidirectionally
- Selection bias: The treatment group might be systematically different from the control group in unobservable ways

OLS tells us about correlations and can make good predictions, but it cannot distinguish between correlation and causation. Causal analysis methods are specifically designed to address these confounding issues and help us isolate the true causal effects.

## Example: Estimating Mile Time

Imagine we are building a linear regression model to predict how fast someone can run a mile.
We collect data on variables such as BMI, VO2-max, income, and body fat. And let's say this model performs reasonably well, and all variables except for income are significant predictors for mile time. We end up with an equation that looks like this:

$$\begin{aligned}
\text{Mile Time} &= 12.5 + 0.18 \cdot \text{BMI} - 0.12 \cdot \text{VO}_2\text{max} + 0.08 \cdot \text{Body Fat}
\end{aligned}$$

The issue then comes down to interpretation. Looking at BMI, we are saying "Each 1-unit increase in BMI adds ~0.18 minutes to our mile time...**holding all other variables constant**".

Hopefully you see the issue now, because how can we expect to increase BMI, without any change to body fat percentage? If the added weight comes from muscle, then our body fat percentage (of our total weight) is lower, but if that weight gain comes from fat, then our body fat percentage increases.

Hence, we see that BMI and body fat percentage are fundamentally linked; they're not independent variables that can be adjusted separately in the real world. The OLS assumption of "holding all other variables constant" breaks down because these variables are mechanically related to each other. This illustrates why causal analysis requires us to think carefully about the underlying data-generating process, rather than the statistical relationships we observe in our sample.



