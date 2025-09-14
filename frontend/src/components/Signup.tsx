import { useState } from "react";
import { signup } from "../api/api";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const res = await signup(email, password);
    alert("Signed up: " + res.data.email);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} type="password"/>
      <button type="submit">Signup</button>
    </form>
  );
}
