#' ----------------------------------------------------------------------
#' `15.774/780 Fall 2021`
#' `Recitation 10 - Multi-Armed Bandits`
#' 
#' By the end of this recitation, you should know:
#'     - The four types of MAB algorithms we discussed
#'          - e-Greedy
#'          - Decaying e-Greedy
#'          - UCB
#'          - Thompson Sampling
#'      - How to run them in R
#' ----------------------------------------------------------------------


#' Let's read the dataset containing the rewards of arm-pulls. 
#' reward_pulls[t,i]: reward you would obtain IF you pulled `i` in period `t`
#' 
#' `NOTE`: You would never actually observe all of these. The point of 
#' bandits is that you *only* ever observe the reward arm you pull. 
reward_pulls = read.csv(file="mab_dataset.csv")
View(reward_pulls)

#' Behind the curtain, I can secretly tell you that:
#'    Arm 1 is Bernoulli(0.2) 
#'    Arm 2 is Bernoulli(0.5)
#'    Arm 3 is Bernoulli(0.7) and is thus the true BAE
#' Recall that in Bernoulli(p) we have success 1 with probability *p* and 
#' failure 0 with probability *1-p*.

set.seed(25)


# Set number of arms as per the data
number_arms  = ncol(reward_pulls)
number_arms
# Set number of periods as per the data
horizon = nrow(reward_pulls)
horizon

#' ----------------------------------------------------------------------
#' Algorithm pull functions
#' ----------------------------------------------------------------------
#' First we will define functions for each bandit algorithm, that tell
#' us what arm we should pull next, based on information we've gathered.


# Epsilon-Greedy: 
pull_epsilon_greedy = function(arm_means, eps=0.5){
  
  # Generate random number from [0,1], and explore if it is <= eps
  if (runif(1) < eps){
    pulled_arm = sample(length(arm_means), size=1) 
  } else {
    pulled_arm = which.max(arm_means)
  }
  return(pulled_arm) 
}


# Decaying Epsilon Greedy
pull_dec_epsilon_greedy = function(arm_means, t, eps=0.5){
  # Generate random number from [0,1], and explore if it is <= eps/t
  if (runif(1) < eps / t){
    pulled_arm = sample(length(arm_means), size=1) 
  } else {
    pulled_arm = which.max(arm_means)
  }
  return(pulled_arm) 
}


# UCB
pull_ucb = function(arm_means, num_pulls, t){
  
  # Calculate upper confidence bound (vectorized for each arm)
  uc_bound = arm_means + sqrt(2 * log(t) / num_pulls)
  
  # Pull the arm which has the maximum UCB
  pulled_arm = which.max(uc_bound)
  return(pulled_arm)
}


# Thompson Sampling
pull_thompson = function(alphas, betas){
  # alphas and betas: vectors of len(arms) of num losses/wins for each arm
  
  number_arms = length(alphas)
  
  # Create vector to hold sample of estimated means from beta distributions
  sampled_reward = rep(NA, number_arms) 
  for(i in 1:number_arms){
    # for each arm, generate a random number from its beta dist
    sampled_reward[i] = rbeta(1, alphas[i], betas[i])
  }
  
  # Pick the arm which has the highest sampled mean
  pulled_arm = which.max(sampled_reward)
  return(pulled_arm)
}


#' ----------------------------------------------------------------------
#' Simulation skeleton function
#' ----------------------------------------------------------------------
#' We first write a skeleton function that will run any MAB algorithm.
#' Think of this as a simulation environment. We won't specify how the
#' decision to pull an arm is made (those are functions defined below),
#' we'll just take care of the surrounding book-keeping. 


bandit_algo = function(algo_name){
    
    #' First we initialize all the book-keeping things. Thes are:
    
    #' num_pulls[i]: number of times arm `i` has been pulled
    num_pulls = rep(0, number_arms) 
    num_pulls
    
    #' arm_rewards[i]: total reward obtained so far from arm `i`
    #' how many 1s have a seen so far from each arm
    #' arm_rewards / num_pulls = estimated means
    arm_rewards = rep(0, number_arms) 
    arm_rewards
    
    #' pulled_arm[t]: which arm was pulled at end of period `t`
    #' vector of len(horizon) representing which arm pulled at t
    pulled_arm = rep(NA, horizon) 
    
    #' reward[t]: reward observed at time `t`
    reward = rep(NA, horizon)
    
    #' arm_means[i,t]: best estimate of arm `i`'s mean at start of period `t`.
    #' We use horizon+1 columns because we want to do mean at end of T.
    arm_means =  matrix(0.5, nrow = number_arms, ncol = horizon + 1)
    arm_means[,1:5]
    
    #' alphas[i]/betas[i]: Beta distribution parameters for arm `i` (used for
    #' Thompson sampling). All arms start at a=b=1, and update as we pull.
    alphas = rep(1, number_arms)
    alphas
    
    betas = rep(1, number_arms)
    betas
    
    #' Now we do the simulation. Depending on the *algo_name*, we use some
    #' function called *pull_<algo>* (which we will define after this). All 
    #' of these will just give as an arm `i` to pull, based on our 
    #' book-keeping information.
    
    for(t in 1:horizon){
      
        # Get which arm to pull:
        if (algo_name == 'eps_greedy'){
            i = pull_epsilon_greedy(arm_means[,t], eps=0.5)
            
        } else if (algo_name == 'dec_eps_greedy') {
            i = pull_dec_epsilon_greedy(arm_means[,t], t, eps=0.99)
            
        } else if(algo_name == 'ucb') {
            if (t <= number_arms) { # initialize UCB by pulling each arm once
                i = t
            } else {
                i = pull_ucb(arm_means[,t], num_pulls, t)
            }
          
        } else if (algo_name == 'thompson_sampling') {
            i = pull_thompson(alphas, betas)
        }

      #' And update everything: 
      pulled_arm[t] = i
      head(pulled_arm)
      
      #' Update number of arm pulls
      num_pulls[i] = num_pulls[i] + 1
      num_pulls
      
      #' Get the reward from the dataset:
      reward[t] =  reward_pulls[t,i]
      head(reward)
      
      #' Update total reward for pull arm
      arm_rewards[i] = arm_rewards[i] + reward[t]
      arm_rewards
      
      #' Update alphas/betas (only for pulled arm)
      alphas[i] = alphas[i] + reward[t]   # (i.e. +1 if success, +0 if failure)
      betas[i] = betas[i] + 1 - reward[t] # (i.e. +0 if success, +1 if failure)
      
      alphas
      betas
      
      #' Finally, update mean estimates for next round. 
      #' They are the same for arms not pulled:
      arm_means[,t+1] = arm_means[,t]
      
      # And for the arm we pull, we update it depending on the algo:
        if (algo_name == "thompson_sampling") {
            arm_means[i,t+1] = alphas[i] / (alphas[i] + betas[i])
        } else {
            arm_means[i,t+1] = arm_rewards[i] / num_pulls[i]
        }
    }
    
    arm_means[,1:5]
      
    return(list("arm_means" = arm_means, 
                "pulled_arm" = pulled_arm, 
                "reward" = reward))
}

#' ----------------------------------------------------------------------
#' Run simulations
#' ----------------------------------------------------------------------
set.seed(42)
mab_eg  = bandit_algo('eps_greedy')
mab_deg = bandit_algo('dec_eps_greedy')
mab_ucb = bandit_algo('ucb')
mab_thm = bandit_algo('thompson_sampling')

#' Let's see what these contain:
head(mab_thm$pulled_arm)
head(mab_thm$reward)
mab_thm$arm_means[,1:5]



#' Plot the arm chosen in each round
plot(mab_eg$pulled_arm , xlab = 'Time step', ylab = 'Arm chosen', main='Arm chosen by e-Greedy')
plot(mab_deg$pulled_arm, xlab = 'Time step', ylab = 'Arm chosen', main='Arm chosen by Decaying e-Greedy')
plot(mab_ucb$pulled_arm, xlab = 'Time step', ylab = 'Arm chosen', main='Arm chosen by UCB')
plot(mab_thm$pulled_arm, xlab = 'Time step', ylab = 'Arm chosen', main='Arm chosen by Thompson')


#' Plot the mean reward estimates at each step for Thompson
plot(1, type='n', xlim = c(1,horizon+1), ylim=c(0,1), 
     xlab = 'Time step', ylab = 'Thompson Sampling Mean Estimate')
lines(mab_thm$arm_means[1,], type='l',lwd=1.5, col='red')
lines(mab_thm$arm_means[2,], type='l',lwd=1.5, col='blue')
lines(mab_thm$arm_means[3,], type='l',lwd=1.5, col='green')
legend("topright", lty=c(1,1,1,1), cex=0.8, 
       legend=c("Arm 1", "Arm 2", "Arm 3"), 
       col=c("red", "blue", "green"))


#' Look at Total Reward at end of horizon
sort(c("e-Greedy"          = sum(mab_eg$reward), 
       "Decaying e-Greedy" = sum(mab_deg$reward), 
       "UCB"               = sum(mab_ucb$reward), 
       "Thompson"          = sum(mab_thm$reward)))


#' We can also look at the *empirical* regret!
#' regret[t]: Difference in reward obtained by algo up to `t` compared 
#' to optimal policy (i.e. always pull the best arm, which here is 3)
 
#' Take the cumulative sum of 3's rewards:
opt_reward = cumsum(reward_pulls[,3])

#' And subtract the cumulutive sum of algos's rewards (vectorized over `t`).
regret_eg  = opt_reward - cumsum(mab_eg$reward)
regret_deg = opt_reward - cumsum(mab_deg$reward)
regret_ucb = opt_reward - cumsum(mab_ucb$reward)
regret_thm = opt_reward - cumsum(mab_thm$reward)

#' And now plot the regrets 
plot(1,type='n', xlim=c(1,horizon), ylim=c(0,150),
     xlab = 'Time step',  ylab='Cumulative Regret')
lines(regret_eg,  type='l', lwd=1.5, col='red')
lines(regret_deg, type='l', lwd=1.5, col='blue')
lines(regret_ucb, type='l', lwd=1.5, col='orange')
lines(regret_thm, type='l', lwd=1.5, col='green')
legend("topleft", lty=c(1,1,1,1), cex=0.9, 
       legend=c("e-Greedy", "Decaying e-Greedy", "UCB", "Thompson"),
       col=c("red", "blue", "orange", "green"))



