# -*- Mode: python -*-
# A random recommender
#
#
# This is a medical scenario with historical data. 
#
# General functions
#
# - set_reward
# 
# There is a set of functions for dealing with historical data:
#
# - fit_data
# - fit_treatment_outcome
# - estimate_utiltiy
#
# There is a set of functions for online decision making
#
# - predict_proba
# - recommend
# - observe


class RandomRecommender:

    #################################
    # Initialise
    #

    def __init__(self, feature_model=None, prediction_model=None):
        self.feature_model = feature_model
        self.prediction_model = prediction_model
        self.reward = self._default_reward

    ## By default, the reward is just equal to the outcome, as the actions play no role
    def _default_reward(self, action, outcome):
        return outcome
    
    ##################################
    # Fit a model from patient data.
    #
    # This will generally speaking be an
    # unsupervised model. Anything from a Gaussian mixture model to a
    # neural network is a valid choice.  However, you can give special
    # meaning to different parts of the data, and use a supervised
    # model instead.
    def fit_data(self, data):
        return None

    # Set the reward function r(a, y)
    def set_reward(self, reward):
        self.reward = reward
        
    ## Fit a model from patient data, actions and their effects
    ## Here we assume that the outcome is a direct function of data and actions
    def fit_treatment_outcome(self, data, actions, outcome):
        return None

    ## Estimate the utility from historical data.
    ## If the policy is None, return use the historical policy
    def estimate_utility(self, data, actions, outcome, policy=None):
        return None

    # Return a distribution of effects for a given person's data and a specific treatment
    def predict_proba(self, data, treatment):
        return None
    
    # Return recommendations for a specific user data
    def recommend(self, user):
        return None

    # Observe the effect of an action
    def observe(self, user, action, reward):
        return None

