import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="미스터리 운세 뽑기", page_icon="❓", layout="centered"
)


# 세션 상태 초기화 (하루 1회 제한 및 뽑기 결과 저장용)
if "has_drawn" not in st.session_state:
  st.session_state.has_drawn = False
if "drawn_number" not in st.session_state:
  st.session_state.drawn_number = None
if "fortune_result" not in st.session_state:
  st.session_state.fortune_result = None


# 운세 판정 함수 (1점이 가장 좋고, 숫자가 높을수록 험난함)
def get_fortune(number):
  if number == 1:
    return (
        "👑 전설의 1점 (대박 찬스!)",
        (
            "믿을 수 없습니다! 확률을 뚫고 1점을 뽑으셨군요! 오늘 당신은"
            " 세상의 모든 행운을 독차지하게 됩니다. 로또를 사거나 원하는 모든"
            " 일이 마법처럼 이뤄질 것입니다!"
        ),
        "success",
        True,
    )  # 폭죽 터짐
  elif number <= 20:
    return (
        "🌱 소소한 행운",
        (
            "기분 좋은 바람이 부는 하루네요. 소소하지만 확실한 행복이"
            " 찾아옵니다."
        ),
        "info",
        False,
    )
  elif number <= 50:
    return (
        "☕ 평범한 일상",
        (
            "특별할 건 없지만 평화롭고 조용한 하루입니다. 따뜻한 커피 한 잔의"
            " 여유를 즐겨보세요."
        ),
        "warning",
        False,
    )
  elif number <= 80:
    return (
        "🌧️ 주의보 발령",
        (
            "은근히 귀찮은 일이 생길 수 있어요. 길을 가다 돌멩이에 걸리거나"
            " 약속 시간이 헷갈릴 수 있으니 정신 바짝 차려야 합니다!"
        ),
        "error",
        False,
    )
  else:
    return (
        "🌪️ 대재앙의 날 (최악의 고난)",
        (
            "아... 숫자가 너무 높군요. 오늘은 가만히 있어도 지갑을 떨어뜨리거나"
            " 이불 킥 할 일이 생길 수 있습니다. 이불 속에서 절대 나오지 마세요!"
        ),
        "error",
        False,
    )


# UI 구성
st.title("❓ 미스터리 운세 뽑기")
st.write("버튼을 눌러 오늘의 운세를 확인해 보세요!")

st.divider()

# 뽑기 버튼 영역
if not st.session_state.has_drawn:
  if st.button("🎲 운세 확인하기", use_container_width=True):
    # 1부터 100까지의 무작위 숫자 생성
    number = random.randint(1, 100)
    title, desc, status, is_lucky = get_fortune(number)

    # 결과 저장
    st.session_state.drawn_number = number
    st.session_state.has_drawn = True
    st.session_state.fortune_result = (title, desc, status, is_lucky)

    st.rerun()  # 화면 새로고침
else:
  st.info(
      "⏰ 오늘의 운세는 이미 확인하셨습니다. 내일 새로운 운세를 시험해"
      " 보세요!"
  )

# 결과 출력 영역
if st.session_state.has_drawn:
  st.subheader("📊 오늘의 뽑기 결과")

  num = st.session_state.drawn_number
  title, desc, status, is_lucky = st.session_state.fortune_result

  # 숫자에 따른 강조 표시
  st.metric(label="나의 뽑기 번호 (1~100)", value=f"{num}점")

  # 결과 박스 출력
  if status == "success":
    st.success(f"### {title}\n\n{desc}")
  elif status == "info":
    st.info(f"### {title}\n\n{desc}")
  elif status == "warning":
    st.warning(f"### {title}\n\n{desc}")
  else:
    st.error(f"### {title}\n\n{desc}")

  # 1점을 뽑았을 때만 화려한 폭죽 효과 발동
  if is_lucky:
    st.balloons()

# 사이드바 안내 (스포일러성 문구 제거)
with st.sidebar:
  try:
    st.image(
        "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=300&auto=format&fit=crop",
        caption="Mystery Day",
    )
  except Exception:
    pass
  st.markdown("### 💡 이용 안내")
  st.markdown("- 뽑기는 **하루에 단 한 번**만 가능합니다.")
  st.markdown("- 결과는 무작위로 결정됩니다.")
  st.markdown("- 어떤 숫자가 행운일지는 직접 확인해 보세요!")
