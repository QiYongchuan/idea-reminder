from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

font_path = 'SimHei.ttf'

# 示例文本
text = """
2023年，大部分时间静不下心来，书坦白讲只读了大概两本书。
一本是莫言的《丰乳肥臀》，剩下的一本是《百年孤独》。
今年新读的就一本，《百年孤独》是不知道第几遍了。有意思的是，随着读的次数越来越多，我发现似乎我也快陷入到那个反复重复循环命名家族，
反复重复某种命运的怪圈里了。
晚年的少校把自己关在房间里，重复的制作小金鱼，融化，继续制作金鱼。我呢，也是反反复复的看同一本书，看奥雷米亚诺，看何塞阿尔卡迪诺，
命运反反复复的重演。
《丰乳肥臀》是我看的莫言的第一本小说，也是因为有人说莫言被称为“中国版的马尔克斯”，丰乳肥臀有人叫它中国版的《百年孤独》。

"""

# 创建词云对象
wordcloud = WordCloud(font_path=font_path, width=800, height=400).generate(text)


# 显示生成的词云图片
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') # 关闭坐标轴
plt.show()
