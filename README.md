# git-test

How to settings git, init, cloning, add, commit, remove, branch, reset, and update sub branch from master branch
<br>

---

## Setting git

- git config --global user.name "아이디"
- git config --global user.email "이메일"
  <br><br>

---

## Initiation

#### 기존 소스 코드 다운로드/복제

- git clone <주소>

#### 프로젝트 폴더 내에서

- git init

#### 클라우드 주소 등록 및 발행

- git remote add origin <주소>

#### 파일 등록

- git add

#### 파일 커밋

- git commit -m "메세지"

#### 파일 넣기

- git push origin <브랜치>
  <br><br>

---

## Branch

#### 브랜치 보기

- git branch

#### 브랜치 생성

- git branch <이름>

#### 브랜치 생성&이동

- git checkout -b <브랜치>

#### 브랜치 이동

- git checkout <브랜치>
  <br><br>

---

## Merge(update) Branch

#### 현재 브랜치에 다른 브랜치의 수정사항 병합(commit 기록 병합)

- git merge <브랜치><br>
  (merge후에 push 필수)

#### 현재 브랜치에 다른 브랜치의 수정사항 병합(commit 기록 병합x)

- git rebase <브랜치><br>
  (rebase후에 commit지점 Applying 하고 merge 수행)

#### 클라우드에서 git프로젝트의 현 상태 확인

- git fetch origin

#### 클라우드의 내용 가져오고 병합(fetch+merge)

- git pull <주소> <브랜치>
  <br><br>

---

## Remove or Cancle

#### git init 해제

- rm -r .git

#### commit 취소하고 unstaged구역에 선택한 HEAD부터 현재 작업내역 저장

- git reset HEAD^

#### commit 취소하고 staged구역에 선택한 HEAD부터 현재 작업내역 저장

- git reset --soft HEAD^

#### commit 취소하고 선택한 HEAD까지 변경사항도 삭제

- git reset --hard HEAD^

<br>

> soft : 현재 인덱스, 워킹 트리를 유지한 채로 HEAD를 변경

> mixed : default 옵션. 인덱스는 취소한채로 워킹트리만 그대로

> hard : 인덱스와 워킹트리 변화를 모두 제거하고 HEAD를 변경

> @: 1.8.4부터 도입된 HEAD의 동의어<br>같은걸로는 @^, @~1, @~ 가 동일

> ^: 한 단계 이전 / ~n: n번 이전

> ORIG_HEAD: 하는 것은 이전에 작업한 곳의 HEAD
