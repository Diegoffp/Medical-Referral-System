# Referral App — Blank Scaffold

Blank Django site: home page + placeholder Patient/Provider pages + working
admin panel. No features yet — this is the "create the blank website"
ticket (HR-6).

## Setup

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # to log into /admin/
python manage.py runserver
```

Then visit http://localhost:8000/

## Structure

- `referral_site/` — project settings and root URL routing
- `core/` — app holding the home page and placeholder Patient/Provider views
- `templates/base.html` — shared layout + nav bar
- `core/templates/core/` — page templates that extend `base.html`

## Next steps (future tickets)

- Add User/Patient/Provider/Specialist/Admin models (see SRS class diagram)
- Add Hospital, Service, Referral models
- Replace placeholder pages with real search/compare/referral functionality
