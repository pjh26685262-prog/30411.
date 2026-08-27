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


# 운세 판정 함수 (숫자에 따른 등급과 폭죽 효과 여부 결정)
def get_fortune(number):
  if number >= 80:
    return (
        "🌟 대길(大吉)!",
        "오늘은 하늘이 돕는 날입니다! 뜻밖의 행운이 찾아올 수 있어요.",
        "success",
        True,
    )  # 폭죽 O
  elif number >= 60:
    return (
        "✨ 길(吉)",
        (
            "무난하고 평온한 하루입니다. 작은 성취가 기쁨을 가져다줄"
            " 거예요."
        ),
        "info",
        True,
    )  # 폭죽 O
  elif number >= 40:
    return (
        "⚖️ 평(平)",
        "특별한 일은 없지만 평화로운 하루입니다. 조급해하지 마세요.",
        "warning",
        False,
    )  # 폭죽 X
  elif number >= 20:
    return (
        "⚠️ 흉(凶)",
        (
            "조금 주의가 필요한 하루입니다. 중요한 결정은 내일로 미루는 게"
            " 좋아요."
        ),
        "error",
        False,
    )  # 폭죽 X
  else:
    return (
        "⚡ 대흉(大凶)",
        (
            "매사에 돌다리도 두드려보고 건너세요. 마음을 비우고 차분히 쉬어가는"
            " 것이 좋습니다."
        ),
        "error",
        False,
    )  # 폭죽 X


# UI 구성
st.title("🎯 하루 한 번 운세 뽑기")
st.write(
    "버튼을 눌러 오늘의 행운의 숫자를 확인하고 운세를 점쳐보세요! (60점 이상은"
    " 축하 폭죽이 터집니다 🎉)"
)

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
  st.info("⏰ 오늘은 이미 뽑기를 완료하셨습니다. 내일 다시 도전해 주세요!")

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

  # 길(60점) 이상일 경우 풍선/폭죽 애니메이션 실행
  if is_lucky:
    st.balloons()  # 스트림릿 기본 제공 폭죽(풍선) 효과

# 사이드바 안내
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
  st.markdown("- 숫자가 60점 이상(길, 대길)이면 축하 폭죽이 터집니다! 🎉")
  st.markdown("- 깃허브와 스트림릿 클라우드로 쉽게 배포할 수 있습니다.")
