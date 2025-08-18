import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💞", layout="centered")
st.title("💞 MBTI 궁합 테스트 💞")
st.markdown("당신의 MBTI와 잘 맞는 궁합을 알아보세요! 🔮✨")

# --- MBTI 궁합 데이터 ---
mbti_match = {
    "INTJ": {
        "best": [
            {"type": "ENFP 🌈", "reason": "자유롭고 창의적인 ENFP가 INTJ의 치밀한 계획에 활력을 불어넣어요."},
            {"type": "ENTP 🚀", "reason": "끊임없는 아이디어를 내는 ENTP와 INTJ의 전략적 사고가 잘 어울려요."},
        ],
        "worst": [
            {"type": "ISFP 🎨", "reason": "감성적인 ISFP는 현실적이고 냉철한 INTJ의 성향을 답답하게 느낄 수 있어요."},
            {"type": "ESFP 🎭", "reason": "즉흥적이고 즐거움을 추구하는 ESFP와는 생활 리듬이 달라 충돌할 수 있어요."},
        ],
    },
    "ENTP": {
        "best": [
            {"type": "INFJ ✨", "reason": "깊이 있는 INFJ가 ENTP의 넘치는 에너지를 균형 있게 잡아줘요."},
            {"type": "ENTJ 👔", "reason": "리더십 강한 ENTJ와 ENTP의 아이디어는 강력한 시너지를 내요."},
        ],
        "worst": [
            {"type": "ISTJ 📚", "reason": "원칙적인 ISTJ와 즉흥적인 ENTP는 사고방식 차이가 커요."},
            {"type": "ISFJ 🤝", "reason": "세심한 ISFJ는 변덕스러운 ENTP의 성향을 힘들어할 수 있어요."},
        ],
    },
    "INFJ": {
        "best": [
            {"type": "ENTP 🚀", "reason": "활발한 ENTP가 INFJ의 진지함을 밝게 만들어줘요."},
            {"type": "ENFP 🌈", "reason": "따뜻한 INFJ와 활발한 ENFP는 서로를 격려하는 좋은 파트너예요."},
        ],
        "worst": [
            {"type": "ESTP ⚡", "reason": "즉흥적인 ESTP는 신중한 INFJ에게 불안감을 줄 수 있어요."},
            {"type": "ISTP 🔧", "reason": "감정을 잘 표현하지 않는 ISTP와는 정서적 교감이 부족할 수 있어요."},
        ],
    },
    "ENFP": {
        "best": [
            {"type": "INFJ ✨", "reason": "깊이 있는 INFJ가 ENFP의 넘치는 에너지를 안정시켜줘요."},
            {"type": "INTJ 🧠", "reason": "계획적인 INTJ가 ENFP의 아이디어를 현실로 실현하게 도와줘요."},
        ],
        "worst": [
            {"type": "ESTJ 📅", "reason": "규율을 중시하는 ESTJ는 자유분방한 ENFP를 답답해할 수 있어요."},
            {"type": "ISTJ 📚", "reason": "보수적인 ISTJ와 ENFP의 즉흥성은 충돌이 잦아요."},
        ],
    },
    "ISTJ": {
        "best": [
            {"type": "ESFP 🎭", "reason": "활발한 ESFP가 ISTJ의 단조로운 일상에 즐거움을 더해줘요."},
            {"type": "ESTP 🏅", "reason": "실행력 있는 ESTP와 ISTJ의 철저함이 잘 맞아요."},
        ],
        "worst": [
            {"type": "ENFP 🌈", "reason": "즉흥적인 ENFP는 ISTJ의 질서를 깨뜨릴 수 있어요."},
            {"type": "ENTP 🚀", "reason": "논리보다 아이디어를 중시하는 ENTP와는 자주 충돌해요."},
        ],
    },
    "ISFJ": {
        "best": [
            {"type": "ESFP 🎉", "reason": "외향적이고 활발한 ESFP가 ISFJ의 내향적인 면을 끌어내줘요."},
            {"type": "ESTP ⚡", "reason": "적극적인 ESTP가 소극적인 ISFJ에게 힘을 줘요."},
        ],
        "worst": [
            {"type": "ENTP 🚀", "reason": "계속 변화하는 ENTP는 안정적인 ISFJ를 불안하게 만들 수 있어요."},
            {"type": "ENFP 🌈", "reason": "즉흥적인 ENFP와 신중한 ISFJ는 생활 리듬이 달라요."},
        ],
    },
    "ESTJ": {
        "best": [
            {"type": "ISTP 🔧", "reason": "실용적인 ISTP와 ESTJ의 추진력이 잘 맞아요."},
            {"type": "ESTP 🏅", "reason": "활동적인 ESTP와 ESTJ는 함께 성과를 만들어가요."},
        ],
        "worst": [
            {"type": "INFP ✒️", "reason": "감성적인 INFP는 규율적인 ESTJ를 부담스러워할 수 있어요."},
            {"type": "ENFP 🌈", "reason": "자유로운 ENFP는 ESTJ의 계획적인 성향과 충돌할 수 있어요."},
        ],
    },
    "ESFJ": {
        "best": [
            {"type": "ISFP 🎨", "reason": "예술적인 ISFP와 따뜻한 ESFJ는 서로를 존중해요."},
            {"type": "ESFP 🎭", "reason": "활발한 ESFP와 ESFJ는 함께 있을 때 에너지가 넘쳐요."},
        ],
        "worst": [
            {"type": "INTP 💻", "reason": "논리적인 INTP는 감성적인 ESFJ와 대화가 잘 안 맞을 수 있어요."},
            {"type": "ENTP 🚀", "reason": "즉흥적인 ENTP와 계획적인 ESFJ는 마찰이 생길 수 있어요."},
        ],
    },
    "ISTP": {
        "best": [
            {"type": "ESTJ 📅", "reason": "현실적인 ESTJ와 ISTP의 유연함이 잘 조화를 이뤄요."},
            {"type": "ENTJ 👔", "reason": "리더십 강한 ENTJ와 실용적인 ISTP는 강력한 팀이 돼요."},
        ],
        "worst": [
            {"type": "INFJ ✨", "reason": "깊은 교감을 원하는 INFJ는 감정을 잘 드러내지 않는 ISTP와 맞지 않아요."},
            {"type": "ENFJ 👨‍🏫", "reason": "지나치게 이끌려는 ENFJ는 독립적인 ISTP에게 부담이 될 수 있어요."},
        ],
    },
    "ISFP": {
        "best": [
            {"type": "ESFJ 👩‍🏫", "reason": "사교적인 ESFJ가 ISFP의 내향적인 성격을 보완해줘요."},
            {"type": "ENFJ 👨‍🏫", "reason": "따뜻한 ENFJ는 예술적인 ISFP를 격려해줘요."},
        ],
        "worst": [
            {"type": "INTJ 🧠", "reason": "계획적인 INTJ와 즉흥적인 ISFP는 생활 방식이 달라요."},
            {"type": "ENTJ 👔", "reason": "리더십 강한 ENTJ와 자유로운 ISFP는 자주 부딪힐 수 있어요."},
        ],
    },
    "ESTP": {
        "best": [
            {"type": "ISTJ 📚", "reason": "철저한 ISTJ와 활동적인 ESTP는 균형을 잘 맞춰요."},
            {"type": "ESTJ 📅", "reason": "실행력 강한 ESTJ와 ESTP는 함께 큰 성과를 낼 수 있어요."},
        ],
        "worst": [
            {"type": "INFJ ✨", "reason": "신중한 INFJ는 즉흥적인 ESTP를 불안하게 느낄 수 있어요."},
            {"type": "INFP ✒️", "reason": "감성적인 INFP는 현실적인 ESTP와 자주 충돌할 수 있어요."},
        ],
    },
    "ESFP": {
        "best": [
            {"type": "ISFJ 🤝", "reason": "배려심 깊은 ISFJ와 즐거운 ESFP는 좋은 조화를 이뤄요."},
            {"type": "ESFJ 👩‍🏫", "reason": "외향적인 둘은 언제나 에너지가 넘쳐요."},
        ],
        "worst": [
            {"type": "INTJ 🧠", "reason": "계획적인 INTJ는 자유로운 ESFP를 이해하기 어려워해요."},
            {"type": "INTP 💻", "reason": "내향적이고 분석적인 INTP와는 대화 리듬이 잘 맞지 않을 수 있어요."},
        ],
    },
    "ENTJ": {
        "best": [
            {"type": "ENTP 🚀", "reason": "에너지 넘치는 ENTP와 ENTJ의 추진력은 강력한 팀을 만들어요."},
            {"type": "INTP 💻", "reason": "논리적인 INTP가 ENTJ의 리더십을 뒷받침해줘요."},
        ],
        "worst": [
            {"type": "ISFP 🎨", "reason": "즉흥적인 ISFP는 계획적인 ENTJ와 충돌할 수 있어요."},
            {"type": "INFP ✒️", "reason": "감성적인 INFP는 현실적이고 단호한 ENTJ와 맞지 않아요."},
        ],
    },
    "INTP": {
        "best": [
            {"type": "ENTJ 👔", "reason": "강력한 리더 ENTJ와 분석적인 INTP는 서로를 보완해요."},
            {"type": "ENTP 🚀", "reason": "호기심 많은 ENTP와 INTP는 끊임없이 아이디어를 발전시켜요."},
        ],
        "worst": [
            {"type": "ESFJ 👩‍🏫", "reason": "감정적인 ESFJ와 논리적인 INTP는 대화가 자주 어긋나요."},
            {"type": "ESFP 🎭", "reason": "즉흥적인 ESFP는 깊이 파고드는 INTP와 리듬이 맞지 않아요."},
        ],
    },
    "INFP": {
        "best": [
            {"type": "ENFJ 👨‍🏫", "reason": "따뜻한 ENFJ가 INFP의 섬세함을 잘 이해해줘요."},
            {"type": "ENTJ 👔", "reason": "현실적인 ENTJ가 INFP의 이상을 실현할 수 있게 도와줘요."},
        ],
        "worst": [
            {"type": "ESTJ 📅", "reason": "규율적인 ESTJ는 자유로운 INFP를 답답하게 할 수 있어요."},
            {"type": "ESTP 🏅", "reason": "즉흥적인 ESTP와 감성적인 INFP는 자주 엇갈릴 수 있어요."},
        ],
    },
    "ENFJ": {
        "best": [
            {"type": "INFP ✒️", "reason": "이상적인 INFP와 따뜻한 ENFJ는 깊은 유대감을 형성해요."},
            {"type": "ISFP 🎨", "reason": "예술적인 ISFP와 ENFJ는 서로의 감정을 존중해요."},
        ],
        "worst": [
            {"type": "ISTP 🔧", "reason": "독립적인 ISTP는 지나치게 이끌려는 ENFJ를 부담스러워할 수 있어요."},
            {"type": "ESTP ⚡", "reason": "즉흥적인 ESTP와 계획적인 ENFJ는 자주 충돌할 수 있어요."},
        ],
    },
}

# --- MBTI 선택 ---
mbti_list = list(mbti_match.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요", mbti_list)

# --- 결과 출력 ---
if selected_mbti:
    st.markdown(f"## 🌟 {selected_mbti}의 궁합 결과 🌟")

    best = mbti_match[selected_mbti]["best"]
    worst = mbti_match[selected_mbti]["worst"]

    st.success("💖 잘 맞는 MBTI")
    for b in best:
        st.write(f"✅ {b['type']}")
        st.caption(f"👉 {b['reason']}")

    st.error("⚡ 맞지 않는 MBTI")
    for w in worst:
        st.write(f"❌ {w['type']}")
        st.caption(f"👉 {w['reason']}")

    st.markdown("---")
    st.info("💡 MBTI 궁합은 재미로만 참고하세요! 실제 인간관계는 이해와 존중이 더 중요해요 🤗")
