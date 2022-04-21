import style from './modal.module.css';

export default function Modal({gameStart}) {

  return (
    <section className={style.container}>
      <h2 onClick={gameStart}>click me to start</h2>
    </section>
  )
}