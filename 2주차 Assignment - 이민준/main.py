import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# 환경 변수에서 API 키와 시스템 메시지 불러오기
API_KEY = os.environ["API_KEY"]
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]

# OpenAI API 설정
BASE_URL = "https://api.together.xyz"
MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

# OpenAI 클라이언트 초기화
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

# 대화 메시지 초기화
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE}
]

print("챗봇을 시작합니다! (종료하려면 'exit' 또는 'quit' 입력)")

# 사용자 입력 루프
while True:
    user_input = input("당신: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("챗봇을 종료합니다.")
        break

    # 사용자 입력 추가
    messages.append({"role": "user", "content": user_input})

    # 챗봇 응답 요청
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7 #온도함수 - 창의성 정도(0.0~1.0)
    )

    # 챗봇 응답 추출 및 출력
    chatbot_reply = response.choices[0].message.content
    print("챗봇:", chatbot_reply)

    # 챗봇 응답을 메시지 목록에 추가
    messages.append({"role": "assistant", "content": chatbot_reply})

# --- 아이디어 작성 ---
# 이 챗봇을 어디에 응용할 수 있을까요?
# 야구시청에 입문하는 사람들에게 보다 야구를 잘 즐길 수 있도록 도움을 줄 수 있을 것 같습니다.
# 예: '~에 적용해 응용 해보고 싶다'
# 야구 중계 플랫폼에 이러한 챗봇을 삽입하여 경기를 보는 도중에도 모르는 용어들에 대해 배울 수 있도록 하면 좋을 것 같습니다.