# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:27:36 2022

@author: pccnf
"""

import streamlit as st
import pandas as pd
import datetime
import os
import glob

iDir = iDir = os.getcwd()#このプログラムと同じディレクトリ
filename = glob.glob('ダッシュボードデータ.xlsx')
Filename = "".join(filename)#上のままではリストなので文字列に直す
FILE = iDir+ "/" + Filename#'C:\\Users\\pccnf\\Desktop\\making_dashboard\\ダッシュボードデータ.xlsx'

st.set_page_config(layout="wide")#layout=”wide”としないとグラフが中心よって両サイドに不必要な空白が生まれる

st.title('産業政策部　政府統計ダッシュボード（仮）')
st.header('経産省　鉱工業指数')

left_column, right_column = st.columns(2)
left_column.subheader('電子部品・デバイス')
df = pd.read_excel(FILE,sheet_name='電子部品デバイス',index_col='年月')
#df = pd.read_excel(r'C:\Users\pccnf\Desktop\streamlit\ダッシュボードデータ.xlsx',sheet_name='電子部品デバイス',index_col='年月')
df_ri = df.reset_index()
df_ri['年月'].max().strftime('%Y/%m')
df_re = df_ri['年月'].dt.strftime('%Y/%m')
df_ri = df_ri.drop(columns='年月')
df_ri.insert(0, 'year-month', df_re)

#st.table(df_ri)
max_value = df_re.max()
min_value = df_re.min()
max_date = datetime.datetime.strptime(max_value, '%Y/%m')
min_date = datetime.datetime.strptime(min_value, '%Y/%m')

max = max_date.year
min = min_date.year

left_column.line_chart(df, width=900, height=500, use_container_width=False)
#st.slider("表示範囲", min, max, value=(min, max))
#df_re = df_ri[df_ri['year-month']<=st.slider]

#start_year, end_year = st.slider(
    #"表示範囲",
    #min_value=min, max_value=max,
    #value=(min, max))




right_column.subheader('電気・情報通信機器')
df = pd.read_excel(FILE,sheet_name='電気情報通信機器',index_col='年月')

df_ri = df.reset_index()
df_ri['年月'].max().strftime('%Y/%m')
df_re = df_ri['年月'].dt.strftime('%Y/%m')
df_ri = df_ri.drop(columns='年月')
df_ri.insert(0, 'year-month', df_re)

right_column.line_chart(df, width=900, height=500, use_container_width=False)

left_column.subheader('在庫率')
df = pd.read_excel(FILE,sheet_name='在庫率',index_col='年月')

df_ri = df.reset_index()
df_ri['年月'].max().strftime('%Y/%m')
df_re = df_ri['年月'].dt.strftime('%Y/%m')
df_ri = df_ri.drop(columns='年月')
df_ri.insert(0, 'year-month', df_re)

left_column.line_chart(df, width=900, height=500, use_container_width=False)

col1 = st.columns(1)
st.header('経産省　生産動態統計')

left_column, right_column = st.columns(2)
left_column.subheader('品目別国内生産高の推移')
df = pd.read_excel(FILE,sheet_name='生産動態項目別生産金額',index_col='年月')

df_ri = df.reset_index()
df_ri['年月'].max().strftime('%Y/%m')
df_re = df_ri['年月'].dt.strftime('%Y/%m')
df_ri = df_ri.drop(columns='年月')
df_ri.insert(0, 'year-month', df_re)

#item_list = df.columns.to_list()#品目をリスト化する
#selected_item = st.selectbox('表示する品目を選択:',item_list)
#df = df[df.columns == selected_item]

left_column.line_chart(df, width=900, height=500, use_container_width=False)


col1 = st.columns(1)
st.header('経産省　特定サービス産業動態統計')

left_column, right_column = st.columns(2)
left_column.subheader('情報サービス産業の売上高の推移（4~9月）')
#df = pd.read_excel(FILE,sheet_name='特サビ統計',index_col='年')

df = pd.DataFrame({
    'ｿﾌﾄｳｴｱ開発・ﾌﾟﾛｸﾞﾗﾑ作成' :[4.91943497230385,4.93144564537357,5.090704,2.574693],
    'ｼｽﾃﾑ等管理運営受託' : [0.929766874649597,0.921282941840423,0.970283,0.505917],
    'その他' : [1.06469219368697,1.01380967738878,1.107981,0.28725]
    })
left_column.bar_chart(df, width=900, height=500, use_container_width=False)
