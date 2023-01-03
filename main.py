from wordcloud import wordcloud
from konlpy.tag import Twitter
from collections import Counter

text = open('test.txt').read()

twitter = Twitter()

sentences_tag = []
sentences_tag = twitter.pos(text)

adj_list = []

for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        adj_list.append(word)

counts = Counter(adj_list)
tags = counts.most_common(40)

wc = wordcloud(font_path=['C:\Windows\Fonts\나눔고딕'],background_color="orange", max_font_size=40)
cloud = wc.frequncies(dict(tags))

cloud.to_file('test.jpg')