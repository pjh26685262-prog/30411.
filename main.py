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


# 운세 판정 함수 (51~100: 좋은 운세 / 41~50: 보통 / 1~40: 아주 아쉬운 운세)
def get_fortune(number):
    if number >= 81:
        return (
            "🌟 대길 (최고의 대폭발 행운!)",
            "와우! 점수가 엄청 높습니다! 오늘 하루는 무엇을 하든 완벽하게 풀리는 최고의 날입니다. 행운이 폭발합니다!",
            "success",
            "balloons",
        )
    elif number >= 51:
        return (
            "✨ 길 (대단히 좋은 하루)",
            "운이 아주 좋습니다! 기분 좋은 소식과 소소한 행운들이 당신의 하루를 가득 채워줄 거예요.",
            "info",
            "snow",
        )
    elif number >= 41:
        return (
            "☕ 평 (무난하고 평범한 하루)",
            "특별한 사건 없이 평화로운 하루입니다. 마음 편히 휴식을 취하기에 딱 좋은 날이에요.",
            "warning",
            "none",
        )
    else:
        return (
            "💀 대흉 (절망적인 운세...)",
            "앗... 점수가 너무 낮습니다! 오늘은 발밑을 조심하시고 중요한 결정은 내일로 미루시는 게 좋겠어요...",
            "error",
            "trump_card",
        )


# UI 구성
st.title("🎯 하루 한 번 운세 뽑기")
st.write("버튼을 눌러 오늘의 행운의 숫자를 확인하고 운세를 점쳐보세요!")

st.divider()

# 뽑기 버튼 영역
if not st.session_state.has_drawn:
    if st.button("🎲 뽑기 시작!", use_container_width=True):
        number = random.randint(1, 100)
        title, desc, status, effect = get_fortune(number)

        st.session_state.drawn_number = number
        st.session_state.has_drawn = True
        st.session_state.fortune_result = (title, desc, status, effect)

        st.rerun()
else:
    st.info("⏰ 오늘의 운세는 이미 확인하셨습니다. 내일 다시 도전해 주세요!")

# 결과 출력 영역
if st.session_state.has_drawn:
    st.subheader("📊 오늘의 뽑기 결과")

    num = st.session_state.drawn_number
    title, desc, status, effect = st.session_state.fortune_result

    st.metric(label="나의 행운의 숫자 (1~100)", value=f"{num}점")

    # 결과 메시지 출력
    if status == "success":
        st.success(f"### {title}\n\n{desc}")
    elif status == "info":
        st.info(f"### {title}\n\n{desc}")
    elif status == "warning":
        st.warning(f"### {title}\n\n{desc}")
    else:
        st.error(f"### {title}\n\n{desc}")

    # 이펙트 실행
    if effect == "balloons":
        st.balloons()
    elif effect == "snow":
        st.snow()
    elif effect == "trump_card":
        # 트럼프 카드 흔들림 & 뒤집기 아쉬움 효과 (HTML/CSS 애니메이션)
        card_html = """
        <style>
            .card-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 20px;
                perspective: 1000px;
            }
            .trump-card {
                width: 140px;
                height: 200px;
                background-color: #ffffff;
                border: 3px solid #d9534f;
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.3);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 10px;
                font-family: Arial, sans-serif;
                color: #d9534f;
                animation: shake 0.8s ease-in-out infinite alternate;
            }
            .card-top { font-size: 24px; font-weight: bold; text-align: left; }
            .card-center { font-size: 48px; text-align: center; }
            .card-bottom { font-size: 24px; font-weight: bold; text-align: right; transform: rotate(180deg); }
            
            @keyframes shake {
                0% { transform: rotate(-5deg) translateY(0); }
                100% { transform: rotate(5deg) translateY(-10px); }
            }
        </style>
        <div class="card-container">
            <div class="trump-card">
                <div class="card-top">♠ A</div>
                <div class="card-center">😭</div>
                <div class="card-bottom">♠ A</div>
            </div>
        </div>
        <p style="text-align: center; color: #d9534f; font-weight: bold; margin-top: 15px;">
            🎴 아쉬운 스페이드 A 카드가 좌절하고 있습니다...
        </p>
        """
        components.html(card_html, height=280)

# 사이드바 안내
with st.sidebar:
    st.markdown("### 💡 이용 안내")
    st.markdown("- **51 ~ 100점**: 대길 및 좋은 운세")
    st.markdown("- **41 ~ 50점**: 평범한 운세")
    st.markdown("- **1 ~ 40점**: 아쉬운 운세 (트럼프 효과 발동)")
