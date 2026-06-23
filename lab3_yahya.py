#Yahya Noorzai, lab 3, Red tiger team

username = "Yahya"
print(len(username)) #7 #yes

username = "Yahya"
print(username[0])    #Y
print(username[4])    #a #it was 1 less

username = "Yahya"
print("Welcome to Loop @Yahya" + username) #yes  #concatenation was easier

username = "Yahya"
print(f"Welcome to Loop @Yahya{username}")

username = "YAHYA"  # username[0]
print("username") #my username will print in Caps #immunable could mean the error cant be broken 
feed = ["cars", "fishing", "health",]
print(len(feed)) #2, and cars will print first
print(feed[0])
feed.append("music")
print(feed)
print(len(feed))#4 #It sits at three because its 0, 1, 2, 3
feed.pop(0)
feed = ["fishing", "health", "music"] #cars got removed, and they ended up in alphabetical order
print(feed) #.pop and .remove

profile = {"username": "Yahya", "fallowers": 200, "verified": "False"} #  profile[0]
print(profile["fallowers"]) #it will print 200. and profile[0] printys nothing
#because the numbers are already their in the values

profile = {"username": "Yahya", "fallowers": 250, "verified": "False", "bio": "hi"} 
print(profile.get("age")) #it might add a new key
#because it tells you their is none their
print(f"@{profile['username']} has {profile['fallowers']} fallowers and {len(feed)} post. Top post: {feed[0]}")
#it will say @Yahya has 250 fallowers and 3 post. top post fishing 
#profile, dictionary, feed, list