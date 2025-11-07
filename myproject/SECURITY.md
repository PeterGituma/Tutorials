# Security and secrets handling

This project keeps secrets out of source control. Follow these steps before pushing to GitHub:

1. Create a `.env` file in the project root (don't commit it):

   SECRET_KEY=your-very-secret-key
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com

2. The project already includes a `.env.example` with placeholders — copy it:

   cp .env.example .env

3. For production, set environment variables in your hosting provider (e.g., Vercel, Heroku, Docker/Kubernetes secrets, or CI/CD) instead of using a `.env` file.

4. `.gitignore` already excludes `.env` and `db.sqlite3`. Verify before pushing:

   git status --ignored

5. If you accidentally committed a secret, rotate it immediately (generate a new SECRET_KEY) and remove it from git history.
