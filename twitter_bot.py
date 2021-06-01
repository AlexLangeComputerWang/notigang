import tweepy
from time import sleep
#Authentication into tweepy
auth = tweepy.OAuthHandler('ENV VARIABLE')
auth.set_access_token('ENV VARIABLE 2')
api = tweepy.API(auth)

#Verify Credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error During Authentication.")


#Open up list of people to notify, split into content
noti_people = open("peopletonoti.txt", "r", encoding="utf8")
content = noti_people.read().split()
completed = open("peoplenotified.txt", "r", encoding = "utf8")
content2 = completed.read().split()
#Infinite loop code
while True:
    public_tweets = api.home_timeline(count=20)
    #Loop through each public tweet
    for tweet in reversed(public_tweets):
        #Create an ID for the current tweet we are grabbing.
        newID = tweet.id
        print (tweet.user.screen_name)
        if((tweet.user.screen_name in content) and (tweet.id not in content2)):
            #Reply to each tweet with 'Noti, update mostRecentReply'
            handle = tweet.user.screen_name
            api.update_status('@' + str(handle) + ' Noti', tweet.id)
            print("Responded to User")
            #Write Tweet ID to peoplenotified.txt, and add tweet id to content2
            content2.append(tweet.id)
            with open('peoplenotified.txt', 'a') as the_file:
                the_file.write(str(tweet.id) +'\n')

    sleep(120)
#The logic is we will get the most recent tweet on our timeline constantly.
#If any of those tweets are ever by someone in the notifications textfile,
#AND we haven't already replied to it (that's what mostRecentReply is for),
#Then we reply noti.

#We run the reversed timeline grab because the IDs should only go upwards when
# tweeting? must confirm
