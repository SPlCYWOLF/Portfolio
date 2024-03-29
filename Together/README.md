<!-- logo -->

# 👬 [ TOGETHER ]

<hr>

<br>

## 📌 목차

<!-- TOC -->
1. [프로젝트 소개](#프로젝트-소개)
2. [기술 스택](#기술-스택)
3. [시스템 구상도](#시스템-구상도)
4. [주요 기능](#주요-기능)
5. [팀원 소개](#팀원-소개)
6. [빌드 및 배포](#빌드-및-배포)
<!-- /TOC -->
<br>
<hr>
<br>

## 프로젝트 소개

```TOGETHER```는 기존의 화상회의 프로그램에 **STT**(speach to text)와 **TTS**(text to speach) 기능을 추가하여   
듣고 말하고 보기 어려웠던 장애인 분들에게 편리함을 제공하는 서비스 입니다.

* [TOGETHER HOMEPAGE](https://ssafytogether.site/)
* [TOGETHER NOTION](https://www.notion.so/A406-80da886168ab4ca4885f5a6de1df1792)

<br>

## 기술 스택

#### Frontend
<img alt="React" src ="https://img.shields.io/badge/React-61DAFB.svg?&style=for-the-badge&logo=react&logoColor=white"/>  <img alt="Next" src ="https://img.shields.io/badge/Next-000000.svg?&style=for-the-badge&logo=Next.js&logoColor=white"/>  <img alt="JavaScript" src ="https://img.shields.io/badge/JavaScript-F7DF1E.svg?&style=for-the-badge&logo=JavaScript&logoColor=white"/>
<img alt="Tailwind CSS" src ="https://img.shields.io/badge/Tailwind CSS-06B6D4.svg?&style=for-the-badge&logo=Tailwind CSS&logoColor=white"/>  <img alt="CSS3" src ="https://img.shields.io/badge/CSS3-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/>  <img alt="Babel" src ="https://img.shields.io/badge/Babel-F9DC3E.svg?&style=for-the-badge&logo=Babel&logoColor=white"/>

#### Backend
<img alt="Spring Boot" src ="https://img.shields.io/badge/Spring Boot-6DB33F.svg?&style=for-the-badge&logo=Spring Boot&logoColor=white"/>  <img alt="Spring Security" src ="https://img.shields.io/badge/Spring Security-6DB33F.svg?&style=for-the-badge&logo=Spring Security&logoColor=white"/>  <img alt="Gradle" src ="https://img.shields.io/badge/Gradle-02303A.svg?&style=for-the-badge&logo=Gradle&logoColor=white"/>

<img alt="Apache Maven" src ="https://img.shields.io/badge/Apache Maven-C71A36.svg?&style=for-the-badge&logo=Apache Maven&logoColor=white"/>  <img alt="Kurrento" src ="https://img.shields.io/badge/Kurrento-008080.svg?&style=for-the-badge&logo=Apache Maven&logoColor=008080"/>  <img alt="Coturn" src ="https://img.shields.io/badge/Coturn-EB680B.svg?&style=for-the-badge&logo=Apache Maven&logoColor=EB680B"/>
<img alt="MySQL" src ="https://img.shields.io/badge/MySQL-4479A1.svg?&style=for-the-badge&logo=MySQL&logoColor=white"/>  <img alt="OpenSSL" src ="https://img.shields.io/badge/OpenSSL-721412.svg?&style=for-the-badge&logo=OpenSSL&logoColor=white"/>

### DevOps
<img alt="Amazon AWS" src ="https://img.shields.io/badge/Amazon AWS-232F3E.svg?&style=for-the-badge&logo=Amazon AWS&logoColor=white"/>  <img alt="Netlify" src ="https://img.shields.io/badge/Netlify-00C7B7.svg?&style=for-the-badge&logo=Netlify&logoColor=white"/>  <img alt="Docker" src ="https://img.shields.io/badge/Docker-2496ED.svg?&style=for-the-badge&logo=Docker&logoColor=white"/>

### Co-tool
<img alt="Jira" src ="https://img.shields.io/badge/Jira-0052CC.svg?&style=for-the-badge&logo=Jira&logoColor=white"/>  <img alt="GitLab" src ="https://img.shields.io/badge/GitLab-FCA121.svg?&style=for-the-badge&logo=GitLab&logoColor=white"/>  <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white">

<br>

## 시스템 구상도

![image](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/de87c10ac334d19914d736ad03addd82/image.png)

<br>

## 주요 기능

- ### 회원관리

- 회원 가입 시 장애 유무를 선택하여 사용자가 필요한 서비스를 제공받을 수 있습니다.<br>
  - ```회원가입```<br>
  ![회원가입](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/a287bccef0b18cf9666465bc115a14da/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.gif)<br>
  <br>

  - ```로그인```<br>
  ![로그인](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/0448875d6b26175eeeee859a9e22bafb/%EB%A1%9C%EA%B7%B8%EC%9D%B8.gif)<br>
  <br>

* ### 메인화면
  
  - 사용자의 고유 방을 확인할 수 있습니다.<br>
  ![내_회의](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/82237749abec4c97167f5d5c0ce703ea/%EB%82%B4_%ED%9A%8C%EC%9D%98.gif)<br>
  <br>
  
  - 초대 코드를 입력하여 방에 입장할 수 있습니다.<br>
  ![회의_참가](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/30c0b80288158d95727c7009161c629e/%ED%9A%8C%EC%9D%98_%EC%B0%B8%EA%B0%80.gif)
  <br>
  
* ### 컨퍼런스 기능
  
  - `컨퍼런스`에 입장하기 전 닉네임을 설정해 입장할 수 있습니다.
  - `시각장애`를 가지고 계신 분은 **TTS** 기능을 제공받을 수 있으며<br>
  ![TTS](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/2c34ffba9aa63baeaafb6f879275d893/TTS.gif)
  <br>
  
  - `청각장애`를 가지고 계신 분은 **STT** 기능을 제공받을 수 있습니다.<br>
  ![STT](https://lab.ssafy.com/s06-webmobile1-sub2/S06P12A406/uploads/9ebc7cb5e7baa0d5539fd5fba0fdc7e9/STT.gif)

<br>

## 팀원 소개

<details><summary><strong>유재룡</strong> [ BE ]&nbsp;&nbsp;&nbsp;<em>Click!</em></summary>

 * **팀장**
 * Database
 * Login API / JWT
 * 동영상 제작
</details>
<details><summary><strong>이　건</strong> [ BE ]</summary>

  * Kurrento 코드 포팅/수정
  * 시그널링 서버 구축
  * User API 
</details>
<details><summary><strong>이호성</strong> [ BE ]</summary>

  * Kurrento 코드 포팅/수정
  * 시그널링 서버 구축
  * Conference API
</details>
<details><summary><strong>강민수</strong> [ FE ]</summary>

  * STT, TTS 서버 구축
  * 랜딩, 메인, 가이드 페이지 레이아웃
  * 로그인, 회원가입 컴포넌트 연결
  * 회원 정보 수정 폼
  * 배포 및 도메인 연결
</details>
<details><summary><strong>김태훈</strong> [ FE ]</summary>

  * 로그인, 회원가입 컴포넌트 제작
  * 웹서비스 페이지 레이아웃 보조
  * 화상회의 구현 보조
  * 웹 접근성 WAI-ARIA 담당
</details>
<details><summary><strong>진민규</strong> [ FE ]</summary>

  * 채팅방 구현
  * 화상회의 구현
  * STT, TTS 화상회의 연결
</details>

<br>

## 빌드 및 배포

* [보러가기✔](https://github.com/SPlCYWOLF/Portfolio/blob/master/Together/exec/%EB%B9%8C%EB%93%9C%20%EB%B0%8F%20%EB%B0%B0%ED%8F%AC.md)

### :triangular_flag_on_post: 버전 정보
* [보러가기✔](https://github.com/SPlCYWOLF/Portfolio/blob/master/Together/exec/%EB%B2%84%EC%A0%84%EC%A0%95%EB%B3%B4.md)

### :beginner: DB 정보
* [보러가기✔](https://github.com/SPlCYWOLF/Portfolio/blob/master/Together/exec/DB_%EC%A0%95%EB%B3%B4.md)

### :ticket: 외부 서비스
* [보러가기✔](https://github.com/SPlCYWOLF/Portfolio/blob/master/Together/exec/%EC%99%B8%EB%B6%80%20%EC%84%9C%EB%B9%84%EC%8A%A4.md)
