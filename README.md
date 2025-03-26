# Elite Escapes

**Elite Escapes** is a full-stack e-commerce website offering curated travel packages, built using Django and PostgreSQL.

---

## Table of Contents

- [Overview](#overview)
- [User Experience (UX)](#user-experience-ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Deployment](#deployment)
- [Local Development & Installation](#local-development--installation)
- [Credits](#credits)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

Elite Escapes is a full-stack e-commerce web application designed to provide users with an intuitive platform to explore and book exclusive travel packages conveniently online.

The website enables users to browse through a selection of curated holiday packages, view detailed itineraries, and securely complete bookings through Stripe's integrated payment system. Registered users can store personal details such as contact information and billing addresses, simplifying and speeding up future transactions.

Users have the option to subscribe to a newsletter for updates on new packages and special promotions. Automated email confirmations are sent following successful bookings, newsletter subscriptions and account registrations, enhancing user interaction and overall experience.

Administrative users have comprehensive control, with capabilities to add, update, or remove travel packages, manage customer accounts, and oversee website content efficiently.

Elite Escapes showcases practical skills in Django web development, PostgreSQL database management, secure online payments, responsive web design, and cloud-based deployment with Heroku and AWS S3, delivering a robust and engaging experience for both customers and administrators alike.

Deployed website: [Elite Escapes](https://elite-escapes-6cd7f36ee2af.herokuapp.com/)

![amiresponsive](static/images/readme-images/amiresponsive.png)

## User Experience (UX)

### Strategy

*(Define the purpose, target audience, and user goals.)*

Elite Escapes was designed to offer users a seamless online experience for exploring and booking exclusive travel packages. The website aims to simplify the booking process, provide clear information about available packages, and enable easy management of user bookings and personal information. The target audience includes both solo travelers but also families seeking convenient and trustworthy online booking services for premium and unforgetable holiday experiences.

### Scope

The key features of Elite Escapes were carefully selected to meet user expectations and enhance the overall booking experience:

- Browse through curated holiday packages.

- Securely book holidays online with integrated payment processing.

- Save personal details for faster and easier bookings in the future.

- Receive email updates for order confirmations and newsletter subscriptions.

- Efficient administrative management for packages and registered users.


#### User Flows

![user-flows-wf](static/images/readme-images/wireframes/user-flows.png)

### Structure

The website is structured intuitively to support effortless navigation and user interaction:

#### Landing Page

- Home/Holiday Packages: Allows users to browse available holiday options easily.

- Package Details: Provides in-depth information about each package.

#### Header | User Profile Icon Dropdown

- Bookings: Enables users to manage their bookings and personal details conveniently.

- Checkout: Seamless and secure payment process via Stripe integration.

- Admin Dashboard: Allows site administrators exclusively to manage packages, bookings and users efficiently.

- Personal Details: Provides the ability to store user details for future bookings and allows editing or deletion of the details as well.

- Contact Us: Offers a communication bridge between Customers and Elite Escapes.

#### Footer 

- Newsletter: Allows user to stay up to date with any new package arrivals and price drops or deals.

### Skeleton

The visual layout and structure of Elite Escapes were initially developed through wireframes and mock-ups, focusing on responsiveness, clarity, and usability. Key pages designed include:

#### Homepage and Package Listing wireframe
  
![homepage-wireframe](static/images/readme-images/wireframes/home.png)

#### Package Details wirefrarme 

![package-details-wf](static/images/readme-images/wireframes/package-details.png)

#### Customer Information form wireframe

![customer-info-form-wf](static/images/readme-images/wireframes/customer-details-form.png)

#### Personal Information wireframe

![personal-info-wf](static/images/readme-images/wireframes/personal-info.png)

#### Bookings page for users wireframe

![personal-bookings-wf](static/images/readme-images/wireframes/presonal-bookings.png)

#### Shopping bag wireframe

![shopping-bag-wf](static/images/readme-images/wireframes/shopping-bag.png)

#### Order Overview wireframe

![order-overview-wf](static/images/readme-images/wireframes/order-overview.png)

#### Contact Us wireframe

![contact-us-wf](static/images/readme-images/wireframes/contact-us.png)

#### Admin Dashboard wireframe

![admin-dashboard-wf](static/images/readme-images/wireframes/admin-dashboard.png)

#### Admin Dashboard Add/Edit Package wireframe

![add_edit-package-admin-wf](static/images/readme-images/wireframes/add_edit-package-admin.png)

#### Dropdown options wireframe

![dropdown](static/images/readme-images/wireframes/dropdown.png)

### Surface

A clean, professional aesthetic was chosen for Elite Escapes, emphasizing simplicity and readability. Specific design elements include:

- Typography: Clear, modern fonts for easy readability.
  - Lato

- Color Palette: Carefully selected colors to convey luxury, professionalism, and trustworthiness (e.g., gold, dark blue, white).

  ![coolors](static/images/readme-images/coolors.png)

- Imagery: High-quality, visually engaging images and features such as the carousel, to inspire and attract users.

## Features
### User authentication
#### Login

![login](static/images/readme-images/features/user-authentication/login.png)

#### Register

![register](static/images/readme-images/features/user-authentication/register.png)

#### Logout

![logout](static/images/readme-images/features/user-authentication/logout.png)

### Main Features
#### Hero Image

![hero](static/images/readme-images/features/main-features/hero-image.png)

#### Our Packages

![our-packages](static/images/readme-images/features/main-features/our-packages.png)

#### Package Details

![package-details](static/images/readme-images/features/main-features/package-details.png)

#### Reviews - Newsletter section

![reviews](static/images/readme-images/features/main-features/reviews-newsletter.png)

#### Shopping Bag - Booking Overview

![bag](static/images/readme-images/features/main-features/bag.png)

#### Order Overview

![order-overview](static/images/readme-images/features/main-features/order-overview.png)

#### Checkout
- This is done externally on Stripe hence not include in features

#### Bookings

![bookings](static/images/readme-images/features/main-features/bookings.png)

#### Personal Details

![personal-details](static/images/readme-images/features/main-features/personal-details.png)

#### Customer Details Form

![customer-details](static/images/readme-images/features/main-features/customer-details-form.png)

#### Delete Customers Details

![delete-customer-details](static/images/readme-images/features/main-features/delete-customer-details.png)

#### Contact Us

![contact-us](static/images/readme-images/features/main-features/contact-us.png)

### Admin Frontend
#### Admin Dashboard

![admin-dashboard](static/images/readme-images/features/admin-frontend/admin-dashboard.png)

#### Add Package

![add-package](static/images/readme-images/features/admin-frontend/add-package.png)

#### Edit Package

![edit-package](static/images/readme-images/features/admin-frontend/edit-package.png)

#### Delete Package

![delete-package](static/images/readme-images/features/admin-frontend/delete-package.png)


### Facebook Page

![fb-desk](static/images/readme-images/features/main-features/fb-desk.png)


## Technologies Used

- **Languages:**
  - Python
  - HTML5
  - CSS3
  - JavaScript
  
- **Frameworks & Libraries:**
  - Django
  - Bootstrap
  - jQuery
  - FontAwesome
  - TinyMCE

- **Databases:**
  - PostgreSQL (production)
  - SQLite (development)

- **Hosting & Deployment:**
  - Heroku
  - AWS S3 (for static/media files)

- **Payment Integration:**
  - Stripe

- **Other Tools:**
  - Git and GitHub
  - Django-Allauth (for authentication)
  - Django-Storages (AWS integration)

---

## Database Schema

*(Include a brief description or diagram (ERD) outlining the database models and their relationships.)*

---

## Testing

*(Explain your testing procedures, such as manual testing, automated tests, and responsiveness tests. Include steps or scenarios tested.)*

---

## Deployment

*(Comprehensive step-by-step instructions on how to deploy the project, including configuring Heroku, AWS S3 bucket setup, database setup, and Stripe integration.)*

## Deployment on Heroku

The following steps explain how to deploy **Elite Escapes** on Heroku using **Python 3.12.8**.

### 1. Create a Heroku App

1. Sign up or log in at [Heroku](https://www.heroku.com/).
2. Click **New** > **Create new app**.
3. Enter a unique app name (e.g., `elite-escapes`) and select a region (e.g., Europe), then click **Create app**.

---

### 2. Prepare the Project for Deployment

From your project's root directory, create or update the following files:

1. **`requirements.txt`** – contains Python dependencies.
2. **`Procfile`** – instructs Heroku how to run your app.
3. **`runtime.txt`** – specifies the Python runtime version.

Run these commands in your terminal:

```bash
pip freeze > requirements.txt
echo web: gunicorn elite_escapes.wsgi:application > Procfile
echo python-3.12.8 > runtime.txt
```

### 3. Initialize Git and Connect to Heroku

Run these commands in your terminal:

```bash
git init
git add .
git commit -m "Initial commit for Heroku deployment"
```

To link local repository to heroku run:

```bash
heroku git:remote -a elite-escapes
```

### 4. Configure Heroku Settings (Config Vars)

In your Heroku dashboard:

  1. Go to Settings.

  2. Click Reveal Config Vars.

  3. Add the following variables (adjust as needed):

      - **SECRET_KEY:**	A random, secure Django secret key

      - **AWS_ACCESS_KEY_ID:**	Your AWS S3 access key

      - **AWS_SECRET_ACCESS_KEY:**	Your AWS S3 secret key

      - **AWS_STORAGE_BUCKET_NAME:**	Your AWS S3 bucket name

      - **STRIPE_TEST_PUBLIC_KEY:**	Your Stripe public key (test mode)

      - **STRIPE_TEST_SECRET_KEY:**	Your Stripe secret key (test mode)
      
      - **STRIPE_WH_SECRET:**	Your Stripe webhook secret

      - **EMAIL_HOST_USER:**	Your email (SMTP)

      - **EMAIL_HOST_PASSWORD:**	Your email password or app password

  ### 5. Add ProsteSQL Database
  1. Navigate to Resources in your Heroku app dashboard.

  2. Under Add-ons, search for Heroku Postgres.

  3. Select the Hobby Dev (free) plan and click Provision.

  4. A DATABASE_URL variable is now added under Config Vars.
  ---

  ### 6. Deploy to Heroku
  ```bash
  git push heroku main
  ```

  Apply migrations:  
  ```bash
  heroku run python manage.py migrate
  ```

  Create superuser:
  ```bash
  heroku run python manage.py createsuperuser
  ```

  ### 7. Set Up Static Files
  ```bash
  heroku run python manage.py collectstatic
  ```

  ### 8. Access Deployed site
  
  Navigate to: https://elite-escapes-6cd7f36ee2af.herokuapp.com/
  If all went well the page should be up and runnning
  
## Local Development & Installation

*(Guide users on how to clone the repository and run the project locally.)*

Example:

```bash
# Clone the repository
git clone https://github.com/Alexiou981/elite-escapes.git

# Change directory
cd elite-escapes

# Install dependencies
pip install -r requirements.txt

# Set environment variables
Create a `.env` file based on the provided `.env.example`

# Apply database migrations
python manage.py migrate

# Run development server
python manage.py runserver


## Credits

PACKAGE IMAGES

Hero Image was uploaded by Pixabay, source:
https://www.pexels.com/photo/brown-hut-island-gazebo-38238/

Santorini_1 was uploaded by Alejandro Gonzlaez, source:https://unsplash.com/photos/a-white-church-with-a-cross-on-top-of-it-bomAA5xYJE0

Santorini_2 was uploaded by geraldfriedrich2, source:
https://pixabay.com/photos/greece-sea-santorini-summer-houses-2197996/

Santorini_3 was uploaded by nextvoyage, source:https://pixabay.com/photos/santorini-city-greece-landscape-4044972/

Santorini_4 was uploaded by olwjddn, source:https://pixabay.com/photos/travel-greece-santorini-wallpapers-2870524/

Santorini_5 was uploaded by EzPzPics, source:https://pixabay.com/photos/santorini-greece-flag-greek-island-1948680/

Santorini_6 was uploaded by Pat_Photographies, source:https://pixabay.com/photos/oia-santorini-greece-travel-white-4372057/



Kyoto_1 was uploaded by mafutto, source:
https://pixabay.com/photos/japan-kyoto-shimogamo-shrine-shrine-1459534/

Kyoto_2 was uploaded by OnkelP, source:
https://pixabay.com/photos/japan-asia-temple-kyoto-landmark-4583669/

Kyoto_3 was uploaded by GPoulsen, source:https://pixabay.com/photos/japan-asia-temple-kyoto-landmark-4583669/

Kyoto_4 was uploaded by derwiki, source:https://pixabay.com/photos/japanese-asia-foliage-ancient-1409839/

Kyoto_5 was uploaded by kjmhdk66112, source:https://pixabay.com/photos/jizo-cute-enkoji-temple-kyoto-2794143/

Kyoto_6 was uploaded by jackmac34, source:
https://pixabay.com/photos/japan-kyoto-zen-pond-pine-4649390/

Kyoto_7 was uploaded by Ramapo, source:https://pixabay.com/photos/bird-japanese-white-eye-3861072/

Kyoto_8 was uploaded by bossladydunmyer, source:https://pixabay.com/photos/japan-cat-gotokuji-lucky-cat-4883346/




Paris_1 was uploaded by nuno_lopes, source:https://pixabay.com/photos/eiffel-tower-france-paris-landscape-975004/

Paris_2 was uploaded by Pignatta, source:https://pixabay.com/photos/montmartre-basilica-paris-france-6510653/

Paris_3 was uploaded by ChiemSeherin, source:
https://pixabay.com/photos/fountain-water-city-square-8318963/

Paris_4 was uploaded by PeggyMarco, source:https://pixabay.com/photos/france-paris-bridge-its-1930719/

Paris_5 was uploaded by LagrangeHerve, source:https://pixabay.com/photos/arc-de-triomphe-monument-paris-7213188/




Maldives_1 was updated by SuzyT, source:https://pixabay.com/photos/veligandu-island-maldives-veligandu-1044366/

Maldives_2 was uploaded by Webkims, source:
https://pixabay.com/photos/maldive-islands-beach-day-off-ocean-2190384/

Maldives_3 was uploaded by FonthipWard, source:
https://pixabay.com/photos/maldives-beach-coconut-white-sand-260686/

Maldives_4 was uploaded by makabero, source:
https://pixabay.com/photos/deck-chairs-parasol-vacation-ocean-6613331/

Maldives_5 was uploaded by Fonthi[Ward, source:https://pixabay.com/photos/maldives-beach-holiday-vocation-261506/

Maldives_6 was uploaded by da1374, source:https://pixabay.com/photos/palma-maldives-beach-231140/

Maldives_7 was uploaded by Csehokel, source:
https://pixabay.com/photos/ship-maldives-ocean-2083710/

Maldives_8 was uploaded by SuzyT, source:
https://pixabay.com/photos/maldives-lagoon-blue-paradise-1044368/

Maldives_9 was uploaded by romaneau, source:
https://pixabay.com/photos/maldives-isle-beach-sun-holiday-666118/




Iceland_1 was uploaded by Noel_Bauza, source:
https://pixabay.com/photos/aurora-polar-lights-northern-lights-1185464/

Iceland_2 was uploaded by Noel_Bauza, source:
https://pixabay.com/photos/christmas-background-aurora-1190254/

Iceland_3 was uploaded by andersgaard, source:
https://pixabay.com/photos/northern-lights-aurora-borealis-4966913/

Iceland_4 was uploaded by Kanenori, source:
https://pixabay.com/photos/sunset-mountain-tateyama-2177324/

Iceland_5 was uploaded by chriszwettler, source:https://pixabay.com/photos/sunset-mountain-tateyama-2177324/

Iceland_6 was uploaded by chriszwettler, source:
https://pixabay.com/photos/nature-adventure-hike-travel-6817376/

Iceland_7 was uploaded by Pexels, source:
https://pixabay.com/photos/woman-adventure-ice-cave-cold-1850094/




NewYork_1 was uploaded by davidvives90, source:https://pixabay.com/photos/new-york-city-night-light-7577186/


NewYork_2 was uploaded by Javaistan, source:https://pixabay.com/photos/empire-state-building-new-york-city-6675010/

NewYork_3 was uploaded by wiggijo, source:
https://pixabay.com/photos/usa-manhattan-contrasts-new-york-1777986/

NewYork_4, source:
https://pixabay.com/photos/new-york-city-urban-cityscape-2263343/

NewYork_5, source:https://pixabay.com/photos/brooklyn-bridge-suspension-bridge-105079/

NewYork_6 was uploaded by Michelle_Raponi, source:
https://pixabay.com/photos/skyscrapers-new-york-city-manhattan-8853215/

NewYork_7 was uploaded by Pexels, source:
https://pixabay.com/photos/pedestrians-crossing-traffic-1853552/

NewYork8, source:
https://pixabay.com/photos/brooklyn-bridge-suspension-bridge-105079/




Dubai_1 was uploaded by Olgaozik, source:
https://pixabay.com/photos/downtown-dubai-uae-tourism-city-4045035/

Dubai_2 was uploaded by Olgaozik, source:
https://pixabay.com/photos/downtown-dubai-uae-tourism-city-4045037/

Dubai_3 was uploaded by BS1920, source:
https://pixabay.com/photos/dubai-desert-burj-kalifa-emirates-2057583/

Dubai_4 was uploaded by julgen1981, source:
https://pixabay.com/photos/landscape-architecture-building-4191991/

Dubai_5 was uploaded by JESHOOTS-com, source:
https://pixabay.com/photos/burj-khalifa-emirates-dubai-uae-2212978/

Dubai_6 was uploaded by next voyager, source:
https://pixabay.com/photos/burj-khalifa-emirates-dubai-uae-2212978/





Peru_1 was uploaded by KinErniquez, source:
https://pixabay.com/photos/peru-tourism-cuzco-landscape-5143632/

Peru_2 was uploaded by FlavioMoura, source:
https://pixabay.com/photos/peru-machu-picchu-andes-inca-2237651/

Peru_3 was uploaded by Info888mari, source:
https://pixabay.com/photos/nature-travel-exploration-6875147/

Peru_4 was uploaded by Poswiecie, source:
https://pixabay.com/photos/machu-picchu-peru-inca-travel-2773629/

Peru_5 was uploaded by Eyelenses, source:
https://pixabay.com/photos/nature-travel-exploration-6875147/

Peru_6 was uploaded by santibertola, source:
https://pixabay.com/photos/llamas-peru-animals-machu-picchu-451195/

Peru_7 was uploaded by MLbay, source:
https://pixabay.com/photos/lama-machu-picchu-landscape-inca-5223959/




SA_1 was uploaded by jeanvdmeulen, source:
https://pixabay.com/photos/table-bay-harbour-cape-town-dawn-3541607/

SA_2 was uploaded by fungaifoto, source:
https://pixabay.com/photos/penguins-south-africa-cape-town-4668754/

SA_3 was uploaded by D_Van_Rensburg, source:
https://pixabay.com/photos/sunset-table-mountain-landscape-sky-5004905/

SA_4 was uploaded by sharonang, source:
https://pixabay.com/photos/helicopter-ride-flight-exciting-1218974/

SA_5 was uploaded by martinaH79, source:
https://pixabay.com/photos/south-africa-cape-town-2267795/

SA_6 was uploaded by cocoparisienne, source:
https://pixabay.com/photos/elephants-animal-elephant-herd-1092508/

SA_7 was uploaded by IanZA, source:
https://pixabay.com/photos/zebras-wildlife-africa-tourism-2791965/

SA_8 was uploaded by DEZALB, source:
https://pixabay.com/photos/south-africa-park-kruger-giraffe-1533414/

SA_9 was uploaded by IanZa:
https://pixabay.com/photos/lion-africa-nature-wildlife-kruger-2793122/



Bali_1 was uploaded by 12_34_56, source:
https://pixabay.com/photos/indonesia-bali-temple-balinese-gate-8788501/

Bali_2 was uploaded by Michelle_Raponi, source:
https://pixabay.com/photos/ubud-indonesia-temple-bali-history-277349/

Bali_3 was uploaded by kienhau, source:
https://pixabay.com/photos/bali-indonesia-kelingking-sea-7969001/

Bali_4 was uploaded by wahyua34, source:
https://pixabay.com/photos/beach-bali-nusa-penida-indonesia-7411683/

Bali_5 was uploaded by DEZALB, source:https://pixabay.com/photos/indonesia-bali-ulun-danu-1578647/

Bali_6 was uploaded by MadebyNastia, source:
https://pixabay.com/photos/pagoda-temple-lake-travel-3240169/

Bali_7 was uploaded by Michelle_Raponi, source:https://pixabay.com/photos/kuta-bali-indonesia-pantai-kuta-277350/

Bali_8 was uploaded by astama81, source:
https://pixabay.com/photos/gapura-gilimanuk-bali-indonesia-198557/

Bali_9 was uploaded by frejka, source:
https://pixabay.com/photos/barong-bali-dance-theatre-ritual-648093/





Rome_1 was uploaded by JerOme82, source:
https://pixabay.com/photos/rome-vatican-place-landscape-italy-5074421/

Rome_2 was uploaded by G-tech, source:
https://pixabay.com/photos/architecture-pillars-historical-4392174/

Rome_3 was uploaded by theabstractvibe, source:
https://pixabay.com/photos/rome-architecture-sunlight-building-4989538/

Rome_4 was uploaded by jdegheest, source:
https://pixabay.com/photos/trevi-fountain-fountain-rome-art-2796710/

Rome_5 was uploaded by Kookay, source:https://pixabay.com/photos/rome-italy-city-houses-buildings-4087275/

Rome_6 was uploaded by Walkerssk, source:
https://pixabay.com/photos/rome-vatican-italy-1945033/

Rome_7 was uploaded by javierAlamo, source:
https://pixabay.com/photos/rome-vatican-italy-1945033/

Rome_8 was uploaded by Emphyrio, source:
https://pixabay.com/photos/rome-bridge-italy-architecture-4691274/

Banff_1 was uploaded by GPoulsen, source:https://pixabay.com/photos/bow-river-banff-nature-river-6888321/

Banff_2 was uploaded by Sonyuser, source:
https://pixabay.com/photos/mountains-river-banff-trees-forest-5936682/

Banff_3 was uploaded by randogrigri, source:https://pixabay.com/photos/lake-mountains-winter-banff-canada-7588123/

Banff_4 was uploaded by Ri_Ya, source:
https://pixabay.com/photos/snowboarding-ski-resort-slopes-4763731/

Banff_5 , source:
https://pixabay.com/photos/cross-country-skiing-skiers-ski-5908416/

Banff_6 was uploaded by Up-Free, source:
https://pixabay.com/photos/man-skier-ski-skiing-snow-slopes-498473/

Banff_7 was uploaded by gsibergerin, source:
https://pixabay.com/photos/nature-winter-snow-ski-vorarlberg-4046557/

## Tutorials and Walkthroughs:

