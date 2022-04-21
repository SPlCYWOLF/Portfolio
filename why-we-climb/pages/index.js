import Head from 'next/head';
import { useState } from 'react';
import style from '../styles/Home.module.css';
import Signup from '../components/signup';
import WaitRoom from '../components/waitRoom';
import MultiRoom from '../components/multiRoom';

export default function Home() {
  const [showMain, setShowMain] = useState(true);
  const [showSignup, setShowSignup] = useState(false);  
  const [showMultiRoom, setShowMultiRoom] = useState(false);
  const [online, setOnline] = useState(false);

  const showMultiRoomToggle = () => {
    setOnline(!online);
    setShowMultiRoom(!showMultiRoom);
  }

  const showSignupToggle = () => {
    setShowSignup(!showSignup);
    setShowMain(!showMain);
  }

  const onlineToggle = (e) => {
    e.preventDefault();
    setShowMain(!showMain);
    setOnline(!online);
  }

  return (
    <>
      {showMain && (
        <main className={style.container}>
          <Head>
            <meta charSet="utf-8" />
            <meta name="viewport" content="width=device-width" />
            <title>점프컹스</title>
            {/* <script type="text/javascript" src="../components/main.js"></script> */}
          </Head>
          <section className={style.intro}>
            <section>
              <h2>why we climb</h2>
            </section>
            <section className={style.login}>
              <div className={style.card}>
                <label>Id <input type="text" /></label>
              </div>
              <div className={style.card}>
                <label>Password <input type="password" /></label>
              </div>
              <section className={style.btns}>
                <button onClick={onlineToggle} >login</button>
                <span>no account? click 
                  <a href='#' onClick={showSignupToggle} className={style.toSignup}> here!</a>
                </span>
              </section>
            </section>
          </section>
        </main>
      )}
      
      {showSignup && <Signup toHome={showSignupToggle} />}
      
      {online && <WaitRoom toHome={onlineToggle} toMultiRoom={showMultiRoomToggle} />}

      {showMultiRoom && <MultiRoom toWaitRoom={showMultiRoomToggle} />}

    </>
  )
}