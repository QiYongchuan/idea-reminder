from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

font_path = 'SimHei.ttf'

# 示例文本
text = """
用文字记录我的胡思乱想与生活的瞬间，我疯狂的想法与可能为之的行动。
一个从农学研究生退学转行到计算机行业的年轻人。
记录在这个时代下的焦虑、迷茫、挣扎与希望。
提醒自己：
1.放弃向他人证明自己，放弃向自己证明自己。专注忘我地去做你应该做的事情，心无旁骛地去解决问题。当你脚踏实地的走自己的路时，那种拼命想要证明什么的冲动就会越来越少。你也会因此变得轻松、自由。
——查理·芒格

2.“我们没有希望，他们也没有希望，这就是希望。”

"""

# 创建词云对象
wordcloud = WordCloud(font_path=font_path, width=800, height=400).generate(text)


# 显示生成的词云图片
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') # 关闭坐标轴
plt.show()
