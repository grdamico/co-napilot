"use client";

import { useState } from "react";
import { askAI } from "../services/api";

export default function Home() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    const result = await askAI(input);
    setResponse(result);
    setLoading(false);
  };

  return (
    <main style={{ padding: "2rem" }}>
      <h1>co-napilot</h1>

      <textarea
        placeholder="Describe your situation..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ width: "100%", height: "100px" }}
      />

      <br /><br />

      <button onClick={handleSubmit}>
        {loading ? "Thinking..." : "Generate Plan"}
      </button>

      <br /><br />

      {response && (
        <div>
          <h3>Result:</h3>
          <pre>{response}</pre>
        </div>
      )}
    </main>
  );
}