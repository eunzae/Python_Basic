# Section01
# 파이썬 소개 및 작업 환경 설정


# 기본 출력

print('Hello Python!')


# 기본 세팅

# <VS Code 파이썬 환경 설정>
#   Extension - 'Python' 설치
#   View - Command Palete 단축키: command + shift + P
#   Command Palete - 'Python: Select Interpreter' 검색 - 내 파이썬 클릭 후 설치

# <VS Code 파이썬 실행 단축키 설정>
#   Command Palete - 'Tasks: Configure Task' 검색 - 'Others' 선택 - 기존 내용 지우고 하단 내용 복사+붙여넣기
'''

{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Project Label",
            "type": "shell",
            "command": "python",
            "args": [
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "options": {
                "env": {
                    "PYTHONIOENCODING": "UTF-8"
                }
            },
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}

'''
# 설정 후에는 Run Without Debuging을 command + shigt + B 키로 가능

# <VS Code 언어 바꾸기>
#   extention - 'korean' 설치
#   Command Palete - Configure Display Language - 'ko': 한글, 'en': 영문