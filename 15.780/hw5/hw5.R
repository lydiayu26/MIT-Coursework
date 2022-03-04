# 15.780 HW5

anime = read.csv("anime_likes.csv")


# 1) compute means of each show
mean_nar = mean(anime$NarutoShippuden)
mean_nar
mean_one = mean(anime$OnePiece)
mean_one


# 2) estimate means with Thompson Sampling
set.seed(15)
number_arms = ncol(anime)
# Set number of periods
horizon = 300

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
    reward[t] =  anime[t,i]
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

mab_thm = bandit_algo('thompson_sampling')

#' Plot the mean reward estimates at each step for Thompson
plot(1, type='n', xlim = c(1,horizon+1), ylim=c(0,1), 
     xlab = 'Time step', ylab = 'Thompson Sampling Mean Estimate')
lines(mab_thm$arm_means[1,], type='l',lwd=1.5, col='red')
lines(mab_thm$arm_means[2,], type='l',lwd=1.5, col='blue')
legend("topright", lty=c(1,1,1,1), cex=0.8, 
       legend=c("Naruto", "One Piece"), 
       col=c("red", "blue"))


# 3) Plot show watched vs time step
plot(mab_thm$pulled_arm, xlab = 'Time step', ylab = 'Arm chosen', main='Arm chosen by Thompson')


# 4) estimated means at end of horizon
est_mean_nar = mean(mab_thm$arm_means[1, -1])
est_mean_nar
est_mean_one = mean(mab_thm$arm_means[2, -1])
est_mean_one


# 5) fraction of rounds that naruto was watched
# worse show was naruto because its final mean was lower
sum(mab_thm$pulled_arm == 1)
