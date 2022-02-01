import wordcloud
from matplotlib import pyplot as plt
f = open("yoooo.txt", encoding="utf8")
file_contents = f.read()
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    #wordcloud
    file_contents = file_contents.lower()
    dict = {}
    words = file_contents.split(" ")
    final = []
    for word in words:
        if word not in uninteresting_words and word.isalpha():
            if word[-1] not in punctuations:
                final.append(word)
            else:
                final.append(word[:-1])
    for word in final:
        if word not in dict:
            dict[word] = 0
        dict[word] += 1 
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()