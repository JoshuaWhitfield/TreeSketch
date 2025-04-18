import { useState, useEffect } from "react";
import "../styles/Sidebar.css";

export default function Sidebar({ onFileSelect }) {
  const [files, setFiles] = useState({});

  useEffect(() => {
    fetch("http://localhost:3001/api/tree")
      .then(res => res.json())
      .then(setFiles);
  }, []);

  const renderFiles = (tree, base = "") =>
    Object.entries(tree).map(([name, type]) => {
      const fullPath = `${base}${name}`;
      if (type === "file") {
        return (
          <div
            key={fullPath}
            className="file"
            onClick={() => onFileSelect(fullPath)}
          >
            {name}
          </div>
        );
      } else {
        return (
          <div key={fullPath} className="folder">
            <strong>{name}</strong>
            <div className="nested">{renderFiles(type, `${fullPath}/`)}</div>
          </div>
        );
      }
    });

  return <aside className="sidebar">{renderFiles(files)}</aside>;
}
