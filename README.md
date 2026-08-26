# Kiln — consultancy website

A landing page + inquiry form for a software consultancy, built as:

- **frontend/** — Vue 3 + Vite, dark "build studio" design
- **backend/** — Django + Django REST Framework, exposes one API endpoint that stores inquiries and shows them in the Django admin

## Backend setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # this is the login your team uses at /admin (Vue dashboard)
python manage.py runserver
```

The API runs at `http://127.0.0.1:8000`.

### Viewing inquiries

Two ways to see submitted inquiries:

1. **Vue admin dashboard (recommended for your team)** — go to
   `http://localhost:5173/admin`, sign in with a Django user (the superuser
   you created above works), and you'll see a list of inquiries with filtering
   by status and one-click status updates (New / Reviewed / Contacted /
   Archived). No Django templates involved.
2. **Django admin** — `http://127.0.0.1:8000/admin/`, same login. Useful for
   bulk actions or exporting data, but not meant for day-to-day use by the
   whole team.

Endpoint: `POST /api/inquiries/`
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "company": "Acme Co",
  "project_type": "new_app",
  "budget": "5_15k",
  "message": "We need a booking app for our team."
}
```
Rate-limited to 5 submissions/hour per IP to deter spam.

Team-only endpoints (require an `Authorization: Token <token>` header, obtained
from `POST /api/auth/login/` with `{"username": ..., "password": ...}`):
- `GET /api/inquiries/list/` — paginated list, optional `?status=new` filter
- `PATCH /api/inquiries/<id>/status/` — update an inquiry's status

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Runs at `http://localhost:5173`. The API base URL is read from `.env`
(`VITE_API_BASE`) — already set to `http://127.0.0.1:8000/api` for local dev.

## Before you deploy

- **Backend**: set `DJANGO_SECRET_KEY` as an environment variable, set `DEBUG = False`
  in `core/settings.py`, set `ALLOWED_HOSTS`, add your production frontend URL to
  `CORS_ALLOWED_ORIGINS`, and switch off SQLite for something like Postgres.
- **Frontend**: set `VITE_API_BASE` to your deployed API URL before running
  `npm run build`, then serve the `dist/` folder from any static host.
- Update the placeholder copy (services, process steps, social links) in
  `frontend/src/components/` to match your actual offering.

## Project structure

```
kiln/
├── backend/
│   ├── core/            # Django project settings & URLs
│   ├── inquiries/        # model, serializers, views (public + team-only), admin
│   └── requirements.txt
└── frontend/
    └── src/
        ├── App.vue        # shell: nav/footer on public site, hidden on /admin
        ├── router/        # public site + /admin/login + /admin routes
        ├── lib/api.js      # fetch helper + auth token storage
        ├── views/
        │   ├── Home.vue           # marketing landing page
        │   ├── AdminLogin.vue     # team sign-in
        │   └── AdminDashboard.vue # inquiry list + status updates
        └── components/
            ├── NavBar.vue
            ├── HeroSection.vue
            ├── BuildStrip.vue     # the animated pipeline graphic
            ├── ServicesSection.vue
            ├── AboutSection.vue
            ├── ProcessSection.vue
            ├── ContactForm.vue
            └── SiteFooter.vue
```
