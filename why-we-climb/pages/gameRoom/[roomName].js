import { useRouter } from "next/router"
import { useEffect } from "react"

export default function GameRoom() {

  const router = useRouter();
  const roomId = router.query.productId;

  return (
    <div>welcome to room: {roomId}</div>
  )
}