import streamlit as st
from auth import login
from quiz import run_quiz
from utils import analyze_result, get_result_detail
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="나의 행동 패턴 분석기",
    page_icon="💣",
    layout="centered"
)

# CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0e1117, #1c1f26);
    color: white;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    animation: fadeInDown 1s ease-in-out;
}

.card {
    padding:20px;
    border-radius:20px;
    background:#1c1f26;
    margin-bottom:15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
}

.stButton>button {
    background: linear-gradient(45deg, #ff4b2b, #ff416c);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.1);
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
}

.metric-box {
    animation: popIn 0.6s ease;
}

@keyframes fadeInDown {
    from { opacity:0; transform: translateY(-20px); }
    to { opacity:1; transform: translateY(0); }
}

@keyframes popIn {
    from { opacity:0; transform: scale(0.8); }
    to { opacity:1; transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="big-title">💣 나의 행동 패턴 분석기</div>', unsafe_allow_html=True)

# 학번 이름
st.markdown("""
<div class="card">
학번: 2024603039<br>
이름: 정희진
</div>
""", unsafe_allow_html=True)

# 로그인
if not login():
    st.stop()

# 퀴즈 실행
score = run_quiz()

st.markdown("### 👇 결과를 확인해보세요")

if st.button("📊 결과 분석하기"):

    result = analyze_result(score)
    details = get_result_detail()
    info = details[result]

    st.markdown("## 📊 분석 리포트")

    # 결과 표시
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.metric("결과", result)

    with col2:
        st.metric("위험도", info["risk"])

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔥 그래프 추가
    st.markdown("### 📈 행동 패턴 분석 그래프")

    labels = list(score.keys())
    values = list(score.values())

    fig = plt.figure()
    plt.bar(labels, values)
    plt.title("행동 유형 점수 분포")

    st.pyplot(fig)

    # 특징
    st.markdown(f"""
    <div class="card" style="animation: fadeInDown 0.8s;">
    <h3>📌 특징</h3>
    <p>{info['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 해결 방법
    st.markdown(f"""
    <div class="card" style="animation: fadeInDown 1s;">
    <h3>💡 해결 방법</h3>
    <p>{info['solution']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 직업 추천
    st.markdown(f"""
    <div class="card" style="animation: fadeInDown 1.2s;">
    <h3>🚀 추천 진로</h3>
    <p>{info['job']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()