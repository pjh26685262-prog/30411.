import random
import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="오늘의 운세 뽑기", page_icon="🎯", layout="centered"
)

# =========================================================
# 🆕 [바뀐 부분 1] GIF 지원 및 사용자 커스텀 설정 (사이드바)
# =========================================================
st.sidebar.header("🎨 배경 캐릭터 커스텀")

# 1. 테마/모드 선택 (이모지 or GIF)
char_mode = st.sidebar.radio("캐릭터 유형 선택", ["움직이는 GIF 이미지 🎬", "이모지 🧸"])

selected_items = []
is_gif = False

if char_mode == "움직이는 GIF 이미지 🎬":
    is_gif = True
    gif_preset = st.sidebar.selectbox(
        "GIF 테마 선택",
        ["귀여운 고양이들 🐱", "짱구 & 친구들 👦", "직접 GIF URL 입력"]
    )
    
    if gif_preset == "귀여운 고양이들 🐱":
        selected_items = [
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnFlOHp6aW8xNWNzeHZ4Nm04b3J2aGF6eDRnMnhueDFuYW9uZ3JmciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BzyTuYCmvSORqs1ABM/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z6ZnU1bjRvemxzaHRkNmY5bzBycWZzeG91eGQ0eG15ZXZ3ZnJmZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ICOgUNjpvO0PC/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHgzZnpqam12ZmljMmxqZHk3aGs0aWs2Zm5ndXVpMmgzeHNvdnhmeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jpbnoe3UIa8TU8LM13/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGN5cG1wbnhxdmsyY2tzOHhhNzVnbms0cWhzeXFkODd4c2xmbmt4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C14EipS9xR3pBKa7y4/giphy.gif"
        ]
    elif gif_preset == "짱구 & 친구들 👦":
        selected_items = [
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDRkZnJmbXNsbms1bjRraXRiN3VqMWs1MnA2MnN4cXlydnE5a2VzOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HqtP4R14R72o3lR99j/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjRreTlxaXZxeHZwbG5oNzYxdndxc3ltYngyeWtybjAyaDZvYWRvZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG13MGdhdmt0MmJodmZ0azVvZXVzMDR2aHN2dnU2OHUwcjU2b2s0ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4Epf0fOag3zBvT20/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDVqbm1wYnlva21xdDRubmlhMWkxbXphNG4ydWhsOXZreXpvcWF5YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13A7Ytf2tTHyOU/giphy.gif"
        ]
    else:
        gif_input = st.sidebar.text_area("GIF 이미지 URL 4개 (줄바꿈 구분)", "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif")
        selected_items = [url.strip() for url in gif_input.split('\n') if url.strip()]
        while len(selected_items) < 4:
            selected_items.append("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif")

else:
    char_preset = st.sidebar.selectbox(
        "이모지 테마 선택",
        ["동물 친구들 🧸🐱🐰🐶", "운세 & 행운 🍀🔮🌟💰", "직접 입력"]
    )
    if char_preset == "동물 친구들 🧸🐱🐰🐶":
        selected_items = ["🧸", "🐱", "🐰", "🐶"]
    elif char_preset == "운세 & 행운 🍀🔮🌟💰":
        selected_items = ["🍀", "🔮", "🌟", "💰"]
    else:
        custom_input = st.sidebar.text_input("이모지 4개 입력 (공백 구분)", "🦊 🐼 🐯 🦄")
        selected_items = custom_input.split()
        while len(selected_items) < 4:
            selected_items.append("✨")

# 2. 크기 및 투명도 조절
char_size = st.sidebar.slider("크기 (px)", min_value=30, max_value=120, value=70)
char_opacity = st.sidebar.slider("투명도", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

# 3. 애니메이션 속도 조절
anim_speed = st.sidebar.select_slider("둥둥 떠다니는 속도", options=["느리게", "보통", "빠르게"], value="보통")
speed_multiplier = {"느리게": 1.5, "보통": 1.0, "빠르게": 0.5}[anim_speed]

# =========================================================
# 세션 상태 및 운세 판정 로직 (기존과 동일)
# =========================================================
if "has_drawn" not in st.session_state:
    st.session_state.has_drawn = False
if "drawn_number" not in st.session_state:
    st.session_state.drawn_number = None
if "fortune_result" not in st.session_state:
    st.session_state.fortune_result = None

def get_fortune(number):
    if number >= 81:
        effects = ["gold_pulse", "rainbow_sparkle", "king_crown"]
        return ("🌟 대길 (최고의 대폭발 행운!)", "와우! 점수가 엄청 높습니다! 오늘 하루는 무엇을 하든 완벽하게 풀리는 최고의 날입니다.", random.choice(effects))
    elif number >= 51:
        effects = ["clover_float", "star_bounce", "happy_7"]
        return ("✨ 길 (대단히 좋은 하루)", "운이 아주 좋습니다! 기분 좋은 소식과 소소한 행운들이 당신의 하루를 가득 채워줄 거예요.", random.choice(effects))
    elif number >= 41:
        effects = ["joker_spin", "coffee_relax"]
        return ("☕ 평 (무난하고 평범한 하루)", "특별한 사건 없이 평화로운 하루입니다. 마음 편히 휴식을 취하기에 딱 좋은 날이에요.", random.choice(effects))
    else:
        effects = ["sad_spade", "broken_heart", "thunder_skull"]
        return ("💀 대흉 (절망적인 운세...)", "앗... 점수가 너무 낮습니다! 오늘은 발밑을 조심하시고 중요한 결정은 내일로 미루시는 게 좋겠어요...", random.choice(effects))

st.title("🎯 하루 한 번 운세 뽑기")
st.write("버튼을 눌러 오늘의 행운의 숫자를 확인하고 운세를 점쳐보세요!")
st.divider()

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

if st.session_state.has_drawn:
    st.subheader("📊 오늘의 뽑기 결과")
    num = st.session_state.drawn_number
    title, desc, effect = st.session_state.fortune_result

    st.metric(label="나의 행운의 숫자 (1~100)", value=f"{num}점")
    st.markdown(f"### {title}")
    st.markdown(f"{desc}")

    # 카드 이펙트 처리
    if effect in ["gold_pulse", "rainbow_sparkle", "king_crown"]:
        st.balloons()
        card_code = '<div class="card gold-pulse"><div class="top">♦ A</div><div class="center">👑</div><div class="bottom">♦ A</div></div>'
    elif effect in ["clover_float", "star_bounce", "happy_7"]:
        st.snow()
        card_code = '<div class="card clover-card"><div class="top">♣ 7</div><div class="center">🍀</div><div class="bottom">♣ 7</div></div>'
    elif effect in ["joker_spin", "coffee_relax"]:
        card_code = '<div class="card relax-card"><div class="top">☕ 10</div><div class="center">☕</div><div class="bottom">☕ 10</div></div>'
    else:
        card_code = '<div class="card shake-card"><div class="top">♠ A</div><div class="center">😭</div><div class="bottom">♠ A</div></div>'

    card_html = f"""
    <style>
        .container {{ display: flex; justify-content: center; margin-top: 20px; }}
        .card {{ width: 140px; height: 200px; border-radius: 12px; display: flex; flex-direction: column; justify-content: space-between; padding: 10px; font-family: Arial; font-weight: bold; background: #fff; border: 3px solid #ffd700; }}
        .top {{ font-size: 24px; }}
        .center {{ font-size: 48px; text-align: center; }}
        .bottom {{ font-size: 24px; text-align: right; transform: rotate(180deg); }}
    </style>
    <div class="container">{card_code}</div>
    """
    components.html(card_html, height=250)

# =========================================================
# 🆕 [바뀐 부분 2 & 3] GIF vs 이모지 동적 HTML HTML 렌더링
#
