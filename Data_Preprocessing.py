import json
from os import listdir
from os.path import isdir, isfile, join

with open("config.json", "r") as f:
    data = json.load(f)

user_profile_features = data["user profile"]
user_tweet_features = data["user tweet"]

def user_profile_process(path):
    list_of_prof_features = {}
    mypath = path
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in files:
        print(file)
        with open(join(mypath,file), 'r', encoding="utf8") as f:
            temp = json.load(f)
            new_dict = {x: v for x, v in temp.items() if x in user_profile_features}
            list_of_prof_features[str(file)] = new_dict

    json_object = json.dumps(list_of_prof_features, indent=4)
 
    
    with open("Base Model's Data\\Logistic Regression with Particle Swarm Optimization\\prof.json", "w", encoding="utf8") as outfile:
        outfile.write(json_object)
    return 0



def user_tweet_process(path):
    size = 1000
    list_of_user_tweet_features = {}
    mypath = path
    dirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    for dir in dirs:
        list_of_tweet = []
        path = join(mypath, dir)
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        counter = 0
        for file in onlyfiles:
            with open(join(path,file), 'r', encoding="utf8") as f:
                temp = json.load(f)
                new_dict = {x: v for x, v in temp.items() if x in user_tweet_features}
                list_of_tweet.append(new_dict)
            counter += 1
            if counter == 1000:
                break
        print(f"{str(dir)} is done!")
        list_of_user_tweet_features[str(dir)] = list_of_tweet

    json_object = json.dumps(list_of_user_tweet_features, indent=4)
 
    
    with open("Base Model's Data\\Logistic Regression with Particle Swarm Optimization\\tweet_1000.json", "w", encoding="utf8") as outfile:
        outfile.write(json_object)

    return 0 

def user_mention_process(path):
    list_of_user_mentions = {}
    mypath = path
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in files:
        with open(join(mypath,file), 'r', encoding="utf8") as f:
            temp = json.load(f)
            new_dict = {x: v for x, v in temp.items()}
            list_of_user_mentions[str(file)] = new_dict

    json_object = json.dumps(list_of_user_mentions, indent=4)
    with open("Base Model's Data\\Logistic Regression with Particle Swarm Optimization\\mention.json", "w", encoding="utf8") as outfile:
        outfile.write(json_object)
    return 0






user_tweet_process("Labeled Data\\Users Tweets")
# user_profile_process("Labeled Data\\Twitter Profiles Json")
# user_mention_process("Labeled Data\\Users Mentions")