---
title: "Bayesian Statistics the Fun Way"
date: 2023-07-02T18:41:23-04:00
draft: false
tags: []
ShowToc: true
cover:
    image: bayesian-stats.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# Part 1: Introduction to Probability

## Chapter 1: Bayesian thinking and everyday reasoning

The central theme of this chapter: **Data informs beliefs; belief should not inform data**
Let's consider two world views in regard to data:
- (Ideal framework): "the probability of data given my hypothesis and experience in the world" or "how well do my beliefs explain the world?"
- (not ideal): "the probability of my beliefs given the data and my experience in the world" or  "how well what I observe supports what I believe"

The first case is where we change our beliefs according ot he data

The second case gathers data (cherry picking) to support our existing belief

> Bayesian thinking is about changing your mind and updating how you understand the world until your new beliefs align with the data.

## Chapter 2: Measuring uncertainty of binary outcomes

You can calculate the odds that your hypothesis is more probable than your counterpart's hypothesis by waging bets and calculating the ratio between the two. This assumes:
1. The outcome is binary
2. The probabilities are uncertain, so we proxy the probabilities by our confidence in how much we're willing to bet.

## Chapter 3: The logic of uncertainty

In this chapter, we review the product rule and sum rule for independent and mutually excuse events.

To recap:
- Independent: the outcome of one event does not impact the outcome of the next event
- Mutually exclusive: An event cannot happen at the same time as another event

- (independent and mutually exclusive): rolling a 6 is mutually exclusive and independent of rolling a 2
- (independent but not mutually exclusive): a basketball game being canceled because the coach is sick is independent of the game being canceled due to weather; but the coach being sick and rain occurring are not mutually exclusive
- (dependent and mutually exclusive): weather forecast between a sunny day and a rainy day; if it's raining, then the probability of it being sunny is affected. Furthermore, it cannot rain at the same time we have clear skies, so the two events are mutually exclusive
- (dependent and not mutually exclusive): "rolling an even number" and "rolling a number greater than 4."

## Chapter 4: Creating a binomial probability distribution

A review of when to use binomial formula:
- Binary outcome
- Fixed number of trials
- Constant probability of success throughout the trials
- Independence between trials

If these conditions are met, then we may use the binomial formula to answer questions like:
- What is the probability of getting **exactly** k successes?
- What is the probability of getting **at least** k successes?
- What is the probability of getting **at most** k successes?
- What is the probability of getting **between** x and y successes (inclusive)?
- What is the probability of getting **no successes**?


The formula for binomial probability is:

P(X = k) = C(n, k) * p^k * q^(n-k)

Where:

- P(X = k) is the probability of getting exactly k successes.
- n is the total number of trials.
- k is the desired number of successes.
- p is the probability of success on a single trial.
- q is the probability of failure on a single trial (q = 1 - p).
- C(n, k) represents the binomial coefficient, which is calculated as n! / (k! * (n - k)!)

## The Beta Distribution

> In real life we are almost never sure what the exact probability of any event is; instead, we just have observations and data.

This is the statement that separates statistics from probability.

In probability, we know exactly how probable events are. In statistics, we look at the problem in reverse, and the task of figuring out probabilities given data is called *inference*. 