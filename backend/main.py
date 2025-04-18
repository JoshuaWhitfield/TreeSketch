from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import file, folder, tree, terminal
app = FastAPI()

# ✅ Add this block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route includes
app.include_router(file.router, prefix="/api/file", tags=["File"])
app.include_router(folder.router, prefix="/api/folder", tags=["Folder"])
app.include_router(tree.router, prefix="/api/tree", tags=["Tree"])
app.include_router(terminal.router, prefix="/api/terminal", tags=["Terminal"])
