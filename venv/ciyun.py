import jieba
import wordcloud
from imageio import imread
mask=imread("C:/Users/Lenovo/Desktop/格格的文件/RandG.png")
exclude={'我们','你们','他们','它们','因为','因而','所以','如果','那么',\
'如此','只是','但是','就是','这是','那是','而是','而且','虽然','这些',\
'有些','然后','已经','于是','一种','一个','一样','时候','没有','什么',\
'这样','这种','这里','不会','一些','这个','仍然','不是','自己','知道',\
'可以','看到','那儿','问题','一会儿','一点','现在','两个','三个'}
f=open("C:/Users/Lenovo/Desktop/格格的文件/伤.txt","r", encoding="utf-8")
t =f.read()
f.close()
ls =jieba.lcut(t)
ls = [word for word in ls if len(word)>1]# 该条主要是为了排除一个字符以下的词，没有这条文本将会分出都是单字。
txt=" ".join(ls)
w =wordcloud.WordCloud( scale=4, stopwords=exclude, mask=mask,font_path= "C:/Windows/Fonts/msyh.ttc",width= 1000,height =700,background_color="white")
w.generate(txt)
w.to_file("在一起悲.png")