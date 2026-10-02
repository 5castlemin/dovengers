# Progress & Decision Log

현재 상태의 단일 기록. 계획·구현·실험·사용자 검증을 구분한다.

## 2026-10-02 — Repository 초기 구조

### 확인된 선행 자료

- `technical_project_brief_power_scheduling.md`를 Ground Truth로 읽고 저장소용 `PROJECT_BRIEF.md`에 보존했다.
- 기존 작업공간의 SMARD 확보·작은 3작업 PoC는 확인된 선행 작업이다.
- 선행 실행 코드·데이터·결과는 아직 이 저장소로 이식하지 않았다.
- GitHub connector에서 인증 계정 `5castlemin`을 확인했다.
- 참고 repository main README는 정보 구조만 참고했다. 모델·성과를 사용하지 않았다.

### 이번에 생성한 것

- README: 문제·데이터·예측/최적화 구분·pipeline·평가·MVP·실명 역할·cross review.
- directory scaffold 및 책임·TODO가 적힌 Python 모듈과 테스트 계획 파일.
- V1 개발 의존성 후보·gitignore·데이터 관리 안내·Roadmap.

### 합의 제안 / 현재 설정

- V1은 알려진 가격, UTC 1시간, 비중단 고정 MW 작업, 기본부하 0, 배터리 없음.
- 실제 비용 표현은 Wholesale Cost Proxy.
- Forecast·CVaR·Battery는 후속 검증. 현재 구현되지 않았다.
- 원격 repository visibility는 사용자 선택 대기. public/private를 임의 선택하지 않는다.
- 소스 라이선스는 아직 선택하지 않았다. 데이터 라이선스와 구분한다.

### 미완료

- 데이터 계약·수집 파이프라인·baseline·validator·MILP·evaluator·UI 구현.
- 실제 실행 테스트·의존성 설치 검증·공통 환경 고정.
- 실제 사용자·요금계약·경쟁 서비스·ML 필요성 검증.
- 원격 생성·push: visibility 결정 및 연결 경로 확인 후 진행.

### 원본 추적

- Ground Truth 원본 SHA-256: `af1c9ec93582c01a2cd9e7ed1fda02aab39df35e8a2f97aed00b59bece3961a0`
- 원본 문서 내용은 보존했고, 저장소 밖 로컬 절대경로 링크는 설명으로 바꾸었다.

## 기록 형식

각 변경은 `날짜 / 담당 / 변경 / 검증 방법·결과 / 남은 일 / 가설 여부`로 추가한다. 구현 전에는 완료 체크를 하지 않는다. Git commit은 코드 변경의 증거이며 모델·사업 성과의 증거가 아니다.
