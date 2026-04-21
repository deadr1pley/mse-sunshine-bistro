# mse-sunshine-bistro

---

## Live Site

The live version of the project can be accessed here:  
[MSE Sunshine Bistro – Live Site](https://mse-sunshine-bistro-1e8e5aa9f2b2.herokuapp.com/)

---

## Features

### Navigation Bar

- Responsive Bootstrap navbar visible on all pages.
- Links to:
  - Home
  - About
  - Menu
  - Book a Table
  - View Bookings

---

### Home Page

- Hero image with welcoming text.
- Short introduction to the restaurant.
- Clear call-to-action button linking to the booking page.

---

### About Page

- Brief information about the restaurant and its atmosphere.

---

### Menu Page

- Static menu listing starters, main courses, desserts and drinks.
- Content is presented in a clean, centered layout.

---

### Booking System (CRUD)

The application now supports full CRUD functionality for bookings in the frontend:

- **Create** – Users can submit a booking through the form  
- **Read** – Users can view all bookings in a list view  
- **Update** – Users can edit existing bookings  
- **Delete** – Users can delete bookings  

---

### Booking Page

- Booking form built with a Django `ModelForm`.
- Fields for:
  - Name
  - Email
  - Date
  - Time
  - Number of guests
  - Optional message
- Validation to prevent:
  - Booking dates in the past
  - Invalid number of guests
- On successful submission:
  - The booking is saved to the database
  - A success message is shown to the user

---

### Admin Panel

- Django admin enables the site owner to:
  - View bookings
  - Edit booking details
  - Update booking status

---

### Footer

- Site-wide footer with restaurant name and placeholder links to social media.

---

## Future Features

- Allow logged-in users to manage their own bookings.
- Email confirmation for bookings.
- Dynamic menu controlled via admin panel.
- Table availability system.

---

## Data Model

The main model in this project is the `Booking` model.

- `name` – customer name (`CharField`)
- `email` – customer email (`EmailField`)
- `date` – booking date (`DateField`)
- `time` – booking time (`TimeField`)
- `guests` – number of guests (`IntegerField`)
- `message` – optional message (`TextField`, blank allowed)
- `status` – booking status (pending / confirmed / cancelled)

---

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- PostgreSQL (Heroku)
- Gunicorn
- WhiteNoise

---

## Testing

Detailed testing is documented in `TESTING.md`.

Testing includes:

- Navigation testing
- Form validation (valid and invalid input)
- Full CRUD testing:
  - Create booking
  - View bookings
  - Edit booking
  - Delete booking
- Admin functionality
- Lighthouse testing
- Responsiveness testing

---

## Deployment

### Heroku Deployment

The project was deployed to Heroku using the following steps:

1. Create a new Heroku app.
2. Connect the app to the GitHub repository.
3. Set Config Vars:
   - `SECRET_KEY`
   - `DATABASE_URL`
4. Ensure required files exist:
   - `requirements.txt`
   - `Procfile`
5. Install required packages:
   - `gunicorn`
   - `whitenoise`
6. Configure static files in `settings.py`.
7. Deploy the `main` branch via Heroku.
8. Run migrations on Heroku:

    python manage.py migrate

9. Create a superuser:

    python manage.py createsuperuser

The application is now live and fully functional.

---

## Running the Project Locally

1. Clone the repository:

    git clone https://github.com/deadr1pley/mse-sunshine-bistro.git
    cd mse-sunshine-bistro

2. Create and activate a virtual environment.

3. Install dependencies:

    pip install -r requirements.txt

4. Create an `env.py` file and add required environment variables.

5. Run migrations:

    python manage.py makemigrations
    python manage.py migrate

6. Create a superuser:

    python manage.py createsuperuser

7. Run the development server:

    python manage.py runserver

---

## Credits

### Media
- The hero image on the home page was taken by the project author.

### Content
- All text content was written by the project author.

### Acknowledgements
- Code Institute for guidance and project inspiration.

### Code & Inspiration
- Inspired by Code Institute Django walkthrough projects
- Bootstrap documentation for layout and styling