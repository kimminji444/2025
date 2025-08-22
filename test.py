# 파일명 예시: app.py
# 사용법: 터미널에서 `streamlit run app.py`

import streamlit as st
from difflib import get_close_matches

st.set_page_config(page_title="질병·증상 검색 도우미", page_icon="🩺", layout="wide")

# ─────────────────────────────────────────────────────────────
# 1) 간단한 데이터베이스 (예시)
#    - 실제 서비스라면 신뢰할 수 있는 의학 데이터 소스와 연동하세요.
#    - 여기서는 교육/발표용으로 아주 기초적인 정보만 담았습니다.
# ─────────────────────────────────────────────────────────────
DB = [
    {
        "name": "감기 (상기도 감염)",
        "symptoms": ["콧물", "코막힘", "재채기", "기침", "인후통", "미열", "몸살"],
        "about": "바이러스에 의한 상기도 감염으로 보통 7~10일 내 호전됩니다.",
        "care": ["수분 섭취", "휴식", "해열진통제(필요시)", "생리식염수 비강세척"],
        "doctor_when": ["고열이 3일 이상 지속", "호흡곤란", "의식저하 또는 심한 탈수"],
        "treat": "대개 대증치료(증상 완화). 항생제는 보통 필요하지 않습니다.",
        "tags": ["감기", "코감기", "상기도 감염"],
    },
    {
        "name": "독감 (인플루엔자)",
        "symptoms": ["고열", "오한", "근육통", "두통", "마른기침", "피로"],
        "about": "인플루엔자 바이러스 감염. 갑작스러운 고열과 전신통이 특징입니다.",
        "care": ["해열진통제", "수분/휴식", "초기(48시간 이내) 항바이러스제 고려"],
        "doctor_when": ["호흡곤란", "의식저하", "기저질환 악화", "영유아·고령·임신 중"],
        "treat": "증상 시작 48시간 이내 항바이러스제 투여를 고려할 수 있습니다.",
        "tags": ["독감", "인플루엔자"],
    },
    {
        "name": "편도염",
        "symptoms": ["인후통", "삼킴통", "고열", "편도 비대", "목 쉼"],
        "about": "바이러스 또는 세균에 의해 편도가 염증을 일으킨 상태입니다.",
        "care": ["수분/휴식", "진통해열제", "꿀물·따뜻한 음료"],
        "doctor_when": ["호흡곤란", "3일 이상 고열", "연하곤란으로 탈수 의심"],
        "treat": "세균성 의심 시 항생제. 재발 잦고 중증이면 수술 고려.",
        "tags": ["편도선염", "목감기"],
    },
    {
        "name": "위장관염 (장염)",
        "symptoms": ["복통", "설사", "구토", "메스꺼움", "발열"],
        "about": "바이러스/세균/기생충 등으로 위장관에 염증이 생긴 상태.",
        "care": ["수분·전해질 보충", "기름진 음식 피하기", "휴식"],
        "doctor_when": ["혈변", "심한 탈수(어지럼, 소변 감소)", "고열 지속", "영유아·노약자"],
        "treat": "원인에 따라 대증요법, 필요 시 지사제/항생제/항구토제.",
        "tags": ["장염", "식중독"],
    },
    {
        "name": "편두통",
        "symptoms": ["박동성 두통", "오심", "구토", "광과민", "소리 과민", "전조(오라)"],
        "about": "반복되는 중등도~중증의 박동성 두통. 빛/소리에 민감해질 수 있습니다.",
        "care": ["조용하고 어두운 곳에서 휴식", "수분 섭취", "카페인 소량(일부 도움)"],
        "doctor_when": ["갑자기 번개처럼 심한 두통", "신경학적 증상 동반", "발열·목경직 동반"],
        "treat": "진통제, 트립탄계 약물 등. 예방약물은 빈도·중증도에 따라 고려.",
        "tags": ["편두통", "편두통 전조"],
    },
    {
        "name": "천식",
        "symptoms": ["쌕쌕거림", "기침", "숨참", "흉부 압박감", "야간/새벽 악화"],
        "about": "기도의 만성 염증으로 가역적 기도폐쇄가 반복되는 질환입니다.",
        "care": ["유발요인 회피", "흡입제 정기 사용(의사 처방)", "증상일지 기록"],
        "doctor_when": ["말이 끊기는 심한 숨참", "청색증", "구조 호흡 필요"],
        "treat": "흡입형 스테로이드, 기관지확장제 등 개인 맞춤 치료가 필요.",
        "tags": ["기관지 천식", "알레르기성 천식"],
    },
    {
        "name": "알레르기 비염",
        "symptoms": ["재채기", "가려운 콧속", "맑은 콧물", "코막힘", "눈 가려움/눈물"],
        "about": "특정 알레르겐에 대한 과민반응으로 코 점막에 염증이 생깁니다.",
        "care": ["알레르겐 회피", "생리식염수 세척", "실내 공기 관리"],
        "doctor_when": ["천식 증상 동반", "만성 부비동염 의심", "일상생활 지장"],
        "treat": "항히스타민제, 비강 스테로이드 스프레이, 면역치료(선별적).",
        "tags": ["비염", "꽃가루 알레르기"],
    },
    {
        "name": "당뇨병 (제2형)",
        "symptoms": ["다뇨", "다갈", "다식", "피로", "체중변화", "상처 회복 지연"],
        "about": "인슐린 저항성/분비저하로 혈당이 만성적으로 상승하는 대사질환.",
        "care": ["식이·운동요법", "체중 관리", "혈당 자가측정"],
        "doctor_when": ["저혈당 증상", "혈당 조절 불가", "시력 저하·피부감염"],
        "treat": "경구혈당강하제/인슐린 등. 정기적 의료진 상담 필수.",
        "tags": ["당뇨", "제2형 당뇨"],
    },
    {
        "name": "고혈압",
        "symptoms": ["무증상", "두통", "어지럼", "흉통", "호흡곤란"],
        "about": "지속적으로 높은 혈압 상태. 합병증 예방을 위한 관리가 중요합니다.",
        "care": ["염분 제한", "운동", "체중·스트레스 관리", "금연"],
        "doctor_when": ["수축기 ≥180 또는 이완기 ≥120mmHg", "신경학적 증상 동반"],
        "treat": "생활습관 교정 + 항고혈압제(의사 처방).",
        "tags": ["혈압", "고혈압증"],
    },
    {
        "name": "심근경색",
        "symptoms": ["가슴 통증(압박감)", "좌측 팔·턱 방사통", "식은땀", "호흡곤란", "구역"],
        "about": "심장혈관이 막혀 심근이 괴사하는 응급질환입니다.",
        "care": ["즉시 119/응급실", "움직임 최소화"],
        "doctor_when": ["의심되면 지체 없이 응급실"],
        "treat": "응급 재관류 치료(스텐트/용해제) 등 병원 치료가 필요.",
        "tags": ["심장마비", "심근경색증"],
    },
]

# ─────────────────────────────────────────────────────────────
# 2) 문자열 전처리 & 간단 매칭 함수
#    - 병명 검색: 철자 유사도(가까운 철자) + 태그 포함
#    - 증상 검색: 입력 문장에 포함된 증상 키워드가 몇 개 일치하는지 점수화
# ─────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    return text.strip().lower()

# 증상 키워드 사전(간단)
ALL_SYMPTOMS = sorted({s for item in DB for s in item["symptoms"]})

# 병명/태그 인덱스
NAME_INDEX = {normalize(tag): i for i, item in enumerate(DB) for tag in [item["name"], *item["tags"]]}


def search_by_disease_name(query: str, topk: int = 5):
    if not query:
        return []
    q = normalize(query)
    # 1) 정확/부분 일치 우선
    direct_hits = [idx for key, idx in NAME_INDEX.items() if q in key]
    # 2) 철자 유사도(가까운 철자)
    close = get_close_matches(q, list(NAME_INDEX.keys()), n=topk, cutoff=0.6)
    close_hits = [NAME_INDEX[c] for c in close]
    hits = list(dict.fromkeys([*direct_hits, *close_hits]))  # 중복 제거/순서 유지
    return [DB[i] for i in hits][:topk]


def search_by_symptoms(text: str, topk: int = 5):
    if not text:
        return []
    q_tokens = [normalize(t) for t in text.replace(",", " ").split()]
    # 입력 문장에서 DB 증상 키워드가 몇 개 포함되는지 스코어링
    scores = []
    for item in DB:
        match_cnt = 0
        for s in item["symptoms"]:
            if normalize(s) in q_tokens or any(normalize(s) in tok for tok in q_tokens):
                match_cnt += 1
        scores.append((match_cnt, item))
    scores.sort(key=lambda x: (-x[0], x[1]["name"]))
    # 매칭이 0개인 항목은 제외
    return [it for cnt, it in scores if cnt > 0][:topk]

# ─────────────────────────────────────────────────────────────
# 3) UI 구성
# ─────────────────────────────────────────────────────────────

st.title("🩺 질병·증상 검색 도우미")

with st.expander("중요 안내 (의학적 조언 아님)", expanded=True):
    st.warning(
        """
        • 이 앱은 **교육 및 정보 제공 목적**으로 제작되었습니다. 실제 진단/치료는 의료 전문가의 진료가 필요합니다.\n
        • **가슴 통증, 호흡곤란, 의식저하, 청색증, 신경학적 증상** 등 응급 증상이 있으면 즉시 119 또는 가까운 응급실로 가세요.
        """
    )

left, right = st.columns([2, 1])
with left:
    st.subheader("검색 입력")
    mode = st.radio("검색 방법", ["증상으로 검색", "질병명으로 검색"], horizontal=True)

    if mode == "증상으로 검색":
        text = st.text_area("증상(또는 키워드)을 입력하세요", placeholder="예: 고열 오한 근육통 마른기침")
        if st.button("검색", use_container_width=True):
            results = search_by_symptoms(text)
            if not results:
                st.info("관련 결과가 없어요. 증상을 2~3개 이상 입력해 보세요.")
            for item in results:
                with st.container(border=True):
                    st.markdown(f"### {item['name']}")
                    st.caption("가능성 있는 관련 항목")
                    st.markdown(f"**주요 증상:** {', '.join(item['symptoms'])}")
                    st.markdown(f"**설명:** {item['about']}")
                    st.markdown(f"**자가관리:** {', '.join(item['care'])}")
                    st.markdown(f"**치료(의료진):** {item['treat']}")
                    st.markdown(f"**다음과 같으면 진료 필요:** {', '.join(item['doctor_when'])}")
    else:
        query = st.text_input("질병명(또는 별칭/태그)", placeholder="예: 독감, 장염, 천식…")
        if st.button("검색", use_container_width=True):
            results = search_by_disease_name(query)
            if not results:
                st.info("관련 결과가 없어요. 다른 이름(별칭)으로도 시도해 보세요.")
            for item in results:
                with st.container(border=True):
                    st.markdown(f"### {item['name']}")
                    st.caption("연관 항목")
                    st.markdown(f"**주요 증상:** {', '.join(item['symptoms'])}")
                    st.markdown(f"**설명:** {item['about']}")
                    st.markdown(f"**자가관리:** {', '.join(item['care'])}")
                    st.markdown(f"**치료(의료진):** {item['treat']}")
                    st.markdown(f"**다음과 같으면 진료 필요:** {', '.join(item['doctor_when'])}")

with right:
    st.subheader("도움말")
    st.markdown(
        """
        - **증상으로 검색**: 고열, 기침, 복통 같은 단어를 **공백으로 구분**해 적어보세요.\n
        - **질병명으로 검색**: '장염', '편도염', '독감' 같은 **일반명/별칭**도 됩니다.\n
        - 결과는 **유사 증상 수**나 **철자 유사도**를 바탕으로 정렬됩니다.\n
        - 발표 팁: 데이터는 파이썬 리스트(DB)로 관리 → 실제 서비스에서는 **공식 의학 데이터**와 연동하면 확장 가능하다고 설명하세요.
        """
    )

st.divider()

st.caption("© 교육·발표용 샘플. 의학적 판단은 반드시 의료 전문가와 상의하세요.")

