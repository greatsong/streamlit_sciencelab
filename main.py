import streamlit as st
import pandas as pd

# --------------------
# 예시용 원소 데이터 (캐싱 생략)
def load_elements_data():
    """예시용 원소 데이터 생성"""
    elements_data = {
        '번호': list(range(1, 19)),  # 1~18번
        '기호': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
        '이름': ['수소', '헬륨', '리튬', '베릴륨', '붕소', '탄소', '질소', '산소', '플루오린', '네온',
                '나트륨', '마그네슘', '알루미늄', '규소', '인', '황', '염소', '아르곤'],
        '족': [1, 18, 1, 2, 13, 14, 15, 16, 17, 18,
              1, 2, 13, 14, 15, 16, 17, 18],
        '주기': [1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 3, 3, 3, 3, 3],
        '원자량': [1.008, 4.003, 6.941, 9.012, 10.81, 12.01, 14.01, 16.00,
                  19.00, 20.18, 22.99, 24.31, 26.98, 28.09, 30.97, 32.06, 35.45, 39.95],
        '예시 원자 반지름 (pm)': [
            53, 31, 167, 112, 87, 67, 56, 48, 42, 38,
            190, 145, 118, 111, 98, 88, 79, 71
        ]
    }
    return pd.DataFrame(elements_data)

# --------------------
# 앱 제목 및 설명
st.title('🔬 주기율표 속성 탐색기')
st.markdown("이 앱은 **예시 원소 데이터**를 통해 주기율표 속성 경향성을 시각적으로 탐색할 수 있도록 도와줍니다. 과학 수업에서 원소의 주기적 성질과 경향성을 학습하는 데 활용해보세요!")

# --------------------
# 원소 데이터 로드
elements_df = load_elements_data()

# --------------------
# 전체 원소 목록 표시
st.subheader('🧪 원소 목록 보기')
st.dataframe(elements_df, use_container_width=True)

st.divider()

# --------------------
# 특정 원소 선택
selected_element_name = st.selectbox('🔍 정보를 보고 싶은 원소를 선택하세요:', elements_df['이름'])
selected_element_data = elements_df[elements_df['이름'] == selected_element_name]

if not selected_element_data.empty:
    st.subheader(f"📘 {selected_element_name} ({selected_element_data['기호'].iloc[0]}) 상세 정보")
    st.write(selected_element_data.iloc[0].to_frame().T)

st.divider()

# --------------------
# 속성 시각화
st.subheader('📊 주기율표 속성의 경향성 보기')

trend_property = st.selectbox(
    '📈 시각화할 속성을 선택하세요:',
    ['원자량', '예시 원자 반지름 (pm)']
)

st.bar_chart(elements_df.set_index('기호')[trend_property])
st.markdown(f"✅ 위 그래프는 **{trend_property}**의 값을 **원소 기호 순서**대로 막대 그래프로 보여줍니다.")
