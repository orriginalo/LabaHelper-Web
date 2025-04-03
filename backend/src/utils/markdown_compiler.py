import os
from fastapi.exceptions import HTTPException
import re

LABS_PATH = "data/Labs"
READMES_PATH = "data/Readmes"

def load_markdown_with_code(lab_num: int):
  
  lab_path = os.path.join(LABS_PATH, f"Laba{lab_num}")
  readme_path = os.path.join(READMES_PATH, f"{lab_num}_README.md")
  if not os.path.isfile(readme_path):
    raise HTTPException(status_code=404, detail=f"README.md не найден по пути {readme_path}")

  with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

  # Регулярка для поиска ссылок вида [filename](./filename)
  pattern = re.compile(r"\[(.+?)\]\(\.\/(.+?)\)")
  
  def replace_match(match):
    filename = match.group(2)
    file_path = os.path.join(lab_path, filename)
    
    if os.path.isfile(file_path):
      with open(file_path, "r", encoding="utf-8") as code_file:
        code_content = code_file.read()
      extension = filename.split('.')[-1]  # Определяем расширение
      return f"```{extension}\n{code_content}\n```"
    else:
      return match.group(0)  # Оставляем ссылку без изменений, если файла нет

  updated_md = pattern.sub(replace_match, readme_content)
  return updated_md