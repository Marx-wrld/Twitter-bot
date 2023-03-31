import tweepy

api_key = "ENTER API KEY"
api_secret = "ENTER API SECRET KEY"

access_token = "ENTER ACCESS TOKEN"
access_token_secret = "ENTER ACCESS TOKEN SECRET"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
