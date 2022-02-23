# git-test

How to settings git, init, cloning, add, commit, remove, branch, reset, and update sub branch from master branch

---

## Setting git
```
git config --global user.name "아이디"
git config --global user.email "이메일"
```

---

## Initiation

#### 원격 저장소 클론 로컬로 복사
```
git clone <:path>
```
#### 프로젝트 폴더 git 등록
```
git init
```
#### git 원격 저장소 목록
```
git remote -v
```
#### git 원격 저장소 추가
```
git remote add <remote:name> <:path>
```
#### git 원격 저장소 URL 변경
```
git remote set-url <remote:name> <:path>
```
#### git 원격 저장소 삭제
```
git remote remove <remote:name>
```
#### unstage 파일 stage 변경
```
git add <file>
```
#### stage 파일 unstage 변경
```
git reset HEAD <file>
```
#### stage 파일 commit
```
git commit -m "message"
```
#### 마지막 commit 내용 변경
```
git commit --amend "message" (option: --no-edit)
```
#### 원격 저장소에 작업 파일 저장
```
git push (-f) <remote:path|name> <branch:name>
```

---

## Branch

#### 브랜치 보기
```
git branch
```
#### 브랜치 생성
```
git branch <branch:name>
```
#### 브랜치 삭제
```
git branch -d <branch:name>
```
#### 브랜치 이동
```
git checkout <branch:name>
```
#### 브랜치 생성&이동
```
git checkout -b <branch:name>
```
#### oldest-commit부터 lastest-commit까지의 모든 커밋을 현재 브랜치에 복사
```
git cherry-pick oldest-commit^..latest-commit
```

---

## Merge(update) Branch

#### 현재 브랜치에 다른 브랜치의 수정사항 병합(commit 기록 병합)
```
git merge <branch:name>
(merge후에 push 필수)
```
#### 현재 브랜치에 다른 브랜치의 수정사항 병합(commit 기록 병합x)
```
git rebase <branch:name>
(rebase후에 commit지점 Applying 하고 merge 수행)
```
#### 클라우드에서 git프로젝트의 현 상태 확인
```
git fetch <remote:path|name> <branch:name>
```
#### 클라우드의 내용 가져오고 병합(fetch+merge)
```
git pull <remote:path|name> <branch:name>
```

---

## Remove or Cancle

#### git init 해제
```
rm -r .git
```
#### git 원격 저장소 삭제
```
git remote remove <remote:name>
```
#### commit 취소하고 unstaged구역에 선택한 HEAD부터 현재 작업내역 저장
```
git reset HEAD^
```
#### commit 취소하고 staged구역에 선택한 HEAD부터 현재 작업내역 저장
```
git reset --soft HEAD^
```
#### commit 취소하고 선택한 HEAD까지 변경사항도 삭제
```
git reset --hard HEAD^
```

---

## Fetch .gitignore
```
git rm -r --cached .
git add .
git commit -m "적용할 커밋 메시지"
```

<br>

> soft : 현재 인덱스, 워킹 트리를 유지한 채로 HEAD를 변경

> mixed : default 옵션. 인덱스는 취소한채로 워킹트리만 그대로

> hard : 인덱스와 워킹트리 변화를 모두 제거하고 HEAD를 변경

> @: 1.8.4부터 도입된 HEAD의 동의어

> ^: 한 단계 이전

> ~n: n번 이전

> ORIG_HEAD: 하는 것은 이전에 작업한 곳의 HEAD
