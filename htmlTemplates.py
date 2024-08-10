css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #2b313e;
    color: white;
    text-align: right;
}

.footer p {
    margin: 0;
    padding: 1rem;
}

a:link {
        color: #64feda;
        background-color: transparent;
        text-decoration: none;
        }

</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://pub-f858c7e521464395920779af297fb1bd.r2.dev/TalkWithPFD-icon.png" style="max-height: 55px; max-width: 55px; border-radius: 20%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://avatars.githubusercontent.com/u/63995315" style="max-height: 45px; max-width: 45px; border-radius: 20%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
"""

footer = """
        <div class="footer">
        <p>Made by <a href="https://yesbhautik.co.in" style="color:#64feda;">Yesbhautik</a> with <a href="https://streamlit.io" style="color:#36AE7C;">Streamlit</a></p>
        </div>
"""
