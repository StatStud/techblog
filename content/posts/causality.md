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

# Background: Why Causal Analysis?

## When do we use causal analysis?
The gold standard for establishing causal relationships is a controlled experiment.
But, sometimes these experiments are not feasible for two primary reasons:
- The experiment itself is unethical (e.g. giving people cigarettes to see if it causes cancer)
- The experiment is expensive or logistically impossible (e.g. studying the long-term effects of economic policies across entire countries)

When these become the case, we try to establish causality from observational data.

## Why can't we use OLS methods?

While OLS regression is excellent for prediction and identifying correlations, it faces fundamental challenges when we want to make causal claims. The core issue is confounding variables, or factors that influence both our treatment variable and our outcome variable, creating spurious relationships.
OLS assumes that once we control for the variables in our model, the remaining variation in our treatment variable is "as good as random." But this assumption often fails in practice because:

- Omitted variable bias: We can never be sure we've included all relevant confounders in our model
- Simultaneity: Variables might influence each other bidirectionally
- Selection bias: The treatment group might be systematically different from the control group in unobservable ways

OLS tells us about correlations and can make good predictions, but it cannot distinguish between correlation and causation. Causal analysis methods are specifically designed to address these confounding issues and help us isolate the true causal effects.

### Example: Estimating Mile Time

Imagine we are building a linear regression model to predict how fast someone can run a mile.
We collect data on variables such as BMI, VO2-max, income, and body fat. And let's say this model performs reasonably well, and all variables except for income are significant predictors for mile time. We end up with an equation that looks like this:

$$\begin{aligned}
\text{Mile Time} &= 12.5 + 0.18 \cdot \text{BMI} - 0.12 \cdot \text{VO}_2\text{max} + 0.08 \cdot \text{Body Fat}
\end{aligned}$$

The issue then comes down to interpretation. Looking at BMI, we are saying "Each 1-unit increase in BMI adds ~0.18 minutes to our mile time...**holding all other variables constant**".

Hopefully you see the issue now, because how can we expect to increase BMI, without any change to body fat percentage? If the added weight comes from muscle, then our body fat percentage (of our total weight) is lower, but if that weight gain comes from fat, then our body fat percentage increases.

Hence, we see that BMI and body fat percentage are fundamentally linked; they're not independent variables that can be adjusted separately in the real world. The OLS assumption of "holding all other variables constant" breaks down because these variables are mechanically related to each other. This illustrates why causal analysis requires us to think carefully about the underlying data-generating process, rather than the statistical relationships we observe in our sample.

# A Deeper Dive into Causal Analysis

For decades, statistics focused primarily on correlation and prediction. The phrase "correlation does not imply causation" was treated almost like a conversation-ender because we simply couldn't make causal claims from observational data. However, this changed dramatically with the work of researchers like Judea Pearl, Donald Rubin, and others who developed formal frameworks for causal reasoning. 

During the 1980s, Pearl was a leading developer of Bayesian networks, which use directed graphs to represent probabilistic relationships. In 2000, he published his landmark book, *Causality: Models, Reasoning, and Inference*, which provided a comprehensive mathematical theory of causation and introduced the do-calculus (the mathematical tool used to compute the effects of interventions in a system). This work was instrumental in formalizing causal inference across many scientific disciplines.

Pearl's "Causal Revolution" gave us mathematical tools to represent causal relationships explicitly and determine when we can identify causal effects from observational data. Rather than avoiding causal questions, we now have principled methods to tackle them head-on.

## Directed Acyclic Graphs (DAGs): 90% of the setup

A Directed Acyclic Graph is a visual representation of the causal relationships between variables. Think of it as a roadmap showing how variables influence each other:
- Nodes represent variables
- Directed arrows represent causal relationships
- Acyclic means no variable can cause itself through a chain of other variables

### Types of Paths in DAGs
Understanding different types of paths is crucial for causal identification. These include:
- Causal paths: Direct routes from treatment to outcome (what we want to measure)
- Confounding paths: Routes that create spurious correlation between treatment and outcome
- Mediating paths: Routes where the treatment affects the outcome through intermediate variables

## Structural Causal Models (SCMs): The Mathematical Foundation

This process is done AFTER we have formalized our DAG. 
Creating the DAG is the most important step in causal analysis.

While DAGs show us the structure of causal relationships, Structural Causal Models (SCMs) give us the mathematical framework. An SCM consists of:
- A set of variables (both observed and unobserved)
- A set of functions describing how each variable is determined
- A probability distribution over the unobserved variables

U₁, U₂, U₃ ~ Some joint distribution (unobserved factors)
Family Background = U₁
Ability = U₂  
Education = f₁(Family Background, Ability, U₃)
Income = f₂(Education, Family Background, Ability, U₄)

This SCM makes explicit how each variable is generated, including the role of unobserved factors (the U terms).

### Interventions in SCMs

The power of SCMs becomes clear when we consider interventions. What happens if we force someone to get a college degree? In SCM language, we "do" an intervention, written as do(Education = College).

When we intervene on Education, we break the causal mechanism that normally determines education level. We replace the equation for Education with our intervention, creating a new "mutilated" model that represents the post-intervention world.


### From Graphs to Equations: Estimating the Structure

Let's formalize our education-income relationship with concrete equations. In the real world, there exists some "ground truth" data-generating process:

**True Structural Equations:**


$$U_1, U_2, U_3, U_4 &\sim \text{Some joint distribution (unobserved factors)} $$
$$\text{Family Background} &= U_1 $$
$$\text{Ability} &= U_2 $$
$$\text{Education} &= \beta_0 + \beta_1 \cdot \text{Family Background} + \beta_2 \cdot \text{Ability} + U_3 $$
$$\text{Income} &= \alpha_0 + \alpha_1 \cdot \text{Education} + \alpha_2 \cdot \text{Family Background} + \alpha_3 \cdot \text{Ability} + U_4$$


Here, $\beta_0, \beta_1, \beta_2, \alpha_0, \alpha_1, \alpha_2, \alpha_3$ represent the **true causal parameters** that govern how variables influence each other in the real world. These are the latent "ground truth" values we're trying to uncover.

#### Estimating the Beta Coefficients

In practice, we don't know these true parameters, so we must estimate them from data. How we do this depends on our assumptions about the functional form:

##### Linear Relationships
If we assume linear relationships, we can estimate each structural equation using OLS regression:

**For Education:**
$\text{Education} = \hat{\beta}_0 + \hat{\beta}_1 \cdot \text{Family Background} + \hat{\beta}_2 \cdot \text{Ability} + \varepsilon_3$

**For Income:**
$\text{Income} = \hat{\alpha}_0 + \hat{\alpha}_1 \cdot \text{Education} + \hat{\alpha}_2 \cdot \text{Family Background} + \hat{\alpha}_3 \cdot \text{Ability} + \varepsilon_4$

The "hat" notation ($\hat{\beta}, \hat{\alpha}$) indicates these are our **estimated** coefficients, which approximate the true values ($\beta, \alpha$). The error terms ($\varepsilon_3, \varepsilon_4$) capture both the unobserved factors ($U_3, U_4$) and any model misspecification.

The linear Estimation Process can be summarized here in 3 points.
1. **Collect data** on Education, Income, Family Background, and Ability
2. **Fit regression models** for each endogenous variable:
   - Regress Education on Family Background and Ability → get $\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2$
   - Regress Income on Education, Family Background, and Ability → get $\hat{\alpha}_0, \hat{\alpha}_1, \hat{\alpha}_2, \hat{\alpha}_3$
3. **Interpret coefficients** as causal parameters (under strong assumptions)

##### Nonlinear Relationships
When relationships aren't linear, we need more flexible estimation approaches:

**Polynomial Models:**
$\text{Education} = \beta_0 + \beta_1 \cdot \text{Family Background} + \beta_2 \cdot \text{Ability} + \beta_3 \cdot (\text{Family Background})^2 + U_3$

**Machine Learning Approaches:**
- **Random Forests**: Can capture complex interactions automatically
- **Neural Networks**: Flexible function approximation
- **Spline Methods**: Piecewise polynomial fits

**Semi-parametric Methods:**
$\text{Income} = \alpha_1 \cdot \text{Education} + g(\text{Family Background}, \text{Ability}) + U_4$
Where $g(\cdot)$ is estimated non-parametrically (e.g., using kernel methods).

### The Gap Between Truth and Estimates

It's crucial to understand that our estimated coefficients $\hat{\beta}_1, \hat{\alpha}_1$, etc., are approximations of the true causal parameters. Several factors create this gap:

#### Finite Sample Error
With infinite data and correct model specification, our estimates would converge to the true values. But with finite samples, we have:
$\hat{\beta}_1 \approx \beta_1 + \text{sampling error}$
$\hat{\alpha}_1 \approx \alpha_1 + \text{sampling error}$

#### Model Misspecification
If the true relationship is nonlinear but we fit a linear model:
$\begin{aligned}
\text{True:} \quad \text{Education} &= \beta_0 + \beta_1 \cdot \text{Family Background} + \beta_2 \cdot (\text{Family Background})^2 + U_3 \\
\text{Estimated:} \quad \text{Education} &= \hat{\beta}_0 + \hat{\beta}_1 \cdot \text{Family Background} + \varepsilon_3
\end{aligned}$
Then $\hat{\beta}_1$ will be a biased estimate of the true marginal effect.

#### Measurement Error
If our variables are measured with error:
$\text{Observed Education} = \text{True Education} + \text{measurement error}$
This can bias our coefficient estimates.

### A Concrete Example: Estimating Education Returns

Suppose we want to estimate how much an additional year of education increases income ($\alpha_1$). Our SCM might be:

**True Model:**
$\text{Income} = 25000 + 3500 \cdot \text{Education} + 500 \cdot \text{Family Background} + 2000 \cdot \text{Ability} + U_4$

**Our Estimation:**
1. Collect data on 10,000 individuals
2. Fit regression: `lm(Income ~ Education + Family.Background + Ability)`
3. Get results: $\hat{\alpha}_1 = 3,485$ (standard error = 45)

**Interpretation:** Our estimate suggests each additional year of education increases income by $3,485, which is close to the true value of $3,500. The standard error tells us the precision of our estimate.

### Why This Matters for Causal Inference

The SCM framework makes explicit that:
1. **Each equation represents a causal mechanism** - not just a statistical association
2. **The coefficients have causal interpretations** - $\hat{\alpha}_1$ estimates the causal effect of education on income
3. **We can simulate interventions** - what happens if we force Education = 16 for everyone?

However, obtaining causal estimates requires strong assumptions:
- **No omitted confounders** - we've included all relevant variables
- **Correct functional form** - our linear (or nonlinear) specification is accurate  
- **No simultaneity** - Education doesn't depend on Income in our model

When these assumptions hold, our estimated structural equations give us the causal parameters we seek. When they don't, we need more sophisticated identification strategies.
