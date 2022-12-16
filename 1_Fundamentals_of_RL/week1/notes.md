# Fundamentals of Reinforcement Learning
## Week 1
* Readings: Chapter 2-2.7 (Pages 25-36)
### K-armed bandit
* Given a k-armed machine, how do we maximize reward collected over a sequence of actions
* Exploitation - taking the ***greedy*** value
* Exploration - taking a ***non-greedy*** action. Exploring long-term reward improvement
### Action-value Methods
Methods for estimating values of actions (expected/mean reward) and using estimates to make actions.
**Sample-average = sum of rewards when a taken prior to t / number of times a taken prior to t**
### E-greedy method
Uniformly select an action with small probability E (epsilon)
### Efficient estimate of next Action Value
NewEstimate <- OldEstimate + StepSize [Target - OldEstimate]
