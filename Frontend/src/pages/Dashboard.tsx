import { useEffect, useState } from "react"

function Dashboard() {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchSubscriptionStatus = async () => {
      try {
        const urlParams = new URLSearchParams(window.location.search)
        const sessionId = urlParams.get("session_id")

        if (!sessionId) {
          setError("No se encontró session_id en la URL")
          return
        }

        // ✅ Consultar tu backend para obtener status completo
        const res = await fetch(`http://localhost:8000/api/subscription-status-by-session/${sessionId}/`)
        const result = await res.json()

        if (res.ok) {
          setData(result)
        } else {
          setError(result.error || "Error al obtener la suscripción")
        }
      } catch (err) {
        setError("Error de conexión con el servidor")
        console.error(err)
      }
    }

    fetchSubscriptionStatus()
  }, [])

  if (error) return <p style={{ color: "red" }}>{error}</p>
  if (!data) return <p>Cargando...</p>

  return (
    <div style={{ padding: "2rem" }}>
      <h1>¡Gracias por suscribirte!</h1>
      <p><strong>Nombre:</strong> {data.name || "Desconocido"}</p>
      <p><strong>Correo:</strong> {data.email || "Desconocido"}</p>
      <p><strong>Estado de suscripción:</strong> {data.status}</p>
    </div>
  )
}

export default Dashboard
