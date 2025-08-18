import streamlit as st
from typing import List, Dict

# ───────────────────── 페이지 설정 ─────────────────────
st.set_page_config(page_title="MBTI ✕ 장르 노래 추천", page_icon="🎵", layout="wide")

st.markdown(
    """
    <style>
    .tag{display:inline-block;padding:4px 10px;margin:2px;border-radius:999px;
         font-size:12px;border:1px solid rgba(255,255,255,0.2);background:rgba(255,255,255,0.06)}
    .card{padding:14px;border-radius:16px;background:rgba(255,255,255,0.06);
         border:1px solid rgba(255,255,255,0.15);box-shadow:0 6px 24px rgba(0,0,0,0.08)}
    .muted{opacity:.8}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎧 MBTI × 장르 맞춤 노래 추천")
st.caption("당신의 MBTI와 듣고 싶은 장르를 선택하면, 무드/에너지/분위기 태그를 기반으로 노래를 추천해드려요. 🔮")

# ───────────────────── MBTI 성향 프로필 ─────────────────────
# 각 MBTI가 선호하는 태그(무드/에너지/보컬/분위기)를 대략적으로 설정
mbti_profile: Dict[str, Dict[str, List[str]]] = {
    # NT(분석/전략)
    "INTJ": {"prefer":["focus","dark","atmospheric","instrumental","deep","modern","low","mid"],
             "avoid":["party","anthem"]},
    "INTP": {"prefer":["focus","chill","experimental","instrumental","deep","low","mid"],
             "avoid":["anthem","romantic"]},
    "ENTJ": {"prefer":["anthem","high","modern","power","bold","lyrical","motivational","clean"],
             "avoid":["sleep","lofi"]},
    "ENTP": {"prefer":["experimental","upbeat","high","modern","playful","bold","lyrical"],
             "avoid":["sleep","dark"]},
    # NF(감성/이상)
    "INFJ": {"prefer":["emotional","warm","deep","introspective","mid","low","lyrical","dreamy"],
             "avoid":["aggressive"]},
    "INFP": {"prefer":["emotional","poetic","warm","introspective","low","mid","lyrical"],
             "avoid":["aggressive","anthem"]},
    "ENFJ": {"prefer":["uplifting","warm","anthem","mid","high","lyrical","romantic"],
             "avoid":["dark","aggressive"]},
    "ENFP": {"prefer":["upbeat","colorful","playful","high","modern","lyrical"],
             "avoid":["monotone","sleep"]},
    # SJ(체계/안정)
    "ISTJ": {"prefer":["classic","clean","mid","steady","lyrical","structured"],
             "avoid":["chaotic","experimental"]},
    "ISFJ": {"prefer":["warm","comfort","classic","mid","low","lyrical","romantic"],
             "avoid":["aggressive","chaotic"]},
    "ESTJ": {"prefer":["anthem","clean","high","motivational","classic","structured"],
             "avoid":["sleep","mellow"]},
    "ESFJ": {"prefer":["warm","romantic","singalong","mid","high","lyrical"],
             "avoid":["dark","aggressive"]},
    # SP(즉흥/감각)
    "ISTP": {"prefer":["groove","bass","clean","mid","high","experimental"],
             "avoid":["sappy","slow"]},
    "ISFP": {"prefer":["aesthetic","warm","chill","mid","lyrical","romantic"],
             "avoid":["aggressive","anthem"]},
    "ESTP": {"prefer":["party","bass","high","bold","anthem","modern"],
             "avoid":["sleep","slow"]},
    "ESFP": {"prefer":["dance","trend","upbeat","party","high","colorful","singalong"],
             "avoid":["dark","sleep"]},
}

# ───────────────────── 장르별 곡 데이터 ─────────────────────
# 각 곡: title, artist, tags, (선택) 링크
catalog: Dict[str, List[Dict]] = {
    "K-Pop": [
        {"title":"Dynamite","artist":"BTS","tags":["upbeat","dance","party","high","modern","singalong"],"link":"https://youtu.be/gdZLi9oWNZg"},
        {"title":"How You Like That","artist":"BLACKPINK","tags":["bold","dance","high","party","modern"],"link":"https://youtu.be/ioNng23DkIM"},
        {"title":"Super Shy","artist":"NewJeans","tags":["colorful","trendy","mid","dance","modern"],"link":"https://youtu.be/ArmDp-zijuc"},
        {"title":"Love Poem","artist":"IU","tags":["emotional","warm","lyrical","low","romantic"],"link":"https://youtu.be/8ZqVx2Z3V0s"},
        {"title":"Hype Boy","artist":"NewJeans","tags":["upbeat","dance","trend","mid","modern"],"link":"https://youtu.be/11cta61wi0g"},
        {"title":"Queencard","artist":"(G)I-DLE","tags":["playful","upbeat","party","high","singalong"],"link":"https://youtu.be/6ZUIwj3FgUY"},
    ],
    "Pop": [
        {"title":"Blinding Lights","artist":"The Weeknd","tags":["anthem","retro","high","modern","singalong"],"link":"https://youtu.be/fHI8X4OXluQ"},
        {"title":"As It Was","artist":"Harry Styles","tags":["warm","mid","nostalgic","lyrical"],"link":"https://youtu.be/H5v3kku4y6Q"},
        {"title":"Levitating","artist":"Dua Lipa","tags":["dance","upbeat","party","high","modern"],"link":"https://youtu.be/TUVcZfQe-Kw"},
        {"title":"drivers license","artist":"Olivia Rodrigo","tags":["emotional","introspective","low","lyrical"],"link":"https://youtu.be/ZmDBbnmKpqQ"},
        {"title":"Shape of You","artist":"Ed Sheeran","tags":["groove","mid","singalong","modern"],"link":"https://youtu.be/JGwWNGJdvx8"},
        {"title":"bad guy","artist":"Billie Eilish","tags":["dark","bass","modern","mid"],"link":"https://youtu.be/DyDfgMOUjCI"},
    ],
    "Hip-Hop": [
        {"title":"HUMBLE.","artist":"Kendrick Lamar","tags":["bold","lyrical","high","modern"],"link":"https://youtu.be/tvTRZJ-4EyI"},
        {"title":"God's Plan","artist":"Drake","tags":["warm","anthem","mid","modern"],"link":"https://youtu.be/xpVfcZ0ZcFM"},
        {"title":"SICKO MODE","artist":"Travis Scott","tags":["experimental","bass","high","modern"],"link":"https://youtu.be/6ONRf7h3Mdk"},
        {"title":"Lose Yourself","artist":"Eminem","tags":["anthem","motivational","high","classic"],"link":"https://youtu.be/_Yhyp-_hX2s"},
        {"title":"Stronger","artist":"Kanye West","tags":["electro","anthem","high","modern"],"link":"https://youtu.be/PsO6ZnUZI0g"},
        {"title":"No Role Modelz","artist":"J. Cole","tags":["lyrical","mid","classic"],"link":"https://youtu.be/wJGcwEv7838"},
    ],
    "R&B/Soul": [
        {"title":"Snooze","artist":"SZA","tags":["emotional","warm","mid","modern","lyrical"],"link":"https://youtu.be/rM4WstLY4H8"},
        {"title":"Thinkin Bout You","artist":"Frank Ocean","tags":["introspective","low","dreamy","lyrical"],"link":"https://youtu.be/PmSjk8dF9LM"},
        {"title":"Best Part","artist":"Daniel Caesar, H.E.R.","tags":["romantic","warm","low","lyrical"],"link":"https://youtu.be/vBy7FaapGRo"},
        {"title":"Get You","artist":"Daniel Caesar","tags":["romantic","low","warm","lyrical"],"link":"https://youtu.be/uQFVqltOXRg"},
        {"title":"No One","artist":"Alicia Keys","tags":["uplifting","anthem","mid","classic"],"link":"https://youtu.be/rywUS-ohqeE"},
        {"title":"Call Out My Name","artist":"The Weeknd","tags":["emotional","dark","mid","lyrical"],"link":"https://youtu.be/MZ4JGye4dQU"},
    ],
    "Rock/Alt": [
        {"title":"Believer","artist":"Imagine Dragons","tags":["anthem","high","motivational","modern"],"link":"https://youtu.be/7wtfhZwyrcc"},
        {"title":"Do I Wanna Know?","artist":"Arctic Monkeys","tags":["dark","groove","mid","modern"],"link":"https://youtu.be/bpOSxM0rNPM"},
        {"title":"Numb","artist":"Linkin Park","tags":["emotional","anthem","high","classic"],"link":"https://youtu.be/kXYiU_JCYtU"},
        {"title":"Californication","artist":"Red Hot Chili Peppers","tags":["nostalgic","mid","classic"],"link":"https://youtu.be/YlUKcNNmywk"},
        {"title":"Smells Like Teen Spirit","artist":"Nirvana","tags":["bold","high","classic"],"link":"https://youtu.be/hTWKbfoikeg"},
        {"title":"Don't Stop Me Now","artist":"Queen","tags":["uplifting","high","singalong","classic"],"link":"https://youtu.be/HgzGwKwLmgM"},
    ],
    "Indie/Alt": [
        {"title":"The Less I Know The Better","artist":"Tame Impala","tags":["dreamy","groove","mid","modern"],"link":"https://youtu.be/sBzrzS1Ag_g"},
        {"title":"Motion Sickness","artist":"Phoebe Bridgers","tags":["introspective","lyrical","mid","modern"],"link":"https://youtu.be/lM5q4N9UEI8"},
        {"title":"Somebody Else","artist":"The 1975","tags":["dreamy","emotional","mid","modern"],"link":"https://youtu.be/B19r1jZ-1qs"},
        {"title":"Holocene","artist":"Bon Iver","tags":["poetic","low","introspective","warm"],"link":"https://youtu.be/tJ6i8r8qrXk"},
        {"title":"Chamber of Reflection","artist":"Mac DeMarco","tags":["chill","retro","low","dreamy"],"link":"https://youtu.be/6KqukG3j7Qw"},
        {"title":"Summertime Sadness","artist":"Lana Del Rey","tags":["emotional","dreamy","mid","lyrical"],"link":"https://youtu.be/TdrL3QxjyVw"},
    ],
    "EDM": [
        {"title":"Wake Me Up","artist":"Avicii","tags":["uplifting","anthem","high","singalong","modern"],"link":"https://youtu.be/IcrbM1l_BoI"},
        {"title":"Animals","artist":"Martin Garrix","tags":["party","bass","high","instrumental","modern"],"link":"https://youtu.be/gCYcHz2k5x0"},
        {"title":"Clarity","artist":"Zedd ft. Foxes","tags":["emotional","anthem","high","modern"],"link":"https://youtu.be/IxxstCcJlsc"},
        {"title":"Firestone","artist":"Kygo ft. Conrad","tags":["warm","dreamy","mid","modern"],"link":"https://youtu.be/9Sc-ir2UwGU"},
        {"title":"Alone","artist":"Marshmello","tags":["uplifting","party","high","modern"],"link":"https://youtu.be/ALZHF5UqnU4"},
        {"title":"Summer","artist":"Calvin Harris","tags":["upbeat","party","high","modern"],"link":"https://youtu.be/ebXbLfLACGM"},
    ],
    "Lo-fi/Study": [
        {"title":"snowfall","artist":"idealism","tags":["lofi","focus","low","instrumental","chill"],"link":"https://youtu.be/Qd01-8sTg0o"},
        {"title":"affection","artist":"jinsang","tags":["lofi","focus","low","instrumental","warm"],"link":"https://youtu.be/HlL9r6hF8O0"},
        {"title":"just friends","artist":"potsu","tags":["lofi","chill","low","instrumental"],"link":"https://youtu.be/9O9uB6jVWeo"},
        {"title":"by the pool","artist":"eevee","tags":["lofi","chill","low","instrumental","dreamy"],"link":"https://youtu.be/2Vv-BfVoq4g?t=1"},
        {"title":"first love","artist":"eevee","tags":["lofi","warm","low","instrumental"],"link":"https://youtu.be/0b0Z2h6Q5No"},
        {"title":"luv nyc","artist":"potsu","tags":["lofi","focus","low","instrumental"],"link":"https://youtu.be/mhC8h8Jtfsw"},
    ],
    "Ballad/OST": [
        {"title":"All of Me","artist":"John Legend","tags":["romantic","warm","low","lyrical"],"link":"https://youtu.be/450p7goxZqg"},
        {"title":"When We Were Young","artist":"Adele","tags":["emotional","anthem","mid","lyrical"],"link":"https://youtu.be/DDWKuo3gXMQ"},
        {"title":"City of Stars","artist":"La La Land OST","tags":["romantic","poetic","low","classic"],"link":"https://youtu.be/GTWqwSNQCcg"},
        {"title":"Speechless","artist":"Naomi Scott (Aladdin)","tags":["uplifting","anthem","mid","lyrical"],"link":"https://youtu.be/8Qn_spdM5Zg"},
        {"title":"Hold My Hand","artist":"Lady Gaga (Top Gun)","tags":["uplifting","anthem","mid","modern"],"link":"https://youtu.be/O2CIAKVTOrc"},
        {"title":"A Thousand Years","artist":"Christina Perri","tags":["romantic","warm","low","lyrical"],"link":"https://youtu.be/rtOvBOTyX00"},
    ],
}

ALL_MBTI = list(mbti_profile.keys())
ALL_GENRES = list(catalog.keys())

# ───────────────────── 사이드바 입력 ─────────────────────
with st.sidebar:
    st.header("🎛️ 설정")
    mbti = st.selectbox("당신의 MBTI를 선택하세요", ALL_MBTI, index=ALL_MBTI.index("ENFP") if "ENFP" in ALL_MBTI else 0)
    genre = st.selectbox("장르를 선택하세요", ALL_GENRES, index=ALL_GENRES.index("K-Pop") if "K-Pop" in ALL_GENRES else 0)
    top_k = st.slider("추천 개수", 3, 10, 6)
    st.caption("💡 *추천 로직*: MBTI 선호 태그와 곡 태그가 많이 겹칠수록 점수가 높아집니다.")

# ───────────────────── 추천 엔진 ─────────────────────
def score_song(mbti: str, tags: List[str]) -> int:
    prof = mbti_profile.get(mbti, {"prefer":[], "avoid":[]})
    score = 0
    for t in tags:
        if t in prof["prefer"]:
            score += 2
        if t in prof.get("avoid", []):
            score -= 2
    # 균형: 기본적으로 곡 태그가 다양하면(풍부함) 소폭 가점
    score += min(len(tags), 6) * 0.1
    return int(round(score))

def explain_match(mbti: str, tags: List[str]) -> str:
    pref = set(mbti_profile[mbti]["prefer"])
    avoid = set(mbti_profile[mbti]["avoid"])
    hits = [t for t in tags if t in pref]
    misses = [t for t in tags if t in avoid]
    chips_hit = " ".join([f"<span class='tag'>✅ {h}</span>" for h in hits]) or "<span class='tag'>—</span>"
    chips_miss = " ".join([f"<span class='tag'>⚠️ {m}</span>" for m in misses]) or "<span class='tag'>—</span>"
    return f"**매칭 태그** {chips_hit} &nbsp;&nbsp; **비선호 태그** {chips_miss}"

# ───────────────────── 결과 영역 ─────────────────────
st.subheader(f"🎵 추천 결과 — {mbti} × {genre}")
songs = catalog.get(genre, [])

# 점수 계산 및 정렬
ranked = []
for s in songs:
    s_score = score_song(mbti, s["tags"])
    ranked.append({**s, "score": s_score})
ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)[:top_k]

# 2열 카드 레이아웃
cols = st.columns(2)
for i, s in enumerate(ranked):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class='card'>
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <div style="font-size:18px;font-weight:700;">🎶 {s['title']}</div>
                        <div class="muted" style="margin-top:2px;">👤 {s['artist']}</div>
                    </div>
                    <div style="font-size:18px;font-weight:700;">⭐ {s['score']}</div>
                </div>
                <div style="margin-top:8px;">
                    {" ".join([f"<span class='tag'>#{t}</span>" for t in s["tags"]])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if s.get("link"):
            st.link_button("▶️ 유튜브에서 듣기", s["link"])

st.markdown("---")
# ─────────────── 매칭 설명 / 가이드 ───────────────
with st.expander("🧠 왜 이 곡들이 선택되었나요? (설명 펼치기)"):
    st.markdown(f"**{mbti}** 성향이 선호하는 태그: " + " ".join([f"<span class='tag'>💖 {t}</span>" for t in mbti_profile[mbti]["prefer"]]), unsafe_allow_html=True)
    st.markdown("회피 성향 태그: " + " ".join([f"<span class='tag'>🚫 {t}</span>" for t in mbti_profile[mbti]["avoid"]]), unsafe_allow_html=True)
    st.write("아래는 각 추천곡의 매칭 상세입니다.")
    for s in ranked:
        st.markdown(f"**🎶 {s['title']} — {s['artist']}**")
        st.markdown(explain_match(mbti, s["tags"]), unsafe_allow_html=True)

st.info("🔔 참고: 노래/태그는 예시 데이터이며 자유롭게 추가·수정할 수 있어요. MBTI는 재미 요소로 활용하고, 결국엔 당신이 좋아하는 음악이 최고! 🎈")
