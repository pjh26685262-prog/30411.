import random
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="오늘의 운세 뽑기", page_icon="🎯", layout="centered"
)


# 세션 상태 초기화
if "has_drawn" not in st.session_state:
    st.session_state.has_drawn = False
if "drawn_number" not in st.session_state:
    st.session_state.drawn_number = None
if "fortune_result" not in st.session_state:
    st.session_state.fortune_result = None


# 운세 판정 및 랜덤 효과 매핑 함수
def get_fortune(number):
    if number >= 81:
        # 81~100점 구간 무작위 효과 선택
        effects = ["gold_pulse", "rainbow_sparkle", "king_crown"]
        return (
            "🌟 대길 (최고의 대폭발 행운!)",
            "와우! 점수가 엄청 높습니다! 오늘 하루는 무엇을 하든 완벽하게 풀리는 최고의 날입니다. 행운이 폭발합니다!",
            random.choice(effects),
        )
    elif number >= 51:
        # 51~80점 구간 무작위 효과 선택
        effects = ["clover_float", "star_bounce", "happy_7"]
        return (
            "✨ 길 (대단히 좋은 하루)",
            "운이 아주 좋습니다! 기분 좋은 소식과 소소한 행운들이 당신의 하루를 가득 채워줄 거예요.",
            random.choice(effects),
        )
    elif number >= 41:
        # 41~50점 구간 무작위 효과 선택
        effects = ["joker_spin", "coffee_relax"]
        return (
            "☕ 평 (무난하고 평범한 하루)",
            "특별한 사건 없이 평화로운 하루입니다. 마음 편히 휴식을 취하기에 딱 좋은 날이에요.",
            random.choice(effects),
        )
    else:
        # 1~40점 구간 무작위 효과 선택 (다양한 아쉬운 효과들)
        effects = ["sad_spade", "broken_heart", "thunder_skull"]
        return (
            "💀 대흉 (절망적인 운세...)",
            "앗... 점수가 너무 낮습니다! 오늘은 발밑을 조심하시고 중요한 결정은 내일로 미루시는 게 좋겠어요...",
            random.choice(effects),
        )


# UI 구성
st.title("🎯 하루 한 번 운세 뽑기")
st.write("버튼을 눌러 오늘의 행운의 숫자를 확인하고 운세를 점쳐보세요!")

st.divider()

# 뽑기 버튼 영역
if not st.session_state.has_drawn:
    if st.button("🎲 뽑기 시작!", use_container_width=True):
        number = random.randint(1, 100)
        title, desc, effect = get_fortune(number)

        st.session_state.drawn_number = number
        st.session_state.has_drawn = True
        st.session_state.fortune_result = (title, desc, effect)

        st.rerun()
else:
    st.write("⏰ **오늘의 운세는 이미 확인하셨습니다. 내일 다시 도전해 주세요!**")

# 결과 출력 영역
if st.session_state.has_drawn:
    st.subheader("📊 오늘의 뽑기 결과")

    num = st.session_state.drawn_number
    title, desc, effect = st.session_state.fortune_result

    st.metric(label="나의 행운의 숫자 (1~100)", value=f"{num}점")

    # 결과 텍스트 출력
    st.markdown(f"### {title}")
    st.markdown(f"{desc}")

    # ==================== 이펙트 처리 영역 ====================

    # [81~100점 효과들]
    if effect in ["gold_pulse", "rainbow_sparkle", "king_crown"]:
        st.balloons()
        
        if effect == "gold_pulse":
            card_code = '<div class="card gold-pulse"><div class="top">♦ A</div><div class="center">👑</div><div class="bottom">♦ A</div></div>'
        elif effect == "rainbow_sparkle":
            card_code = '<div class="card rainbow-card"><div class="top">♥ A</div><div class="center">💎</div><div class="bottom">♥ A</div></div>'
        else:
            card_code = '<div class="card crown-card"><div class="top">♠ K</div><div class="center">🏆</div><div class="bottom">♠ K</div></div>'

        card_html = f"""
        <style>
            .container {{ display: flex; justify-content: center; margin-top: 20px; }}
            .card {{ width: 140px; height: 200px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; padding: 10px; font-family: Arial; font-weight: bold; }}
            .top {{ font-size: 24px; }}
            .center {{ font-size: 48px; text-align: center; }}
            .bottom {{ font-size: 24px; text-align: right; transform: rotate(180deg); }}
            
            .gold-pulse {{ background: linear-gradient(135deg, #f6d365, #fda085); border: 3px solid #ffd700; color: #fff; animation: pulse 1s infinite alternate; }}
            .rainbow-card {{ background: linear-gradient(135deg, #ff9a9e, #fecfef, #a1c4fd); border: 3px solid #fff; color: #fff; animation: bounce 0.8s infinite alternate; }}
            .crown-card {{ background: #2c3e50; border: 3px solid #f1c40f; color: #f1c40f; animation: pulse 1.2s infinite alternate; }}

            @keyframes pulse {{ 0% {{ transform: scale(1); }} 100% {{ transform: scale(1.08); }} }}
            @keyframes bounce {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-15px); }} }}
        </style>
        <div class="container">{card_code}</div>
        """
        components.html(card_html, height=250)

    # [51~80점 효과들]
    elif effect in ["clover_float", "star_bounce", "happy_7"]:
        st.snow()
        
        if effect == "clover_float":
            card_code = '<div class="card clover-card"><div class="top">♣ 7</div><div class="center">🍀</div><div class="bottom">♣ 7</div></div>'
        elif effect == "star_bounce":
            card_code = '<div class="card star-card"><div class="top">★ 7</div><div class="center">⭐</div><div class="bottom">★ 7</div></div>'
        else:
            card_code = '<div class="card happy-card"><div class="top">♥ 7</div><div class="center">😄</div><div class="bottom">♥ 7</div></div>'

        card_html = f"""
        <style>
            .container {{ display: flex; justify-content: center; margin-top: 20px; }}
            .card {{ width: 140px; height: 200px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; padding: 10px; font-family: Arial; font-weight: bold; background: #fff; }}
            .top {{ font-size: 24px; }}
            .center {{ font-size: 48px; text-align: center; }}
            .bottom {{ font-size: 24px; text-align: right; transform: rotate(180deg); }}
            
            .clover-card {{ border: 3px solid #2e7d32; color: #2e7d32; animation: float 1.8s ease-in-out infinite alternate; }}
            .star-card {{ border: 3px solid #f39c12; color: #f39c12; animation: float 1.2s ease-in-out infinite alternate; }}
            .happy-card {{ border: 3px solid #e74c3c; color: #e74c3c; animation: float 2s ease-in-out infinite alternate; }}

            @keyframes float {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-12px); }} }}
        </style>
        <div class="container">{card_code}</div>
        """
        components.html(card_html, height=250)

    # [41~50점 효과들]
    elif effect in ["joker_spin", "coffee_relax"]:
        if effect == "joker_spin":
            card_code = '<div class="card spin-card"><div class="top">JOKER</div><div class="center">🃏</div><div class="bottom">JOKER</div></div>'
        else:
            card_code = '<div class="card relax-card"><div class="top">☕ 10</div><div class="center">☕</div><div class="bottom">☕ 10</div></div>'

        card_html = f"""
        <style>
            .container {{ display: flex; justify-content: center; margin-top: 20px; }}
            .card {{ width: 140px; height: 200px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; padding: 10px; font-family: Arial; font-weight: bold; background: #fff; border: 3px solid #7f8c8d; color: #7f8c8d; }}
            .top {{ font-size: 20px; }}
            .center {{ font-size: 48px; text-align: center; }}
            .bottom {{ font-size: 20px; text-align: right; transform: rotate(180deg); }}
            
            .spin-card {{ animation: spin 5s linear infinite; }}
            .relax-card {{ animation: swing 3s ease-in-out infinite alternate; }}

            @keyframes spin {{ 0% {{ transform: rotateY(0deg); }} 100% {{ transform: rotateY(360deg); }} }}
            @keyframes swing {{ 0% {{ transform: rotate(-5deg); }} 100% {{ transform: rotate(5deg); }} }}
        </style>
        <div class="container">{card_code}</div>
        """
        components.html(card_html, height=250)

    # [1~40점 효과들 - 아쉬운 연출들]
    elif effect in ["sad_spade", "broken_heart", "thunder_skull"]:
        if effect == "sad_spade":
            card_code = '<div class="card shake-card"><div class="top">♠ A</div><div class="center">😭</div><div class="bottom">♠ A</div></div>'
        elif effect == "broken_heart":
            card_code = '<div class="card break-card"><div class="top">♥ 2</div><div class="center">💔</div><div class="bottom">♥ 2</div></div>'
        else:
            card_code = '<div class="card dark-card"><div class="top">◆ 3</div><div class="center">⚡</div><div class="bottom">◆ 3</div></div>'

        card_html = f"""
        <style>
            .container {{ display: flex; justify-content: center; margin-top: 20px; }}
            .card {{ width: 140px; height: 200px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; padding: 10px; font-family: Arial; font-weight: bold; }}
            .top {{ font-size: 24px; }}
            .center {{ font-size: 48px; text-align: center; }}
            .bottom {{ font-size: 24px; text-align: right; transform: rotate(180deg); }}
            
            .shake-card {{ background: #ffffff; border: 3px solid #d9534f; color: #d9534f; animation: shake 0.5s ease-in-out infinite alternate; }}
            .break-card {{ background: #2c3e50; border: 3px solid #95a5a6; color: #e74c3c; animation: drop 1s ease infinite alternate; }}
            .dark-card {{ background: #1a1a1a; border: 3px solid #e74c3c; color: #f39c12; animation: flash 0.8s infinite alternate; }}

            @keyframes shake {{ 0% {{ transform: rotate(-8deg); }} 100% {{ transform: rotate(8deg); }} }}
            @keyframes drop {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(15px); }} }}
            @keyframes flash {{ 0% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
        </style>
        <div class="container">{card_code}</div>
        """
        components.html(card_html, height=250)

# 사이드바 안내
with st.sidebar:
    st.markdown("### 💡 이용 안내")
    st.markdown("- **81 ~ 100점**: 폭죽 + 랜덤 황금 계열 카드")
    st.markdown("- **51 ~ 80점**: 눈 내림 + 랜덤 행운 계열 카드")
    st.markdown("- **41 ~ 50점**: 회전/흔들림 무난한 카드")
    st.markdown("- **1 ~ 40점**: 랜덤 좌절/아쉬움 카드 효과 (울기, 깨진 하트, 번개)")
