#' ----------------------------------------------------------------------

#' `15.774/780 Fall 2021`
#' `Recitation 9 - Recommender Systems`
#' 
#' By the end of this recitation, you should know:
#'     - How to work with user-item datasets
#'     - Calculate and use similarity between users and items
#'     - Make new recommendations of items for users based on similar users! 
#'       (and same for items XD ) 
#' ----------------------------------------------------------------------

#' Dataset
#' ----------------------------------------------------------------------
#' download and load the `lastfm-matrix-germany.csv` file.
#' This data set contains information about *users*, their gender, their age,
#' and *which artists they like*. 
#' The entire data set available online is huge, so we will only be using
#' artists in Germany, and only considering the artists (i.e. ignoring ages, genders, etc.)
#' 
data_germany = read.csv("lastfm-matrix-germany.csv")
nrow(data_germany) #' how many users
ncol(data_germany) #' how many artists

artists = colnames(data_germany)[-1] 
users = data_germany$user

#' create a matrix of reviews
#' all rows, all columns except the first column
reviews = as.matrix(data_germany[, -1])
rownames(reviews) = users


#' User-Based Collaborative Filtering
#' ----------------------------------------------------------------------
#' Let's remove users with no reviews
reviews_per_user = apply(reviews, 1, sum) #' 1 here means sum across rows
users_w_reviews = reviews[reviews_per_user > 0, ] # filter those with no reviews
length(reviews) - length(users_w_reviews) #' how many did we eliminate?

#' let's calculate user similarity matrix (extending the idea of similarity
#' between two vectors to a matrix of vectors)

normalize = function(x) {
  unit_x = x / (sqrt(sum(x^2)))
  return(unit_x)
}
#' normalize across users
normed_reviews = t(apply(users_w_reviews, 1,
                         normalize))

#' matrix dot product
user_simils = normed_reviews %*% t(normed_reviews)

#' Check: does it make sense?
artists[as.logical(reviews["19227", ])]  #' What has 19277 listened to?
tail(sort(user_simils["19227", ]), 10) #' Who is similar to user 19277? -> *user 17101*
artists[as.logical(reviews["17101", ])]  #' What has 17101 listened to?


#' Making recommendations based on user similarities
#' ----------------------------------------------------------------------
#' for *each artist* `a` and *user* `u`, take a weighted sum of listens to
#' that artist by other users -- weighted by cosine similarity:
user_based_recs = user_simils %*% users_w_reviews

#' let's pick our guy user 19227
user_id = "19227"
has_listened = as.logical(reviews[user_id, ]) #' sift through what they listen to
artists[has_listened]  # Which artists has the user already listened to?
#' What are we recommending to user 19277? `Prescriptive--taking an action!`
tail(sort(user_based_recs["19227", !has_listened]), 20) 

#' Does this make sense? Let's see
#' user 17101 is ~similar to user 19227, we'd expect ~similar recommendations
user_id = "17101"
has_listened = as.logical(reviews[user_id, ])
artists[has_listened]  #' Which artists has the user already listened to?
tail(sort(user_based_recs["17101", !has_listened]), 20) # What are we recommending to user 17101?

#' We'd pick linkin park as the first recommendation for both users! (as well as
#' other similar recommendations such as rihanna, nightwish, coldplay, etc. 
#' `GOOD CHOICES OVERALL`)


#' User-Based Collaborative Filtering
#' ----------------------------------------------------------------------
#' #' normalize across users
normed_reviews = apply(reviews, 2, normalize)
#' matrix dot product - note the transpose is in a different spot
item_simils = t(normed_reviews) %*% normed_reviews

#' Check: who's most similar to your favorite artist?

head(sort(item_simils["trivium", ], decreasing=TRUE)) #' a metal band - are metal bands produced??

head(sort(item_simils["rihanna", ], decreasing=TRUE))

head(sort(item_simils["air", ], decreasing=TRUE))

#' Making recommendations based on user similarities
#' ----------------------------------------------------------------------
#' For a *given user* `u` and *artist* `a`, we can see how many similar artists
#'`u` has listened to in the past, weight them by how similar they are to `a`,
#' and sum them up.
item_based_recs = reviews %*% item_simils 

#' Check to see if it makes sense:
user_id = "141"
has_listened = as.logical(reviews[user_id, ])
artists[has_listened]  #' Which artists has the user already listened to?
tail(sort(item_based_recs[user_id, !has_listened]), 20) #' Which are we recommending to user 75?
#' metal stuff XD 
