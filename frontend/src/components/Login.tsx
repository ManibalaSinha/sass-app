import { useState } from "react";
import { login } from "../api/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const res = await login(email, password);
    localStorage.setItem("token", res.data.access_token);
    alert("Logged in!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} type="password"/>
      <button type="submit">Login</button>
    </form>
  );
}
