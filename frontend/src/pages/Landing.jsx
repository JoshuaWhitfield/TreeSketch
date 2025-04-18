import "../styles/Landing.css";

export default function Landing() {
  return (
    <div className="landing">
      <h1 className="landing-title">Welcome to TreeSketch</h1>
      <p className="landing-subtitle">
        A visual coding interface with filesystem + terminal access.
      </p>
      <a href="/editor">
        <button className="enter-button">Enter Editor</button>
      </a>
    </div>
  );
}
