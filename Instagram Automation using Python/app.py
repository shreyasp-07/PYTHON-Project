from instabot import Bot

bot = Bot()
bot.login(username="",password="")
bot.follow('wscubetechindia')
bot.upload_photo("--path--",caption="I love Python")
bot.unfollow("wscubetechindia")
bot.send_message("I love Python",["rv_goswami_2","wscubetechindia"])
followers = bot.get_user_followers("insta-id")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("insts-id")
for follower in following:
    print(bot.get_user_info(follower))