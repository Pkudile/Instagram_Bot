from instabot import Bot
bot=Bot()

#Here we are logging in our account.
bot.login(username="specify your username",password="specify password")

#To follow a person please specify username of that person in follow function.
bot.follow("specify username")

#To upload photo on our instagram please specify path of image in a function.
bot.upload_photo("specify path of image here",caption="specify caption here.")

#To unfollow please specify username of that person in unfollow function.
bot.unfollow("specify username")

#To send a message please specify username in list.
bot.send_message("I am Bot.How are you?",["username1","username2"])

#To get list of all followers.
followers=bot.get_user_followers("specify your username")
for followers in followers:
    print(bot.get_user_info(follower))
