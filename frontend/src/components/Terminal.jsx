import "../styles/Terminal.css";

export default function Terminal() {
  return (
    <div className="terminal">
      <div>&gt; node index.js</div>
      <div className="terminal-output">Hello World</div>
      <div className="cursor" />
    </div>
  );
}
