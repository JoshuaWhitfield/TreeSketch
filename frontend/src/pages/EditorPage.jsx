import { useState } from "react";
import Sidebar from "../components/Sidebar";
import Editor from "../components/Editor";
import Terminal from "../components/Terminal";
import "../styles/EditorPage.css";

export default function EditorPage() {
  const [activeFile, setActiveFile] = useState(null);

  return (
    <div className="editor-wrapper">
      <div className="editor-layout">
        <Sidebar onFileSelect={setActiveFile} />
        <Editor activeFile={activeFile} />
      </div>
      <Terminal />
    </div>
  );
}
