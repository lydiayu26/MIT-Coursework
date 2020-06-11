#######################################
## EXAMPLE: getting grades using lists, do NOT do it this way...
#######################################
#def get_grade_list(student, name_list, grade_list, course_list):
#    i = name_list.index(student)
#    grade = grade_list[i]
#    course = course_list[i]
#    return (course, grade)
#
#names = ['Ana', 'John', 'Denise', 'Katy']
#grade = ['B', 'A+', 'A', 'A']
#course = [2.00, 6.0001, 20.002, 9.01]
#print(get_grade_list('John', names, grade, course))

#######################################
## EXAMPLE: getting grades using dictionaries
#######################################
#def get_grade_dict(student, grade_dict):
#    return grade_dict[student]
#
#d = {'Ana':(2.00,'B'), 'John':(6.0001,'A+'), 'Denise':(20.002,'A'), 'Katy':(9.01,'A')}
#print(get_grade_dict('John', d))


#######################################
## COMPLEX EXAMPLE: frequency dictionary of song lyrics
#######################################
def generate_word_dict(song):
    """
    input: song, a string
    returns: dictionary with keys: song words, 
             values: frequencies each word occurs
    """
    # remove special characters and convert to lowercase
    song_words = song.lower()
    words_list = song_words.split()
    word_dict = {}
    for w in words_list:
        if w in word_dict:
            # seen word again, so add one to frequency
            word_dict[w] += 1
        else:
            # insert a dictionary entry
            word_dict[w] = 1
    return word_dict
     
def find_frequent_word(word_dict):
    """
    input: word_dict, a dict mapping string:int
    Finds the words that occur the most
    returns: tuple of (list of words that occur most, frequency)
    """
    # a list in case there is more than one word occuring that often
    word = []
    highest = max(word_dict.values())
    for w in word_dict.keys():
        if word_dict[w] == highest:
            word.append(w)
    return (word, highest)
    
def occurs_often(word_dict, atleast):
    """
    input: word_dict, a dict
           atleast, an int
    Side effect warning, modifying word_dict here modifies word_dict passed in
    returns: list of tuples in order of frequency (list of words, frequency)
    """
    freq_list = []
    done = False
    # find and delete most common word(s), repeat for the 
    # 'atleast' most common words.
    while not done:
        # extract most frequet word(s)
        word_freq_tuple = find_frequent_word(word_dict)
        # do not care about words(s) if they occur very few times
        if word_freq_tuple[1] < atleast:
            done = True
        else:
            # keep track of most common words, append them in order
            freq_list.append(word_freq_tuple)
            for i in word_freq_tuple[0]:
                del(word_dict[i])
    return freq_list

# pick a song by uncommenting your favorite
#song = "I threw a wish in the well Dont ask me Ill never tell I looked to you as it fell And now youre in my way  Id trade my soul for a wish Pennies and dimes for a kiss I wasnt looking for this But now youre in my way  Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where do you think youre going baby  Hey I just met you And this is crazy But heres my number So call me maybe  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  You took your time with the call I took no time with the fall You gave me nothing at all But still youre in my way  I beg and borrow and steal Have foresight and its real I didnt know I would feel it But its in my way  Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where you think youre going baby  Hey I just met you And this is crazy But heres my number So call me maybe  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  Before you came into my life I missed you so bad I missed you so bad I missed you so so bad  Before you came into my life I missed you so bad And you should know that I missed you so so bad bad bad  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  Before you came into my life I missed you so bad I missed you so bad I missed you so so bad  Before you came into my life I missed you so bad And you should know that  So call me maybe"
#song = "Youre insecure Dont know what for Youre turning heads when you walk through the door Dont need makeup To cover up Being the way that you are is enough  Everyone else in the room can see it Everyone else but you  Baby you light up my world like nobody else The way that you flip your hair gets me overwhelmed But when you smile at the ground it aint hard to tell You dont know Oh oh You dont know youre beautiful If only you saw what I can see Youd understand why I want you so desperately Right now Im looking at you and I cant believe You dont know Oh oh You dont know youre beautiful Oh oh Thats what makes you beautiful  Zayn So ccome on You got it wrong To prove Im right I put it in a song I dont know why Youre being shy And turn away when I look into your eyeeyeeyes  Everyone else in the room can see it Everyone else but you  Baby you light up my world like nobody else The way that you flip your hair gets me overwhelmed But when you smile at the ground it aint hard to tell You dont know Oh oh You dont know youre beautiful If only you saw what I can see Youll understand why I want you so desperately Right now Im looking at you and I cant believe You dont know Oh oh You dont know youre beautiful Oh oh  Thats what makes you beautiful  Na na na na na na na na na na Na na na na na na Na na na na na na Na na na na na na  Baby you light up my world like nobody else The way that you flip your hair gets me overwhelmed But when you smile at the ground it aint hard to tell  You dont know Oh oh You dont know youre beautiful  Baby you light up my world like nobody else The way that you flip your hair gets me overwhelmed But when you smile at the ground it aint hard to tell You dont know Oh oh You dont know youre beautiful Oh If only you saw what I can see Youll understand why I want you so desperately Harry: desperately Right now Im looking at you and I cant believe You dont know Oh oh You dont know youre beautiful Oh oh You dont know youre beautiful Oh oh  Thats what makes you beautiful"
#song = "We we dont have to worry bout nothing Cause we got the fire and were burning one hell of a something They they gonna see us from outer space outer space Light it up like were the stars of the human race human race  When the light started out they don’t know what they heard Strike the match play it loud giving love to the world Well be raising our hands shining up to the sky Cause we got the fire fire fire Yeah we got the fire fire fire  And we gonna let it burn burn burn burn We gonna let it burn burn burn burn Gonna let it burn burn burn burn We gonna let it burn burn burn burn  We dont wanna leave no We just wanna be right now right rrright now And what we see is everybodys on the floor acting crazy getting loco til the lights out Musics on Im waking up we fight the fire then we burn it up And its over now we got the love theres no sleeping now no sleeping now no sleeping  When the light started out they don’t know what they heard Strike the match play it loud giving love to the world Well be raising our hands shining up to the sky Cause we got the fire fire fire Yeah we got the fire fire fire  And we gonna let it burn burn burn burn We gonna let it burn burn burn burn Gonna let it burn burn burn burn We gonna let it burn burn burn burn  When the light started out they don’t know what they heard Strike the match play it loud giving love to the world  We gonna let it burn burn burn burn burn burn Burn burn burn burn burn burn  We can light it up up up So they cant put it out out out We can light it up up up So they cant put it out out out We can light it up up up So they cant put it out out out We can light it up up up So they cant put it out out out  When the light started out they don’t know what they heard Strike the match play it loud giving love to the world Well be raising our hands shining up to the sky Cause we got the fire fire fire Yeah we got the fire fire fire  And we gonna let it burn burn burn burn We gonna let it burn burn burn burn Gonna let it burn burn burn burn We gonna let it burn burn burn burn  When the light started out they don’t know what they heard Strike the match play it loud giving love to the world Well be raising our hands shining up to the sky Cause we got the fire fire fire Yeah we got the fire fire fire  And we gonna let it burn"
#song = "The snow glows white on the mountain tonight Not a footprint to be seen A kingdom of isolation And it looks like Im the queen  The wind is howling like this swirling storm inside Couldnt keep it in heaven knows I tried  Dont let them in dont let them see Be the good girl you always have to be Conceal dont feel dont let them know Well now they know  Let it go let it go Cant hold it back anymore Let it go let it go Turn away and slam the door  I dont care What theyre going to say Let the storm rage on The cold never bothered me anyway  Its funny how some distance Makes everything seem small And the fears that once controlled me Cant get to me at all  Its time to see what I can do To test the limits and break through No right no wrong no rules for me Im free  Let it go let it go I am one with the wind and sky Let it go let it go Youll never see me cry  Here I stand And here Ill stay Let the storm rage on  My power flurries through the air into the ground My soul is spiraling in frozen fractals all around And one thought crystallizes like an icy blast Im never going back The past is in the past  Let it go let it go And Ill rise like the break of dawn Let it go let it go That perfect girl is gone  Here I stand In the light of day Let the storm rage on The cold never bothered me anyway"
#song = "Because you know Im all about that bass  Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass bass bass bass  Yeah its pretty clear I aint no size two But I can shake it shake it like Im supposed to do Cause I got that boom boom that all the boys chase And all the right junk in all the right places I see the magazine workin that Photoshop We know that stuff aint real come on now make it stop If you got beauty beauty just raise em up Cause every inch of you is perfect from the bottom to the top Yeah my mama she told me dont worry about your size Shoo wop wop shaooh wop wop She says Boys like a little more booty to hold at night That booty uh that booty booty You know I wont be no stick figure silicone Barbie doll So if that what youre into then go head and move along Because you know Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass Hey Im bringing booty back Go head and tell them skinny girls that No Im just playing I know you think youre fat But Im here to tell you Every inch of you is perfect from the bottom to the top Yeah my mama she told me dont worry about your size Shoo wop wop shaooh wop wop She says Boys like a little more booty to hold at night That booty booty uh that booty booty You know I wont be no stick figure silicone Barbie doll So if thats what youre into then go head and move along Because you know Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass You know Im all about that bass Bout that bass no treble I said Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass Because you know Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass no treble Im all about that bass Bout that bass Hey Im all about that bass Bout that bass Hey Im all about that bass Bout that bass Hey Yeah yeah ohh You know you like this bass Hey "
song = "It might seem crazy what Im about to say Sunshine shes here you can take a break Im a hot air balloon that could go to space With the air like I dont care baby by the way  Uh  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Here come bad news talking this and that yeah Well give me all you got and dont hold it back yeah Well I should probably warn you Ill be just fine yeah No offense to you dont waste your time Heres why  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Hey Go Uh  Happy Bring me down Cant nothing Bring me down My levels too high Bring me down Cant nothing Bring me down I said let me tell you now Bring me down Cant nothing Bring me down My levels too high Bring me down Cant nothing Bring me down I said  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Hey Go Uh  Happy repeats Bring me down cant nothing Bring me down my levels too high Bring me down cant nothing Bring me down I said let me tell you now  Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do   Because Im happy Clap along if you feel like a room without a roof Because Im happy Clap along if you feel like happiness is the truth Because Im happy Clap along if you know what happiness is to you Because Im happy Clap along if you feel like thats what you wanna do  Hey Cmon"

song_dict = generate_word_dict(song)
print("***** WORDS IN SONG *****")
print(song_dict)
print("***** MOST COMMON WORD *****")
print(find_frequent_word(song_dict))
print("***** TOP MOST COMMON WORDS *****")
print(occurs_often(song_dict, 20))


#######################################
## EXAMPLE: fibonacci without and with a dictionary
#######################################
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
        
def fib_efficient(n, d):
    # side effect - modifying d here modifies original d
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
#print(fib(34)) # 11,405,773 recursive calls
#
#d = {1:1, 2:2}
#print(fib_efficient(34, d)) # 65 recursive calls
