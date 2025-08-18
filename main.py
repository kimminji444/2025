import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="centered")
st.title("✨ MBTI 기반 진로 추천 프로그램 ✨")
st.markdown("당신의 성격 유형에 맞는 직업을 찾아보세요! 💼🚀")

# --- MBTI 직업 추천 데이터 ---
mbti_jobs = {
    "INTJ": [
        {"job": "데이터 과학자 📊", 
         "desc": "논리적이고 분석적인 사고로 데이터를 해석하고 미래를 예측하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/616/616489.png"},
        {"job": "전략 컨설턴트 🧠", 
         "desc": "복잡한 문제를 체계적으로 분석해 기업의 전략을 제시하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"},
    ],
    "ENTP": [
        {"job": "기업가 🚀", 
         "desc": "새로운 아이디어로 혁신적인 사업을 만들어가는 사람", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135692.png"},
        {"job": "마케팅 기획자 🎯", 
         "desc": "창의적인 아이디어로 시장을 분석하고 고객을 사로잡는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/2920/2920324.png"},
    ],
    "INFJ": [
        {"job": "상담사 💬", 
         "desc": "사람들의 고민을 공감하고 문제 해결을 돕는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/4333/4333609.png"},
        {"job": "작가 ✍️", 
         "desc": "깊은 통찰과 창의력을 바탕으로 글로 세상을 표현하는 사람", 
         "img": "https://cdn-icons-png.flaticon.com/512/3940/3940056.png"},
    ],
    "ENFP": [
        {"job": "크리에이티브 디렉터 🌈", 
         "desc": "예술적 감각과 자유로운 사고로 콘텐츠를 기획하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/1903/1903162.png"},
        {"job": "방송인 🎤", 
         "desc": "밝고 에너지 넘치는 모습으로 대중과 소통하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/921/921490.png"},
    ],
    "ISTJ": [
        {"job": "회계사 📚", 
         "desc": "철저한 원칙과 정확함으로 재무를 관리하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/4151/4151022.png"},
        {"job": "법률가 ⚖️", 
         "desc": "논리적 사고와 원칙을 바탕으로 정의를 실현하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/476/476863.png"},
    ],
    "ISFJ": [
        {"job": "간호사 🏥", 
         "desc": "세심한 배려와 헌신으로 환자의 건강을 돌보는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/2922/2922561.png"},
        {"job": "교사 👩‍🏫", 
         "desc": "학생들을 가르치고 성장하도록 돕는 교육 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135773.png"},
    ],
    "ESTJ": [
        {"job": "프로젝트 매니저 📅", 
         "desc": "체계적인 관리 능력으로 목표를 달성하도록 이끄는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/1026/1026470.png"},
        {"job": "군 장교 🎖️", 
         "desc": "리더십과 조직력을 발휘해 대규모 팀을 이끄는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"},
    ],
    "ESFJ": [
        {"job": "사회복지사 🤝", 
         "desc": "사람들의 삶을 향상시키고 도움을 주는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/1971/1971290.png"},
        {"job": "인사담당자 👔", 
         "desc": "사람을 잘 이해하고 조직을 조율하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/1256/1256650.png"},
    ],
    "ISTP": [
        {"job": "엔지니어 🔧", 
         "desc": "기술적 문제를 해결하고 새로운 시스템을 설계하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/2721/2721297.png"},
        {"job": "파일럿 ✈️", 
         "desc": "모험심과 집중력을 발휘해 하늘을 나는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/1086/1086933.png"},
    ],
    "ISFP": [
        {"job": "아티스트 🎨", 
         "desc": "자유로운 영감과 감성을 작품으로 표현하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/4333/4333604.png"},
        {"job": "사진작가 📷", 
         "desc": "세상을 새로운 시각으로 포착하는 창의적인 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/2920/2920044.png"},
    ],
    "ESTP": [
        {"job": "기업 세일즈맨 💼", 
         "desc": "빠른 판단력과 추진력으로 비즈니스를 성사시키는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135692.png"},
        {"job": "스포츠 선수 🏅", 
         "desc": "열정과 도전 정신으로 경쟁하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"},
    ],
    "ESFP": [
        {"job": "배우 🎭", 
         "desc": "무대와 스크린에서 다양한 감정을 표현하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/921/921071.png"},
        {"job": "이벤트 기획자 🎉", 
         "desc": "사람들에게 즐거운 경험을 선사하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/2871/2871847.png"},
    ],
    "ENTJ": [
        {"job": "CEO 👔", 
         "desc": "강력한 리더십으로 회사를 이끄는 최고 경영자", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135792.png"},
        {"job": "전략 기획자 📈", 
         "desc": "큰 그림을 보고 미래를 설계하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/2490/2490400.png"},
    ],
    "INTP": [
        {"job": "연구원 🔬", 
         "desc": "논리적 탐구로 새로운 지식을 발견하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/2721/2721297.png"},
        {"job": "소프트웨어 개발자 💻", 
         "desc": "창의적 사고로 새로운 프로그램을 만들어내는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/1197/1197460.png"},
    ],
    "INFP": [
        {"job": "심리학자 🧘", 
         "desc": "사람의 내면을 깊이 이해하고 연구하는 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/2920/2920204.png"},
        {"job": "시인 ✒️", 
         "desc": "섬세한 감성과 언어로 마음을 표현하는 직업", 
         "img": "https://cdn-icons-png.flaticon.com/512/1256/1256657.png"},
    ],
    "ENFJ": [
        {"job": "강사 👨‍🏫", 
         "desc": "사람들을 이끌고 영감을 주는 교육 전문가", 
         "img": "https://cdn-icons-png.flaticon.com/512/3135/3135773.png"},
        {"job": "인권운동가 ✊", 
         "desc": "사회 정의와 변화를 위해 행동하는 사람", 
         "img": "https://cdn-icons-png.flaticon.com/512/2950/2950648.png"},
    ],
}

# --- MBTI 선택 ---
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요", mbti_list)

# --- 결과 출력 ---
if selected_mbti:
    st.markdown(f"## 🌟 {selected_mbti} 유형 추천 직업 🌟")
    
    for job_info in mbti_jobs[selected_mbti]:
        st.subheader(job_info["job"])
        st.write(job_info["desc"])
        st.image(job_info["img"], width=120)

    st.markdown("---")
    st.info("🔮 MBTI는 참고용일 뿐! 진짜 진로는 당신의 열정과 경험이 결정해요 💖")
