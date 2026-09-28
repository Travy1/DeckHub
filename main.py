import json, shlex, shutil, subprocess
from pathlib import Path
CONFIG=Path.home()/".config/deckhub/launchers.json"
DEFAULTS=[{"name":"Steam","command":"steam","category":"Gaming","description":"Open Steam"},{"name":"Discover","command":"plasma-discover","category":"System","description":"Install applications"},{"name":"Dolphin","command":"dolphin","category":"System","description":"Browse files"},{"name":"Konsole","command":"konsole","category":"System","description":"Terminal"}]
class Plugin:
 async def _main(self):
  CONFIG.parent.mkdir(parents=True,exist_ok=True)
  if not CONFIG.exists(): self._save(DEFAULTS)
 def _load(self):
  try:
   data=json.loads(CONFIG.read_text()); return data if isinstance(data,list) else DEFAULTS
  except (OSError,json.JSONDecodeError): return DEFAULTS
 def _save(self,data):
  CONFIG.parent.mkdir(parents=True,exist_ok=True); CONFIG.write_text(json.dumps(data,indent=2))
 async def get_launchers(self): return self._load()
 async def save_launchers(self,entries):
  if not isinstance(entries,list): raise ValueError("Expected list")
  safe=[{k:str(x.get(k,"")) for k in ("name","command","category","description")} for x in entries if isinstance(x,dict) and x.get("name") and x.get("command")]
  self._save(safe); return True
 async def launch(self,command):
  args=shlex.split(command)
  if not args: raise ValueError("Empty command")
  if "/" not in args[0] and shutil.which(args[0]) is None: raise FileNotFoundError(args[0])
  subprocess.Popen(args,start_new_session=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); return True
