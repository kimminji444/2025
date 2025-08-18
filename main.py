import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💞", layout="centered")
st.title("💞 MBTI 궁합 테스트 💞")
st.markdown("당신의 MBTI와 잘 맞는 궁합을 알아보세요! 🔮✨")

# --- MBTI 궁합 데이터 ---
mbti_match = {
    "INTJ": {"best": ["ENFP 🌈", "ENTP 🚀"], "worst": ["ISFP 🎨", "ESFP 🎭"]},
    "ENTP": {"best": ["INFJ ✨", "ENFP 🌈"], "worst": ["ISTJ 📚", "ISFJ 🤝"]},
    "INFJ": {"best": ["ENTP 🚀", "ENFP 🌈"], "worst": ["ESTP ⚡", "ISTP 🔧"]},
    "ENFP": {"best": ["INFJ ✨", "INTJ 🧠"], "worst": ["ESTJ 📅", "ISTJ 📚"]},
    "ISTJ": {"best": ["ESFP 🎭", "ESTP 🏅"], "worst": ["ENFP 🌈", "ENTP 🚀"]},
    "ISFJ": {"best": ["ESFP 🎭", "ESTP 🏅"], "worst": ["ENTP 🚀", "ENFP 🌈"]},
    "ESTJ": {"best": ["ISTP 🔧", "ESTP 🏅"], "worst": ["INFP ✒️", "ENFP 🌈"]},
    "ESFJ": {"best": ["ISFP 🎨", "ESFP 🎉"], "worst": ["INTP 💻", "ENTP 🚀"]},
    "ISTP": {"best": ["ESTJ 📅", "ENTJ 👔"], "worst": ["INFJ ✨", "ENFJ 👨‍🏫"]},
    "ISFP": {"best": ["ESFJ 👔", "ENFJ 👨‍🏫"], "worst": ["INTJ 🧠", "ENTJ 👔"]},
    "ESTP": {"best": ["ISTJ 📚", "ESTJ 📅"], "worst": ["INFJ ✨", "INFP ✒️"]},
    "ESFP": {"best": ["ISFJ 🤝", "ESFJ 👩‍🏫"], "worst": ["INTJ 🧠", "INTP 💻"]},
    "ENTJ": {"best": ["ENTP 🚀", "INTP 💻"], "worst": ["ISFP 🎨", "INFP ✒️"]},
    "INTP": {"best": ["ENTJ 👔", "ENTP 🚀"], "worst": ["ESFJ 👩‍🏫", "ESFP 🎭"]},
    "INFP": {"best": ["ENFJ 👨‍🏫", "ENTJ 👔"], "worst": ["ESTJ 📅", "ESTP 🏅"]},
    "ENFJ": {"best": ["INFP ✒️", "ISFP 🎨"], "worst": ["ISTP 🔧", "ESTP ⚡"]},
}

# --- MBTI 선택 ---
mbti_list = list(mbti_match.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요", mbti_list)

# --- 결과 출력 ---
if selected_mbti:
    st.markdown(f"## 🌟 {selected_mbti}의 궁합 결과 🌟")

    best = mbti_match[selected_mbti]["best"]
    worst = mbti_match[selected_mbti]["worst"]

    st.success(f"💖 최고의 궁합: {', '.join(best)}")
    st.error(f"⚡ 맞지 않는 궁합: {', '.join(worst)}")

    st.markdown("---")
    st.info("💡 MBTI 궁합은 재미로만 참고하세요! 실제 인간관계는 노력과 이해가 더 중요해요 🤗")
