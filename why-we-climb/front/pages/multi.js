
import FindModal from '../components/multi/findModal';
import JoinModal from "../components/multi/joinModal";
import Create from '../components/multi/create';
import style from '../styles/multi.module.css';
import Link from 'next/link';
import { useState } from 'react';
import axios from 'axios';
import toast from 'react-hot-toast';

export default function Multi() {
  const basicURL = 'https://k6a401.p.ssafy.io/api'
  const [modalOn, setModalOn] = useState(false);

  const toggleModal = () => {
    console.log('toggleModal activated');
    setModalOn(!modalOn);
    console.log(`modal is currently: ${modalOn}`)
  }

  const toggleCreateModal = () => {
    toggleModal();
    toast(<CreateModal toggleModal={toggleModal} />)
  }
  const toggleFindModal = () => {
    toggleModal();
    toast(<FindModal toggleModal={toggleModal} />)
  }
  const toggleJoinModal = () => {
    toggleModal();
    toast(<JoinModal toggleModal={toggleModal} />)
  }

  const joinRoom = () => {
    axios.get(`${basicURL}/chat/rooms`)
      .then(res=>res.data)
      .then(data=>{
        if(data.length === 0) {
          alert("대기 중인 방이 없습니다. 잠시후 시도해 주세요.");
        } else {
          location.href=`multi/${data[data.length-1].roomId}`;
        }
      })
      .catch(e=>console.error(e))
  }

  return (
    <main className={`${style.multi} ${modalOn && style.modalOn}`}>   {/* `${modalOn ? style.ModalOn : style.multi}` */}
      
      <nav className={style.lobby}>
        <h2><a href="#" onClick={toggleJoinModal} >join</a></h2>
        <h2><a href="#" onClick={toggleFindModal} >find</a></h2>
        <h2><a href="#" onClick={toggleCreateModal} >create</a></h2>
      </nav>
      <Link href={'/'} passHref>
        <button className={style.back} >back</button>
      </Link> 
    
    </main>
  )
}