import { Link } from "react-router-dom";
import "../styles/NavBar.css";

export default function NavBar() {
  return (
    <nav className="navbar">
      <div className="nav-title">🌳 TreeSketch</div>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/editor">Editor</Link>
      </div>
    </nav>
  );
}
