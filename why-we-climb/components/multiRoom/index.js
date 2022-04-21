import style from './multiRoom.module.css';
import {useState, useEffect} from 'react';
import Link from 'next/link';

export default function MultiRoom({toWaitRoom}) {
  
  const [rooms, setRooms] = useState([]);

  const getRooms = async () => {
    const res = await fetch(/* 수정: api 요청 주소 */);
    const data = await res.json();
    setRooms([data]);
  }

  useEffect(() => {
    getRooms();
  }, [])

  return (
    <main className={style.container}>
      <section>
        open rooms:
        {rooms ? rooms.map(room => {
          <Link href={'/gameRoom/' + room} key={room} passHref></Link>
        }) : <p>no room available</p>}
        
      </section>
      <button onClick={toWaitRoom}>back</button>
    </main>
  )
}