import style from './waitRoom.module.css';
import {useState, useEffect} from 'react';
import Link from 'next/link';

export default function WaitRoom({toHome, toMultiRoom}) {

  return (
    <main className={style.container}>
      <Link href={'/game'} passHref>
        <h2>single mode</h2>
      </Link>
      <h2 onClick={toMultiRoom}>multi mode</h2>
      <button onClick={toHome}>back</button>
    </main>
  )
}