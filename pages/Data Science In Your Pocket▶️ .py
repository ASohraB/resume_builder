import pandas as pd
import streamlit as st
from streamlit_player import st_player
import os

st.error('My debut book on Generative AI is out', icon="📕")
name="LangChain in your Pocket: Beginner's Guide to Building Generative AI Applications using LLMs"
url="https://medium.com/data-science-in-your-pocket/my-first-book-langchain-in-your-pocket-is-out-9a1f156c0f7b"
st.markdown("""<a href={}><b><u>{}</b></u></a>""".format(url,name),unsafe_allow_html=True)

st.header('Youtube Playlists')
path = os.getcwd()+'/pdfs/youtube.csv'
df = pd.read_csv(path)
df = df.sample(frac = 1).reset_index()
x=0


html = '''<iframe id="ytplayer" type="text/html" width="75%" height="300"
src="https://www.youtube.com/embed/?listType=playlist&list={}"
frameborder="0" allowfullscreen>'''

while x<1:
        url = "https://www.youtube.com/playlist?list="+df.at[x,'playlist']
        st.subheader("[{}]({})".format(df.at[x,'name'],url))
        st.components.v1.html(html.format(df.at[x,'playlist']), width=800, height=300, scrolling=False)
        x+=1

st.write('sample video')
st_player('https://www.youtube.com/watch?v=X5DViFo9kXw')