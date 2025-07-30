// App.tsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App: React.FC = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState<string>('');

  useEffect(() => {
    axios.get('http://localhost:8000/messages')
      .then(res => setMessages(res.data.messages));
  }, []);

  const handleSubmit = async () => {
    await axios.post('http://localhost:8000/messages', { content: input });
    const res = await axios.get('http://localhost:8000/messages');
    setMessages(res.data.messages);
    setInput('');
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>FastAPI + React POC</h2>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Type a message"
      />
      <button onClick={handleSubmit}>Send</button>
      <ul>
        {messages.map((msg, i) => <li key={i}>{msg}</li>)}
      </ul>
    </div>
  );
};

export default App;
