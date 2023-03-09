# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: server_simple.py
@Time: 2023-03-09 22:39
@Last_update: 2023-03-09 22:39
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import gradio as gr
from lib.OpenaiBot import OpenaiBot

openai_bot = OpenaiBot()


def ask_chatGPT(openai_key, role, new_msg, state):
    """向chatGPT提问"""
    res_content = '对不起，服务器出错了，请稍后再试。'
    res = [(new_msg, res_content)]
    try:
        openai_bot.set_api_key(openai_key)
        res_content = openai_bot.get_response(role, new_msg, state)
        res = [(new_msg, res_content)]
    except Exception as e:
        print(e)
    finally:
        state += res
        res = state

    return res, state


def clean_question(question):
    """清除问题"""
    return ''


if __name__ == '__main__':
    with gr.Blocks(title="尝试chatGPT对话", css="#maxheight {max-height: 500px} ") as demo:
        state = gr.State([])
        with gr.Column(variant='panel'):
            # title
            with gr.Row():
                gr.Markdown("## 尝试chatGPT对话")
            with gr.Row():
                # left part
                with gr.Column():
                    openai_key = gr.Textbox(
                        label='openai_key', placeholder='输入你openai的api key', type='password')
                    role_b = gr.Textbox(
                        label='请输入你设定的chatGPT的角色', lines=2,
                        value='你是ChatGPT，OpenAI训练的大规模语言模型，简明的回答用户的问题。')
                    question_b = gr.Textbox(
                        label='请输入你想要问的问题',
                        placeholder='输入你想提问的内容...',
                        lines=3
                    )
                    with gr.Row():
                        greet_btn = gr.Button('提交', variant="primary")
                # right part
                with gr.Column():
                    answer_b = gr.Chatbot(
                        label='chatGPT的问答', value=[(None, '请在这里提问')], elem_id='maxheight')

        greet_btn.click(fn=ask_chatGPT, inputs=[openai_key, role_b, question_b, state], outputs=[answer_b, state])
        greet_btn.click(fn=clean_question, inputs=[question_b], outputs=[question_b])

    demo.launch()
    demo.close()
