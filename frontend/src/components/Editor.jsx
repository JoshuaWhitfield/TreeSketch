import { useState, useEffect } from "react";
import "../styles/Editor.css";

export default function Editor({ activeFile }) {
  const [content, setContent] = useState("");

  useEffect(() => {
    if (!activeFile) return;
    fetch(`http://localhost:3001/api/file?path=${encodeURIComponent(activeFile)}`)
      .then(res => res.text())
      .then(setContent);
  }, [activeFile]);

  return (
    <main className="editor">
      {content.split("\n").map((line, i) => (
        <div className="line" key={i}>
          <span className="line-number">{i + 1}</span>
          <span className="line-content">{line}</span>
        </div>
      ))}
    </main>
  );
}
