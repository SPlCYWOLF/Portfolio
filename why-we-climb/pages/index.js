import Head from 'next/head'
import dynamic from 'next/dynamic';

// 오직 cliend-side 에서만 렌더 되게끔 lazy loading 처리
const Main = dynamic(() => {return import('../components/main')}, {ssr: false});

export default function Home() {
  return (
    <div className="container">
      <Head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>점프컹스</title>
        {/* <script type="text/javascript" src="../components/main.js"></script> */}
      </Head>

      <main className="main">
        <div id="container">
          <div id="head">
            <p id="title">점프컹스</p>
            <p id="mute">Mute<input type="checkbox" /></p>
          </div>
          <Main />
        </div>
      </main>

    </div>
  )
}
