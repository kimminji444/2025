import streamlit as st

# --- 직업 데이터 (예시) ---
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 과학자", "🔬 연구원"],
    "ENTP": ["🚀 기업가", "🎯 마케팅 기획자", "💡 벤처 투자자"],
    "INFJ": ["💬 상담사", "✍️ 작가", "👩‍🏫 교육자"],
    "ESFP": ["🎭 배우", "🎉 이벤트 기획자", "📺 광고 크리에이터"],
    "ISTJ": ["📚 회계사", "🏛️ 법률가", "🏢 관리자"],
    "ENFP": ["🌈 크리에이티브 디렉터", "🎤 방송인", "🎶 음악가"],
    "ENTJ": ["👔 CEO", "⚖️ 변호사", "📈 전략 기획자"],
    "ISFP": ["🎨 아티스트", "📷 사진작가", "🎵 음악 프로듀서"],
    # ... 나머지 MBTI도 채워 넣을 수 있음
}

# --- 페이지 타이틀 ---
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="centered")
st.title("✨ MBTI 기반 진로 추천 프로그램 ✨")
st.markdown("당신의 성격 유형에 맞는 직업을 찾아보세요! 💼🚀")

# --- MBTI 선택 ---
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요", mbti_list)

# --- 결과 출력 ---
if selected_mbti:
    st.markdown(f"## 🌟 {selected_mbti} 유형 추천 직업 🌟")
    st.success("당신에게 잘 맞는 직업들이에요! ✨")
    
    for job in mbti_jobs[selected_mbti]:
        st.write(f"💡 {job}")

    st.markdown("---")
    st.info("🔮 MBTI는 참고용일 뿐! 진짜 진로는 당신의 열정과 경험이 결정해요 💖")
