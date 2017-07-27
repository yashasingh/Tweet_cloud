from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class MyCloud():

    def generate(self, title, text):
        wordcloud = WordCloud(max_font_size=40).generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        # plt.show()
        filename = title + '.png'
        plt.savefig(filename,  bbox_inches='tight')