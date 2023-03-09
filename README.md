# ChatGPT-gradio
# 简介

> 这是一个可以简单的把ChatGPT的API应用的前端网页，通过gradio进行构建。同时给出了简单的无需数据库的版本和加入数据库的两个不同的版本。

 
基于ChatGPT的[API](https://github.com/openai/openai-python) 接口进行调用。

app的版本是已经直接部署到huggingface space的版本，没有任何的状态存储所以不需要数据库的支持。

而server版本是使用gradio结合mongodb的实现方式，加入了对于gradio的access token的识别并获取，对于想要使用gradio构建自己的应用的朋友有一定的参考价值。需要注意的是这里需要通过offline部分的代码提前加入用户。

有任何问题欢迎来骚扰，vx: freshield