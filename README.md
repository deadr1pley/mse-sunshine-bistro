# mse-sunshine-bistro

## Features

### Navigation Bar

- Responsive Bootstrap navbar visible on all pages.
- Links to:
  - Home
  - About
  - Menu
  - Book a Table

### Home Page

- Hero image with welcoming text.
- Short introduction to the restaurant.
- Clear call-to-action button linking to the booking page.

### About Page

- Brief information about the restaurant and its atmosphere.

### Menu Page

- Static menu listing starters, main courses, desserts and drinks.
- Content is presented in a clean, centered layout.

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

### Admin Panel

- Django admin enables the site owner to:
  - View bookings
  - Edit booking details
  - Update booking status

### Footer

- Site-wide footer with restaurant name and placeholder links to social media.

---

## Future Features

- Allow logged-in users to view and manage their own bookings.
- Email confirmation when a booking is submitted or confirmed.
- Database-driven menu so that staff can update dishes via the admin.
- Table management (number of tables, capacity, fully booked time slots).

---

## Data Model

The main model in this project is the `Booking` model.

- `name` – customer name (`CharField`)
- `email` – customer email (`EmailField`)
- `date` – booking date (`DateField`)
- `time` – booking time (`TimeField`)
- `guests` – number of guests (`IntegerField`)
- `message` – optional message (`TextField`, blank allowed)
- `status` – status of the booking (e.g. pending / confirmed / cancelled)

The model is managed through the Django admin interface.

---

## Technologies Used

- **Languages**
  - Python
  - HTML5
  - CSS3

- **Frameworks & Libraries**
  - Django
  - Bootstrap 5

- **Database**
  - SQLite (development)
  - Heroku Postgres (if configured for deployment)

- **Version Control & Deployment**
  - Git & GitHub
  - Heroku

---

## Testing

A separate `TESTING.md` file contains detailed information about:

- Manual testing of all views and user stories
- Form validation tests (valid and invalid input)
- Admin functionality
- Lighthouse and HTML validation

In short:

- All navigation links were tested to ensure they lead to the correct pages.
- The booking form was tested with:
  - Valid data
  - Dates in the past
  - Too few / too many guests
  - Missing required fields
- The admin panel was tested to:
  - View bookings
  - Update booking status

---

## Deployment

## Live Site

The live version of the project can be accessed here:
[MSE Sunshine Bistro – Live Site](https://mse-sunshine-bistro-1e8e5aa9f2b2.herokuapp.com/)

### Deployment Steps
1. Log in to GitHub and open your repository.
2. Choose the project you want to deploy.
3. Go to **Settings** > **Pages**.
4. Under **Source**, select **Deploy from a branch**.
5. Choose the `main` branch and the `/(root)` folder.
6. Click **Save**.
7. GitHub Pages will build and then publish the site (this may take a few moments).
8. Once finished, go back to your repository and navigate to the **Deployments** section.
9. Click on **github-pages** to open the live deployed site.

### Deployment to Heroku

1. Create a new Heroku app.
2. Connect the app to the GitHub repository.
3. Set config vars such as:
   - `SECRET_KEY`
   - `DISABLE_COLLECTSTATIC` (used during development; removed once static files are configured)
4. Choose the `main` branch to deploy from.
5. Click **Deploy Branch** to trigger a build.

> When static files are fully configured, `DISABLE_COLLECTSTATIC` is removed so that `python manage.py collectstatic` runs during the build.

---

## Credits

### Media

- The hero image on the home page was taken by the project author.

### Content

- All text content was written by the project author.

### Acknowledgements

- Code Institute for the project inspiration and learning material.

### Code & Inspiration

- Project structure and logic inspired by Code Institute's Django walkthrough projects.
- Bootstrap documentation used as a reference for layout and styling examples.