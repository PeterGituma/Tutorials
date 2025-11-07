# myproject — learning Django (fun walkthrough)

Welcome! This is a small Django playground you can use while following along with a tutorial video.

You're learning Django from this video:
https://www.youtube.com/watch?v=nGIg40xs9e4&t=295s

Think of this repo as your practice lab: break things, fix them, and then build your own apps.

## Quickstart — get it running locally

1. Create a Python virtual environment and activate it (macOS zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies (Django). If you want to use local .env support, install python-dotenv too:

```bash
pip install django python-dotenv
```

3. Copy `.env.example` to `.env` and set a secure SECRET_KEY. For local learning, DEBUG=True is fine.

```bash
cp .env.example .env
# Edit .env and put a real SECRET_KEY
```

4. Run migrations and start the dev server:

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## What this repo contains

- `myproject/` — project configuration (settings, urls, wsgi)
- `myapp/` — a tiny example app created for following the tutorial
- `db.sqlite3` — local SQLite database (ignored by git)
- `.env.example` — example environment variables
- `.gitignore` — ignores secrets and common untracked files

## Learning roadmap (bite-sized)

1. Follow the video and re-create what you see.
2. Try adding a new model in `myapp/models.py`, run `makemigrations`, then `migrate`.
3. Create views and templates to render your models. Try the Django admin too.
4. Add tests in `myapp/tests.py` (happy path + one edge case).
5. When comfortable, scaffold a small TODO app: list items, add items, mark done.

## Fun challenges

- Add user authentication and let users save their own TODOs.
- Deploy to Heroku or Render and set environment variables there instead of `.env`.
- Add REST API endpoints using Django REST Framework.

## If you break things (you will!)

- Read the error — Django's tracebacks are often helpful.
- Use `python manage.py shell` to inspect models and data.
- Revert with Git (or rm the DB and start fresh):

```bash
rm db.sqlite3
python manage.py migrate
```

## Want me to do more?

I can:
- generate a fresh secure SECRET_KEY and add a helper script to create `.env` for you,
- add `requirements.txt`,
- scaffold a starter TODO app with models, views, templates, and tests.

Tell me which one and I'll do it next.

Happy building — may your migrations always apply on the first try!
