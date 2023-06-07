from pathlib import Path
import shutil
import time

ROOT = Path(__file__).parent
WATCHED_DIR = ROOT / "downloads"
TARGET_DIR = ROOT / "clean_downloads"
CATEGORY_MAP = {
        "audio": ["mp3", "wav", "flac"],
        "documents": ["doc", "docx", "xlsx", "pdf"],
        "pictures": ["jpeg", "jpg", "png", "bmp"]
    }   

def categorize(file_path: Path, category: str):
    category_dir = TARGET_DIR / category
    category_dir.mkdir(exist_ok=True)
    
    file_name = file_path.name
    dst_path = category_dir / file_name
    
    shutil.move(str(file_path), str(dst_path))
    
def get_category(path: Path):
    extension = path.suffix.strip(".")
    for k, v in CATEGORY_MAP.items():
        if extension.lower() in v:
            return k
    return "misc"

def walk(root_dir: Path):
    for path in root_dir.iterdir():
        if path.is_file():
            categorize(path, get_category(path))

def watch(dir: Path):
    
    prev_m_time = dir.stat().st_mtime
    
    while True:
        time.sleep(0.1)
        m_time = dir.stat().st_mtime
        
        if m_time > prev_m_time:
            walk(dir)
            prev_m_time = m_time

watch(WATCHED_DIR)