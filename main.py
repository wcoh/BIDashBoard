import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
import numpy as np
import io
import datetime

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 30, 20, 10, 15]
heatmap_data = np.random.rand(10, 10)

# 날짜 선택
selected_date = st.date_input('대시보드 날짜 선택', value=datetime.date(2023, 4, 1), min_value=datetime.date(2023, 4, 1), max_value=datetime.date(2023, 4, 10))

# 그래프를 그릴 전체 이미지 생성
fig = plt.figure(figsize=(5, 15))

# 막대그래프 생성
ax1 = fig.add_subplot(3, 1, 1)
ax1.bar(categories, values)
ax1.set_title('Bar Chart')
ax1.set_xlabel('Category')
ax1.set_ylabel('Value')

# 원형 그래프 생성
ax2 = fig.add_subplot(3, 1, 2)
ax2.pie(values, labels=categories)
ax2.set_title('Pie Chart')

# 히트맵 생성
ax3 = fig.add_subplot(3, 1, 3)
sns.heatmap(heatmap_data, cmap='YlGnBu', ax=ax3)
ax3.set_title('Heatmap')

# FigureCanvas 객체 생성
canvas = FigureCanvas(fig)

# 바이트 스트림 객체 생성
buf = io.BytesIO()
canvas.print_png(buf)

# 스트림 rewind
buf.seek(0)

# Streamlit으로 이미지 출력
st.image(buf, caption='Vision AI BI Solution', use_column_width=True)