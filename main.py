import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="오늘의 운세 뽑기", page_icon="🎯", layout="centered"
)


# 세션 상태 초기화 (하루 1회 제한 및 뽑기 결과 저장용)
if "has_drawn" not in st.session_state:
  st.session_state.has_drawn = False
if "drawn_number" not in st.session_state:
  st.session_state.drawn_number = None
if "fortune_result" not in st.session_state:
  st.session_state.fortune_result = None


# 운세 판정 함수 (숫자가 높을수록 좋은 운세 / 80점 이상은 폭죽!)
def get_fortune(number):
  if number >= 80:
    return (
        "🌟 대길 (최고의 행운!)",
        (
            "와우! 숫자가 아주 높게 나왔습니다! 오늘 하루는 무엇을 하든"
            " 완벽하게 풀리는 최고의 날입니다. 기분 좋은 소식이 찾아올"
            " 거예요!"
        ),
        "success",
        True,
    )  # 폭죽 터짐
  elif number >= 60:
    return (
        "✨ 길 (좋은 하루)",
        (
            "상쾌하고 평온한 하루입니다. 소소한 행운들이 당신을 미소짓게"
            " 만들어 줄 거예요."
        ),
        "info",
        False,
    )
  elif number >= 40:
    return (
        "☕ 평 (평범한 하루)",
        (
            "특별한 일은 없지만 그만큼 마음 편히 보낼 수 있는 평화로운"
            " 하루입니다."
        ),
        "warning",
        False,
    )
  elif number >= 20:
    return (
        "🌧️ 소소한 아쉬움",
        (
            "살짝 아쉬운 순간이 있을 수 있어요. 하지만 가볍게 웃어넘기면 금방"
            " 지나간답니다!"
        ),
        "error",
        False,
    )
  else:
    return (
        "🍃 다음 기회에...",
        (
            "오늘은 에너지가 조금 부족할 수 있겠네요. 무리하지 말고 편안하게"
            " 쉬어가세요. 내일은 더 좋을 거예요!"
        ),
        "error",
        False,
    )


# UI 구성
st.title("🎯 하루 한 번 운세 뽑기")
st.write("버튼을 눌러 오늘의 행운의 숫자를 확인하고 운세를 점쳐보세요!")

st.divider()

# 뽑기 버튼 영역
if not st.session_state.has_drawn:
  if st.button("🎲 뽑기 시작!", use_container_width=True):
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
      "⏰ 오늘의 운세는 이미 확인하셨습니다. 내일 새로운 마음으로 다시"
      " 도전해 주세요!"
  )

# 결과 출력 영역
if st.session_state.has_drawn:
  st.subheader("📊 오늘의 뽑기 결과")

  num = st.session_state.drawn_number
  title, desc, status, is_lucky = st.session_state.fortune_result

  # 숫자에 따른 강조 표시
  st.metric(label="나의 행운의 숫자 (1~100)", value=f"{num}점")

  # 결과 박스 출력
  if status == "success":
    st.success(f"### {title}\n\n{desc}")
  elif status == "info":
    st.info(f"### {title}\n\n{desc}")
  elif status == "warning":
    st.warning(f"### {title}\n\n{desc}")
  else:
    st.error(f"### {title}\n\n{desc}")

  # 높은 숫자(80점 이상)가 나왔을 때 폭죽 효과 실행
  if is_lucky:
    st.balloons()

# 사이드바 안내 (스포일러 방지)
with st.sidebar:
  try:
    st.image(
        "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=300&auto=format&fit=crop",
        caption="Lucky Day",
    )
  except Exception:
    pass
  st.markdown("### 💡 이용 안내")
  st.markdown("- 뽑기는 **하루에 단 한 번**만 가능합니다.")
  st.markdown("- 숫자가 높을수록 더 좋은 운세가 찾아옵니다.")
  st.markdown("- 과연 오늘은 몇 점이 나올까요?")
