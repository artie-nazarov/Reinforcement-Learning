import numpy as np

class Bandit:
    '''
    Bandit
    The rewards are sampled with a Normal Distribution
    For each action k, the ND is centered on a random value within a given range
    k - number of "bandit hands"
    mean - the mean value of the normal distribution (default: 0)
    var - the variance value of the normal distribution (default: 1)
    r - a value that defined a range of values where the reward can be placed [-r, r] (default: 3)
    '''
    def __init__(self, k=10, mean=0, var=1, r=3):
        self.k = k
        self.k_means = [0 for _ in range(k)]    # true reward values for each action
        self.k_rewards = [0 for _ in range(k)]  # predicted reward values for each action
        self.k_steps = [0 for _ in range(k)]    # number of times each action was taken
        self.optimal_actions = 0
        self.reward_at_step = []
        self.optimal_actions_at_step = []
        self.actions_taken = {key:0 for key in range(k)}
        self.mean = mean
        self.var = var
        self.r = r
        self.init_epsilon = 1e-5
        # Center distributions for each action
        for i in range(k):
            self.k_means[i] = np.random.uniform(-self.r, self.r)
        # Initialize rewards to very small values [0, e]
        for i in range(k):
            self.k_rewards[i] = np.random.uniform(0,self.init_epsilon)

    ''' 
    The K-Bandit function
    Return a reward given an action (index [0, k))
    '''
    def bandit(self, a):
        sample = np.random.normal(self.mean, self.var) + self.k_means[a]
        return sample

    '''
    Simulate K-Bandit for n timeteps
    exploration_prob - probability of taking a random action at each timestep (default: 1/greedy aproach)
    '''
    def simulation(self, n=100, exploration_prob=0):
        for i in range(n):
            # Exploration Step
            if np.random.uniform() > 1-exploration_prob:
                a = np.random.choice(np.arange(self.k))
            # Exploitation Step
            else: 
                a = np.argmax(self.k_rewards)
            # Take an action with the highest predicted reward
            self.k_steps[a] += 1
            R = self.bandit(a)
            Q = self.k_rewards[a]
            N = self.k_steps[a]
            # Action-value method (incremental)
            self.k_rewards[a] += (1/N) * (R - Q)
            self.reward_at_step.append(R)
            self.actions_taken[a] += 1
            # Check if an optimal value has been chosen
            if a == np.argmax(self.k_means):
                self.optimal_actions += 1
            self.optimal_actions_at_step.append(self.optimal_actions / sum(self.k_steps))

    def get_rewards(self):
        return np.array(self.reward_at_step)

    def get_actions(self):
        return np.array(self.optimal_actions_at_step)

    def get_action_distribution(self):
        return self.actions_taken

