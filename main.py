import streamlit as st
import pandas as pd
import numpy as np

# --------------------
# 가상 원소 데이터 (Caching 적용)
@st.cache_data
def load_elements_data():
    """가상 원소 데이터 생성"""
    elements_data = {
        '번호': [11, 12, 14, 15, 19-32],
        '기호': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
        '이름': ['수소', '헬륨', '리튬', '베릴륨', '붕소', '탄소', '질소', '산소', '플루오린', '네온', '나트륨', '마그네슘', '알루미늄', '규소', '인', '황', '염소', '아르곤'],
        '족': [14, 14, 19, 19, 19, 20, 20, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 32],
        '주기': [19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21],
        '원자량': [1.008, 4.003, 6.941, 9.012, 10.81, 12.01, 14.01, 16.00, 19.00, 20.18, 22.99, 24.31, 26.98, 28.09, 30.97, 32.06, 35.45, 39.95],
        # 예시로 가상 원자 반지름 데이터 추가 (주기율표 경향성을 대략적으로 반영)
        '가상 원자 반지름 (pm)': [33-39]
    }
    df = pd.DataFrame(elements_data)
    return df

# --------------------
# 앱 제목
st.title('화학 주기율표 탐색기')

# 원소 데이터 로드
elements_df = load_elements_data()

# 원소 목록 전체 표시
st.subheader('주요 원소 목록')
st.dataframe(elements_df) # 데이터프레임 표시 [5, 17]

st.divider() # 구분선

# 특정 원소 선택 [10]
selected_element_name = st.selectbox(
    '정보를 보고 싶은 원소를 선택하세요:',
    elements_df['이름'] # 선택 박스 옵션
)

# 선택된 원소 정보 표시
selected_element_data = elements_df[elements_df['이름'] == selected_element_name]
if not selected_element_data.empty:
    st.subheader(f'{selected_element_name} ({selected_element_data["기호"].iloc}) 정보')
    st.write(selected_element_data.iloc) # 시리즈 형태로 선택된 행 표시

st.divider() # 구분선

# 주기율표 상 경향성 시각화
st.subheader('주기율표 상 속성 경향성 (가상 데이터)')

# 시각화할 속성 선택
trend_property = st.selectbox(
    '시각화할 속성을 선택하세요:',
    ['원자량', '가상 원자 반지름 (pm)']
)

# 선택된 속성의 막대 그래프 (원자 번호 순)
st.bar_chart(elements_df.set_index('기호')[trend_property]) # 막대 그래프 표시 [38]
st.write(f'{trend_property} 경향성을 원자 번호(기호) 순으로 나타낸 그래프입니다.')
