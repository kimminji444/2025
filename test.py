import streamlit as st


# 증상으로 찾기: 입력 단어(공백 구분)와 DB의 증상 이름이 얼마나 겹치는지 간단히 세서 정렬


def search_by_symptoms(text: str):
tokens = [norm(t) for t in text.replace(",", " ").split() if t]
scored = []
for item in DB:
match_count = sum(1 for s in item["symptoms"] if norm(s) in tokens)
if match_count > 0:
scored.append((match_count, item))
scored.sort(key=lambda x: -x[0]) # 많이 겹칠수록 위로
return [it for _, it in scored]


# ===== ③ 화면 구성 =====
st.title("🩺 질병·증상 검색 (교육용)")
with st.expander("중요 안내", expanded=True):
st.warning("이 앱은 교육용입니다. 증상이 심하거나 걱정되면 의료진의 진료를 받으세요.")


mode = st.radio("검색 방법", ["증상으로 검색", "질병명으로 검색"], horizontal=True)


if mode == "증상으로 검색":
text = st.text_area("증상을 공백으로 구분해 적어주세요", placeholder="예: 고열 오한 근육통")
if st.button("검색"):
results = search_by_symptoms(text)
if not results:
st.info("결과가 없습니다. 증상을 2~3개 이상 적어보세요.")
for item in results:
st.subheader(item["name"]) # 병명
st.caption("가능성 있는 관련 정보")
st.write("**주요 증상:** ", ", ".join(item["symptoms"]))
st.write("**설명:** ", item["about"])
st.write("**자가관리:** ", ", ".join(item["care"]))
st.write("**치료(의사):** ", item["treat"])
st.write("**바로 진료가 필요한 경우:** ", ", ".join(item["emergency"]))
else:
q = st.text_input("질병명(또는 별칭)", placeholder="예: 독감, 장염, 천식")
if st.button("검색"):
results = search_by_name(q)
if not results:
st.info("결과가 없습니다. 다른 이름(별칭)으로 시도해 보세요.")
for item in results:
st.subheader(item["name"]) # 병명
st.caption("연관 항목")
st.write("**주요 증상:** ", ", ".join(item["symptoms"]))
st.write("**설명:** ", item["about"])
st.write("**자가관리:** ", ", ".join(item["care"]))
st.write("**치료(의사):** ", item["treat"])
st.write("**바로 진료가 필요한 경우:** ", ", ".join(item["emergency"]))


st.caption("© 교육·발표용 샘플. 실제 의학적 판단은 의료진과 상의하세요.")
