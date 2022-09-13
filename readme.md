1. .env 파일

```env
TOKEN='DISCORD_BOT_TOKEN'
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=DB_HOST
DB_NAME=DB_NAME
```

2. 개발서버 with watchdog
   - > python3 main.py
3. 프로덕션 서버
   - > python3 exec.py

4. 폴더구조
   ```
   |   .env                      --환경설정 파일입니다.
   |   .gitignore
   |   base.py                   --실제 디스코드 봇이 초기화 됩니다. 모든 discord app은 이곳의 app을 참조합니다
   |   consts.py
   |   docker-compose.yml        --당신이
   |   dockerfile                --싫어하는 것들
   |   exec.py                   --디스코드 서버를 구동하는 파일입니다
   |   main.py                   --watchdog을 이용해 변경사항이 감지되면 자동으로 리로드 해주는 파일입니다
   |   readme.md                 --이것은 '나'입니다
   |   requirements.txt          --필요한 파이썬 모듈을 담아둡니다
   |   todo.md
   |
   +---.devcontainer             --윈도우 가상 컨테이너용 설정 파일입니다.
   |       devcontainer.json
   |       docker-compose.yml
   |
   +---MyBot
   |   |   conversations.py      --기본 회화 엔드포인트입니다.
   |   |   interfaces.py         --discord의 Messageable과 Context타입의 래퍼 인터페이스입니다.
   |   |   mybot.py              --봇의 기본 동작을 지정하는 클래스가 있습니다.
   |   |   __init__.py           --파이썬 기본 패키지 단위에 필요한 파일입니다. 보통은 비어있습니다.
   |   |
   |   +---cats
   |   |   |   conversations.py  --고양이 봇과의 인터랙션 회화 엔드포인트입니다.
   |   |   |   functions.py      --고양이와의 기본적인 상호작용을 관리하는 클래스입니다.
                                   추후에 다른 폴더로 옮길 예정입니다.
   |   |   |   __init__.py
   |   |   |
   |   |
   |   +---enchant
   |   |   |   conversations.py  --마비노기 인챈트 검색 회화 엔드포인트입니다.
   |   |   |   __init__.py       --마비노기 인챈트 검색페이지를 크롤링해 결과를 리턴하는 클래스가 있습니다.
   |   |   |
   |   |
   |   +---formatter
   |   |   |   Formatter.py      --discord 봇의 출력 문법을 메소드로 정의 해놓은 클래스입니다. 추후에 utils이나 그 외의 폴더로 옮길 예정입니다.
   |   |   |
   |   |
   |   +---intimacy
   |   |       conversations.py  --사용자와 discord 봇의 관계에 관한 회화가 들어갈 엔드포인트입니다.
   |   |       __init__.py
   |   |
   |   +---messages
   |   |   |   conversations.py  --메모와 관련된 회화가 있는 엔드포인트입니다.
   |   |   |   __init__.py
   |   |   |
   |   |
   |
   +---server
   |   |   __init__.py           --백엔드에 등록된 모듈들을 자동으로 db에 migrate해주는 코드가 있습니다.
   |   |                         --db모델들이 추가 될때마다 이곳에서 수동으로 임포트를 해주어야 합니다
   |   +---base
   |   |   |   models.py         --백엔드에서 쓰이는 기본적인 db모델을 정의 해놓은 파일입니다.
                                 --모든 모델에서 쓰이는 메소드들을 정의 해놓습니다.
                                 --ex) models.my_name 은 각 모델들의 이름을 Formatter클래스를 통해 볼드&이탤릭체로 리턴합니다
   |   |   |   settings.py       --백엔드와 db의 연결을 정의 해놓은 파일입니다.
   |   |   |   __init__.py
   |   |   |
   |   |
   |   +---attachments
   |   |   |   models.py         --사용자가 파일을 업로드 하면 이곳에 저장됩니다.
                                 --이후 모든 models.py들은 각 모델의 기본적인 로직을 정의 해둡니다.
                                 --친밀도증가,친밀도 감소등의 기본적인 메소드를 구현해놓습니다.
   |   |   |   __init__.py
   |   |   |
   |   |
   |   +---cats
   |   |   |   models.py
   |   |   |   __init__.py
   |   |   |
   |   |
   |   +---channels
   |   |       models.py
   |   |       __init__.py
   |   |
   |   +---history
   |   |   |   models.py
   |   |   |   __init__.py
   |   |   |
   |   |
   |   +---messages
   |   |   |   models.py
   |   |   |   __init__.py
   |   |   |
   |   |
   |   +---users
   |   |   |   models.py
   |   |   |   __init__.py
   |   |   |
   |   |
   |
   +---utils
   |   |   fshandler.py          --파일변화가 감지되면 자동으로 discord 봇을 리로드 시켜주는 핸들러입니다.
   |   |
   |
```

5. 테스트 로케이션
   1. https://discord.gg/FvJwWbYnFs
6. 명령어
   1. ?help