print("loading...")

from nltk.stem import WordNetLemmatizer
import json
import sys
v = '-v' in sys.argv
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

lemmatizer = WordNetLemmatizer()

# copied and edited from [here](https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50)
def get_jaccard_sim(str1, str2):
    ap = str1

    # https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
    for ele in ap:
        if ele in punc:
            ap = ap.replace(ele, "")

    a = set(ap.split())
    al = set()
    for word in a:
        al.add(lemmatizer.lemmatize(word).lower())

    bp = str2
    for ele in bp:
        if ele in punc:
            bp = bp.replace(ele, "")
    b = set(bp.split())
    bl = set()
    for word in b:
        bl.add(lemmatizer.lemmatize(word).lower())
    c = al.intersection(bl)
    try:
        return float(len(c)) / (len(al) + len(bl) - len(c))
    except ZeroDivisionError:
        return 0.0

# load responses file
responses = {}
with open('responses.json', 'r') as fp:
    responses = json.load(fp)

print("loaded!")
me = ""

# main loop
try:
    if '-dl' in sys.argv:
        print("Not learning")
        while True:
            you = input("> ")
            scores = {}

            # calculate score for each response
            for response in responses:
                scores[response] = get_jaccard_sim(you, response)
            closest = max(scores, key=scores.get)

            # just in case the bot hasn't heard of anything you said
            if scores[closest] == 0.0:
                me = "hmm. " + you
            else:
                closest = max(scores, key=scores.get)
                me = responses[closest]
            if v:
                print("'" + closest + "'", "is", str(scores[closest]*100) + "% similar.")
            print(me)
    else:
        while True:
            you = input("> ")
            responses[me] = you
            scores = {}

            # calculate score for each response
            for response in responses:
                scores[response] = get_jaccard_sim(you, response)
            closest = max(scores, key=scores.get)

            # just in case the bot hasn't heard of anything you said
            if scores[closest] == 0.0:
                me = "hmm. " + you
            else:
                closest = max(scores, key=scores.get)
                me = responses[closest]
            print(me)

except:
    if not '-dl' in sys.argv:
        print("saving and exiting...")
        
        with open('responses.json', 'w') as fp:
            json.dump(responses, fp)
# test
print("done!")


