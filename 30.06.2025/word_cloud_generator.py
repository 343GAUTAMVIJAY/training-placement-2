from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = input("Enter text: ")
wordcloud = WordCloud(width=800, height=400).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.png')
print("Word cloud saved as wordcloud.png")