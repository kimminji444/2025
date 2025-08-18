import streamlit as st

# MBTI별 직업 추천 데이터 (예시)
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구원"],
    "ENTP": ["기업가", "마케팅 기획자", "벤처 투자자"],
    "INFJ": ["상담사", "작가", "교육자"],
    "ESFP": ["배우", "이벤트 기획자", "광고 크리에이터"],
    # 필요한 만큼 추가
}

st.title("MBTI 기반 진로 추천 프로그램")

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 직업 추천 출력
if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 유형 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

