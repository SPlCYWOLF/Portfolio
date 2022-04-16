import dynamic from 'next/dynamic';

// 오직 cliend-side 에서만 렌더 되게끔 lazy loading 처리
const Main = dynamic(() => { return import('../components/main') }, { ssr: false });

export default function Game() {

  return (
    <main className="main">
      <div id="container">
        <div id="head">
          <p id="title">점프컹스</p>
          <p id="mute">Mute<input type="checkbox" /></p>
        </div>
        <Main />
      </div>
    </main>
  )
};