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
### Nonstationary Problem
* Commonly Reinforcement Learning problems are nonstationary, meaning that the actual reward for an action can change in the future.
* One solution to this problem is to use a constant step-size parameter ***a*** in the range (0, 1]. This way the most recently obtained reward will be assigned the highest weight, and previous rewards including Q1 will be assigned ***decaying*** weights.
* We use a **weighted average** approach. Sometimes reffered to as ***exponential recency-weighted average***.
#### Convergence guarantees
1. Steps are large enough to overcome any initial conditions or random fluctuations. **Sum of all steps approaches inf**.
2. Eventually the steps become small enough to asure convergence. **Sum of squared steps is strictly smaller than inf**.
* The sample-average method (1/n) satisfies both properties.
* Constant step a fails condition 2.
* Although constant step doesn't guarantee convergence, this approach is desirable in nonstationary environments. Step sizes that meet he 2 conditions often converge very slowly and are seldom used in practice.
### Optimistic initial values
* We can encourage **exploration** by setting initial values Q1 to an ***optimistic value*** (+5 for example)
* This way all actions will be explored, since each initial action will produce a ***disappointing*** result and move on to another action; even in the greedy approach
* This approach however doesn't explore well for **nonstationary** methods beacuse it cannot account for a renewed need for exploration
### Associative Search (Contextual Bandits)
* Many RL problems involve learning the best actions for more than 1 task.
* Example: we are handed several bandit tasks, and asked to learn a general policy for all. This could be viewed as a case of a non-stationary problem, but unless the action-values change slowly over time, the previous approaches we've seen won't work well
* We can try to look at additional features: if given 10 slot machines, look at the machine's color and apply a distinct policy for each color
* Associative search tasks involve both trial-and-error learning to search for the best actions, and **association** of these actions with the **situations** in which the are best
