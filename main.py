import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

st.title('Streamlit Demo App')

#プログレスバーの表示
st.write('[Site Download]')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!!!!'

#画像を表示
#チェックボックスによるメディアの表示可否
st.write('[Interactive Widgets]')
if st.sidebar.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Small Boat Next To Catamaran On Water', use_column_width=True)

#セレクトボックスによる値の動的変化
option = st.sidebar.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字：',option

#テキストボックスによる値の動的変化
text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味：',text

#スライダーによる値の動的変化
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'今日のコンディション：',condition

#カラム機能
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('Here is right column')


#表を描画
st.write('DataFlame1')

df_1 = pd.DataFrame({
    'fast':[1, 2, 3, 4],
    'second':[10, 20, 30, 40]
})

st.dataframe(df_1.style.highlight_max(axis=0))


#チャート描画
st.write('DataFlame2')

df_2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df_2)
st.area_chart(df_2)
st.bar_chart(df_2)


#マップを描画
st.write('DataFlame3')

df_3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70] ,
    columns=['lat','lon']
)

st.map(df_3)

#エクスパンダ機能
expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ解答１')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ解答２')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ解答３')
