# SmolAgents — Party Planning Agent 🎉

A small demo project showing how to build a simple party-planning agent using the `smolagents` library, with optional Langfuse instrumentation for observability.

---

## 🔧 Features

- Simple agent that suggests menus, finds caterers, and generates superhero-themed party ideas.
- Uses `smolagents` and a Hugging Face model (via token) for inference.
- Optional Langfuse instrumentation via `mylangfuse.py` to track and send telemetry.

## 🚀 Quick Start

1. Clone the repo and change into the project folder:


2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. Configure environment variables by copying `.env` (not committed) and adding your keys:

```text
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_HOST=https://cloud.langfuse.com
HF_TOKEN=hf_...
```

> Note: `.env` is listed in `.gitignore` by default—do NOT commit secrets.

## ▶️ Running the demo

- Run instrumentation + agent example via `test.py`:

```bash
python test.py
```

- Or import and run the `agent` directly (see `partyplanningagent.py`):

```python
from partyplanningagent import agent
agent.run("Plan a party for female superheros")
```

## 📁 Key files

- `partyplanningagent.py` — Agent setup, tools, and agent configuration.
- `mylangfuse.py` — Langfuse client & instrumentation setup.
- `test.py` — Small script that wires instrumentation and runs the agent.
- `requirements.txt` — Python dependencies used by the project.

## ⚙️ Environment variables

- `HF_TOKEN` — Hugging Face token used by `InferenceClientModel`.
- `LANGFUSE_SECRET_KEY`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_HOST` — Langfuse credentials for telemetry.

## 🧪 Testing & Development Tips

- Increase `verbosity_level` in `partyplanningagent.py` for more agent logs.
- Use a local virtualenv to avoid dependency conflicts.
- To add tools, follow the `@tool` decorator pattern used for `suggest_menu` and `catering_service`.

## 🤝 Contributing

Contributions are welcome—feel free to open issues or PRs. Keep secrets out of commits and add tests for new tools.

## 📜 License

This project does not include a license file. Add one (e.g., `MIT`) if you plan to make it public.

---

Happy hacking! 💡 If you want, I can also add a sample GitHub Actions workflow or a `Makefile` to streamline tasks.