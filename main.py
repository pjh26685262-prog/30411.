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

# UI 타이틀
st.title("🎯 하루 한 번 운세 뽑기")

# =========================================================
# ⚙️ [메인 화면 상단] 이미지 & 위치 커스텀 설정 창
# =========================================================
with st.expander("🛠️ 배경 이미지 & 위치 커스텀 설정하기", expanded=False):
    st.subheader("1. 이미지 스타일 설정")
    
    col_a, col_b = st.columns(2)
    with col_a:
        img_size = st.slider("이미지 크기 (px)", min_value=30, max_value=200, value=80, key="img_size_slider")
    with col_b:
        img_opacity = st.slider("투명도", min_value=0.1, max_value=1.0, value=0.8, step=0.1, key="img_opacity_slider")

    st.markdown("---")
    st.subheader("2. 캐릭터 이미지 URL 및 위치 조정")

    # 안정적인 기본 이미지(GIF) 링크 예시
    default_imgs = [
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnFlOHp6aW8xNWNzeHZ4Nm04b3J2aGF6eDRnMnhueDFuYW9uZ3JmciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BzyTuYCmvSORqs1ABM/giphy.gif",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z6ZnU1bjRvemxzaHRkNmY5bzBycWZzeG91eGQ0eG15ZXZ3ZnJmZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ICOgUNjpvO0PC/giphy.gif",
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHgzZnpqam12ZmljMmxqZHk3aGs0aWs2Zm5ndXVpMmgzeHNvdnhmeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jpbnoe3UIa8TU8LM13/giphy.gif",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGN5cG1wbnhxdmsyY2tzOHhhNzVnbms0cWhzeXFkODd4c2xmbmt4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C14EipS9xR3pBKa7y4/giphy.gif"
    ]

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📍 이미지 1 (왼쪽 위)**")
        img1 = st.text_input("사진/GIF URL 1", value=default_imgs[0], key="u1")
        top1 = st.slider("상하 위치 1 (%)", 0, 100, 15, key="t1")
        left1 = st.slider("좌우 위치 1 (%)", 0, 50, 3, key="l1")

        st.markdown("**📍 이미지 2 (왼쪽 아래)**")
        img2 = st.text_input("사진/GIF URL 2", value=default_imgs[1], key="u2")
        top2 = st.slider("상하 위치 2 (%)", 0, 100, 65, key="t2")
        left2 = st.slider("좌우 위치 2 (%)", 0, 50, 4, key="l2")

    with col2:
        st.markdown("**📍 이미지 3 (오른쪽 위)**")
        img3 = st.text_input("사진/GIF URL 3", value=default_imgs[2], key="u3")
        top3 = st.slider("상하 위치 3 (%)", 0, 100, 20, key="t3")
        right3 = st.slider("좌우 위치 3 (%)", 0, 50, 3, key="r3")

        st.markdown("**📍 이미지 4 (오른쪽 아래)**")
        img4 = st.text_input("사진/GIF URL 4", value=default_imgs[3], key="u4")
        top4 = st.slider("상하 위치 4 (%)", 0, 100, 70, key="t4")
        right4 = st.slider("좌우 위치 4 (%)", 0, 50, 4, key="r4")

selected_images = [img1, img2, img3, img4]
positions = [
    (top1, f"left: {left1}%"),
    (top2, f"left: {left2}%"),
    (top3, f"right: {right3}%"),
    (top4, f"right: {right4}%")
]

st.divider()

# =========================================================
# 🎲 운세 뽑기 메인 기능
# =========================================================
st.write("버튼을 눌러 오늘의 행운의 숫자를 확인하고 운세를 점쳐보세요!")

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
# 🖼️ 배경 이미지 동적 HTML 렌더링 (st.markdown으로 수정)
# =========================================================
elements_html = "".join([
    f'<img src="{selected_images[i]}" class="bg-img img{i+1}">'
    for i in range(4)
])

bg_custom_html = f"""
<style>
    .bg-img {{
        position: fixed;
        width: {img_size}px;
        height: auto;
        opacity: {img_opacity};
        z-index: 0;
        pointer-events: none;
    }}

    .img1 {{ top: {positions[0][0]}%; {positions[0][1]}; animation: floatImg 3.0s ease-in-out infinite alternate; }}
    .img2 {{ top: {positions[1][0]}%; {positions[1][1]}; animation: floatImg 4.0s ease-in-out infinite alternate-reverse; }}
    .img3 {{ top: {positions[2][0]}%; {positions[2][1]}; animation: floatImg 3.5s ease-in-out infinite alternate; }}
    .img4 {{ top: {positions[3][0]}%; {positions[3][1]}; animation: floatImg 4.5s ease-in-out infinite alternate-reverse; }}

    @keyframes floatImg {{
        0% {{ transform: translateY(0px) rotate(0deg); }}
        100% {{ transform: translateY(-15px) rotate(6deg); }}
    }}
</style>

{elements_html}
"""

st.markdown(bg_custom_html, unsafe_allow_html=True)
