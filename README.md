# ChatGPT LangChain 챗시스템 구축 실전 입문(가제) 예제 코드

## 장절별 예제 코드

| 장                                                                  | 소스 코드                                                                                                                                                            |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3장 ChatGPT에서 API를 활용 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ychoi-kr/chatgpt-langchain/blob/main/chapter3/notebook.ipynb) |
| 4장 랭체인 기초 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ychoi-kr/chatgpt-langchain/blob/main/chapter4/notebook.ipynb) |
| 5장 랭체인 활용 - Data connection | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/ychoi-kr/chatgpt-langchain/blob/main/chapter5/5_1_Data_connection.ipynb) |
| 5장 랭체인 활용 - Agents | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/ychoi-kr/chatgpt-langchain/blob/main/chapter5/5_2_Agents.ipynb) |
| 6장 외부 검색, 히스토리를 기반으로 응답하는 웹 앱 구현 | [완성된 소스코드는 여기](./chapter6/) |
| 7장 스트림 형식으로 히스토리를 기반으로 응답하는 슬랙 앱 구현 | [완성된 소스코드는 여기](./chapter7/) |
| 8장 사내 문서에 응답하는 슬랙 앱 구현하기 | [완성된 소스코드는 여기](./chapter8/) |

6장부터 8장까지의 각 절의 소스 코드는 [details](. /details) 디렉터리 아래에서 확인할 수 있습니다.

## 작동 확인 환경

이 책의 소스코드는 다음과 같은 환경과 버전에서 작동을 확인했습니다.

| 장               | 환경                        | 파이썬  | 랭체인 |
| ---------------- | --------------------------- | ------- | --------- |
| 3~5장 | 구글 코랩                | 3.10.12 | 0.1.14 |
| 6~8장 | AWS Cloud9 (Amazon Linux 2) | 3.10.13 | 0.0.292   |

그 외의 파이썬 패키지의 작동이 확인된 버전은 각 장의 디렉토리에 있는 requirements.txt(또는 requirements-dev.txt)를 참고합니다.

7장, 8장의 소스코드 배포에 사용한 Serverless Framework와 그 플러그인은 다음 버전에서 작동을 확인했습니다.

- serverless@3.35.2
- serverless-python-requirements@6.0.0
- serverless-dotenv-plugin@6.0.0

## 원서
- 제목: 「ChatGPT、LangChain によるチャットシステム構築［実践］入門」
- 홈페이지: https://gihyo.jp/book/2023/978-4-297-13839-4
- 깃허브: https://github.com/yoshidashingo/langchain-book
