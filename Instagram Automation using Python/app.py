from instabot import Bot

bot = Bot()
# bot.login(username="wtf_jammess",password="")
# bot.follow('wscubetechindia')
# bot.upload_photo("--path--",caption="I love Python")
# bot.unfollow("wscubetechindia")
# bot.send_message("I love Python",["rv_goswami_2","wscubetechindia"])
followers = bot.get_user_followers("luvely.mikaa")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("luvely.mikaa")
for follower in following:
    print(bot.get_user_info(follower))