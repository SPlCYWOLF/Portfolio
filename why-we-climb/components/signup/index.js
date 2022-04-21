import style from './Signup.module.css';

export default function Signup ({toHome}) {
  
  

  return (
    <main className={style.container}>
      <h2>
        this is signup page
      </h2>
      <a href="#" onClick={toHome}>back</a>
    </main>
  )

}