import Head from 'next/head';
import style from '../styles/Home.module.css';

export default function Home() {
  return (
    <div className="container">
      <Head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>점프컹스</title>
        {/* <script type="text/javascript" src="../components/main.js"></script> */}
      </Head>

      <section className={style.grid}>
        <div className={style.card}>
          <label htmlFor='id' >Id</label>
          <input id="id" type="text" />
        </div>
        <div className={style.card}>
          <label htmlFor="pw" >Password</label>
          <input id="pw" type="password" />
        </div>
      </section>

    </div>
  )
}
