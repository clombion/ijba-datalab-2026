<!-- chunk: 1/1 | source: 97f-nicar-2021.md | words: 1303 -->
<!-- headings: NICAR 2021 Tipsheets & Session Notes; 2021-causal-inference-dummies.md; 2021-data-unit-guide.md; Data Unit Guide (DUG); Modules; 2021-git-scraping-github-actions.md; Git Scraping: Tracking Changes to a Scraped Data Source Using GitHub Actions; 2021-text-mining-tidy-r.md; Text Mining with Tidy Data Principles -->

# NICAR 2021 Tipsheets & Session Notes


## 2021-causal-inference-dummies.md

Causal Inference for Dummies

Kathy Qian
Co-Founder
Code for Democracy

kathy@codefordemocracy.org
@kathyqian_

NICAR 2021
Hello! I’m Kathy, the Co-Founder of Code for Democracy. Today, I’m going to talk about causal inference, a topic that probably deserves at least an hour, but I’m going to do it in 5 minutes.

Causal inference is the process of determining causality

If we change A, will B change? If yes, then A has a causal relationship with B.


A mantra to remember: “No causation without manipulation.”
Causal inference is the process of determining causality, or whether changes in one thing will lead to changes in another. It’s a term most commonly used in social sciences like economics, but it’s been of increasing interest to machine learning-based data scientists as well. 

The most important thing to remember about causal inference is that the heart of causality is manipulation. You have to change something in order to measure the effect of it. This lack of manipulation is the reason why correlation is not causation.

Good causal inference questions sound like experiments

If you can’t think of an experiment that would help you answer a question, it probably can’t be answered with clever statistics either.


Nearly impossible to answer: 
Did Hillary Clinton receive a lower vote share because she is a woman?

Much easier to answer: 
Does hydroxychloroquine reduce mortality in COVID patients?
If this is starting to bring back memories of 5th grade science, you’re on the right track! Good causal inference questions sound like experiments. In fact, if you can’t think of an experiment that would help you answer a causal question, you probably can’t answer it at all, even if you use a lot of advanced statistics.

For example, it’s nearly impossible to answer some causal questions that pundits are interested in, such as “Did Hillary Clinton receive a lower vote share because she is a woman?” This is because there is only one Hillary Clinton, and there’s basically no way to change the fact that she is a woman while holding all else equal.

Randomized controlled trials (RCTs) are the gold standard for causal inference

In an ideal world, we would design experiments for everything. But often it is too expensive, too time-consuming, or too unethical.
Randomized controlled trials are the gold standard for causal inference. But in the real world, they are often too expensive, too time-consuming, or too unethical.

If you can’t run an experiment, the next best thing is to use a quasi-experimental method

Quasi-experimental methods are used when you have data that has a treatment and control group, but unlike an actual experiment, the treatment and control groups are not assigned randomly.
So the next best thing we can do is to use a quasi-experimental method, which involves creating a treatment and control group from an existing dataset without you having to design and run an experiment yourself. 

These aren’t as great as actual experiments because there’s usually no randomization, which means there’s some inherent differences between the treatment and control groups that you’re going to have to be careful about, but they work well when experimentation is impossible. 

I’m going to talk about 2 common quasi-experimental methods.

QUASI-EXPERIMENTAL METHOD #1
Difference in differences

Difference in differences is useful when there is data from two groups (one treatment and one control) at two points in time (one before the intervention and one after the intervention).

See: Card & Krueger on minimum wage
time
outcome
control
treatment
effect
intervention
The first is the difference in differences approach, which is useful when you have two groups, one which is the treatment and one which is the control, and two points in time, one before the intervention and another after. 

For example, for years, prevailing economic theory predicted that increases in the minimum wage would increase unemployment.

In 1993, two economists named David Card and Alan Krueger decided to test the theory with some data-driven work and used the difference in differences approach to compare employment levels in New Jersey, which raised its minimum wage, to employment levels in nearby areas of Pennsylvania, which did not. They didn’t end up finding the expected increases in unemployment in New Jersey.

QUASI-EXPERIMENTAL METHOD #2
Regression discontinuity design

Regression discontinuity design is useful when a cutoff in a continuous variable splits a population into treatment and control groups.

See: Lee on incumbency advantage
characteristic
outcome
intervention
effect
The second quasi-experimental method I’ll talk about is regression discontinuity design, which is useful when there is a cutoff in some continuous variable that results in very different outcomes for observations near the cutoff, even though all the observations around the cutoff are fairly similar.

For example, electoral districts where the vote share for a party in an election is just under 50% are on average pretty similar to districts where the vote share for that party was just over 50%. But this small change in vote share determines the party affiliation of the district for the next election.

By comparing districts where a party won the previous election with just over 50% of the popular vote with districts where that party lost the previous election with just under 50% of the vote, we can use regression discontinuity design to measure the incumbency advantage.

If you can’t find data to analyze as a quasi-experiment, regressions can help test a causal hypothesis

But if there is no intervention, they cannot prove causality. It doesn’t matter how many variables you “control” for. 


What p-values tell us: If there is no relationship between A and B, then the likelihood of seeing these numbers due to random chance is X%. If X is low, then the data is considered consistent with the hypothesis that there is a relationship between A and B.
Unfortunately, it’s hard to execute good experiments or find interesting datasets for quasi-experimental methods. That means a lot of data-driven work is not that rigorous from a causal inference perspective.

Regressions are often used to illustrate the relationship between 2 variables. But remember, causality can’t be measured without manipulation, so while a regression can help test a causal hypothesis by showing whether data is consistent with it, it can’t on its own prove causality. 

Even when you’re controlling for a lot of variables in a regression, at the end of the day, you’re really just doing a more advanced correlation.

You should be extremely skeptical of drawing conclusions from correlations

Correlation is not causation. You cannot change this fact with big data, machine learning, pretty visualizations, or fancy degrees from fancy schools.


Spurious Correlations: https://tylervigen.com/spurious-correlations
So, in conclusion, causal inference is hard. A lot of people get it wrong. You should be extremely skeptical of drawing conclusions from correlations. And you can’t make up for bad causal inference methods with more data, more code, more graphics, or more credentials.

## 2021-data-unit-guide.md

# Data Unit Guide (DUG)
_Source: https://dug.news_
_Authors: Clayton Aldern, Tatyana Monnay (Caldern LLC / Reynolds Journalism Institute)_

Organizational guide to data journalism for small-to-medium and non-profit newsrooms.

## Modules
1. Getting Started — what is a data unit
2. People — assembling and developing teams
3. Structure — integrating within newsroom hierarchies
4. Tech and Tools — software, platforms, resources
5. Value — demonstrating and quantifying contributions
6. Fundraising — securing sustainable funding

## 2021-git-scraping-github-actions.md

# Git Scraping: Tracking Changes to a Scraped Data Source Using GitHub Actions
_Source: https://www.youtube.com/watch?v=2CjA-03yK8I_
_Author: Simon Willison (NICAR 2021 lightning talk)_

Video presentation on automated data collection methodology using GitHub Actions to track changes over time.

## 2021-text-mining-tidy-r.md

# Text Mining with Tidy Data Principles
_Source: https://juliasilge.shinyapps.io/learntidytext/_
_Author: Julia Silge (2021)_

Interactive Shiny app tutorial for text mining in R using tidytext package.
Note: Content is interactive and cannot be fully scraped; visit the URL directly.
