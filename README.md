# Sip_Out_Loud_P5

![Website Mockup](assets/images/readme/mockup.png)

[This is a link to the live website]()


## Table Of Contents
- [Introduction](#introduction)
- [Design](#design) 
  * [User Feedback](#user-feedback)
- [Application Features](#application-features)
  * [Data/APIs Used](#dataapis-used)
- [UX (User Experience)](#user-experience)
- [Accessibility](#accessibility)
- [Future Features](#future-features)
- [Testing](#testing)  
- [Deployment](#deployment)
- [Technologies](#technologies)
- [Code](#code)  
- [Credits for images](#credits-for-images) 
- [Acknowledgements](#acknowledgements) 


## Introduction
Sip Out Loud is a premium online store offering a curated selection of spirits, including gin, vodka, whiskey, and wine. Designed with a modern and user-friendly interface, this e-commerce platform allows customers to explore various collections, filter products, and seamlessly complete their purchases. Whether you're a connoisseur or a casual enthusiast, Sip Out Loud brings a seamless and stylish way to discover and purchase your favorite spirits online.

## Design 
Sip Out Loud features a sleek and modern design that aligns with the premium nature of the brand. The visual aesthetic combines elegant typography, a sophisticated color palette, and high-quality product imagery to create an immersive browsing experience.

### 1. Key Design Elements:
Color Scheme: A refined blend of deep, rich tones complemented by subtle accents, reinforcing a sense of luxury and exclusivity.

**Typography** : Clean, modern fonts that enhance readability while maintaining an upscale feel.
**Product Display**: A visually appealing grid layout showcasing high-quality product images with essential details such as alcohol percentage, volume, and rating.
**Navigation**: Intuitive navigation with category-based browsing (Gin, Vodka, Whiskey, Wine) and sorting options for user convenience.
**Call-to-Action Buttons**: Stylish and well-placed buttons like "See Collection" and "Add to Bag", designed to enhance user engagement and encourage seamless shopping.

The design ensures a user-friendly and visually immersive experience, making it easy for customers to explore and purchase their favorite spirits effortlessly.

**Homepage Wireframe**  
  ![Homepage Wireframe](docs/wireframes/homepage.png)  

**Category Page Wireframe (Gin, Vodka, Whiskey, Wine)**  
  ![Category Page Wireframe](docs/wireframes/category.png)  

**Product Detail Page Wireframe**  
  ![Product Detail Page Wireframe](docs/wireframes/product_detail.png)  

### 2. Design Inspiration  
The design of *Sip Out Loud* is inspired by **modern e-commerce liquor stores**, featuring:  

- A **dark, premium aesthetic** with navy blue and light blue tones.  
- A **minimalist layout** for an elegant shopping experience.  
- **High-quality images** of liquors for a visually appealing interface.

### 3. Final UI Screenshots  
Below are screenshots of the final design after implementation:  

- **Homepage**  
  ![Homepage Screenshot](docs/screenshots/homepage.png)  

- **Category Page (Gin, Vodka, Whiskey, Wine)**  
  ![Category Page Screenshot](docs/screenshots/category.png)  

- **Product Details Page**  
  ![Product Details Screenshot](docs/screenshots/product_detail.png)  

- **Shopping Cart & Checkout Page**  
  ![Checkout Page Screenshot](docs/screenshots/checkout.png)  
 
## User Feedback  

User feedback played a crucial role in refining the **Sip Out Loud** project. Throughout development, feedback was collected through **user testing, surveys, and real-world interactions**. Below are the key insights and improvements made based on user input:

### ✅ Positive Feedback  
- **Aesthetic & Branding** – Users appreciated the **dark, elegant color scheme** and **high-quality images**, which created a premium shopping experience.  
- **Navigation & UX** – The **"See Collection"** buttons and **category pages** made it easy to browse different liquors.  
- **Product Display** – Users liked the **detailed product pages** with information such as alcohol percentage, volume, and rating.  

### 🔹 Areas of Improvement  
- **Sorting & Filtering** – Some users requested additional sorting methods (e.g., **price range, rating, alcohol percentage**), which were later added.  
- **Mobile Responsiveness** – Early testing revealed **minor layout issues** on smaller screens, which were adjusted for a better mobile experience.  
- **Cart & Checkout Process** – Users suggested **clearer feedback** when adding items to the cart, leading to the enhancement of the **"Add to Bag" button** styling.  

### ✔ Implemented Changes  
- **Added Sorting Options** – Users can now sort by **price, rating, and volume**.  
- **Improved Mobile Experience** – Layouts were optimized for seamless browsing on mobile devices.  
- **Enhanced "Add to Bag" Feedback** – A **visual confirmation** now appears when adding a product to the cart.  


## Application Features

### 1. User Authentication & Profile Management  
- Secure user registration and login system.  
- Users can reset passwords via email.  
- Profile dashboard for managing personal details and order history.  

### 2. Product Browsing & Filtering  
- Users can browse a wide range of alcoholic beverages, including Gin, Vodka, Whiskey, and Wine.  
- Categories are well-structured for easy navigation.  
- Sorting options available (e.g., by price, rating, or alcohol percentage).  

### 3. Product Detail & Reviews  
- Each product has a dedicated page displaying details such as SKU, alcohol percentage, volume, rating, and an image.  
- Users can leave reviews and rate products.  

### 4. Shopping Cart & Checkout  
- Seamless "Add to Bag" functionality with real-time updates.  
- Secure Stripe payment integration.  
- Order summary before confirming purchases.  

### 5. Order Management  
- Users receive email confirmations for successful orders.  
- Admins can manage orders through the Django admin panel.  

### 6. Responsive Design  
- Fully optimized for mobile, tablet, and desktop viewing.  
- Stylish UI with a modern aesthetic.  

### 7. Admin & Management Features  
- Admins can add, edit, and delete products from the database.  
- Order management tools available in the Django admin dashboard.  

### 8. User Feedback & Improvements  
- Implemented features based on user feedback to enhance UX.  
- Improved navigation, search functionality, and design refinements.  

## Backend Logic

The backend of the **Sip Out Loud** application is built using **Django**, following the **Model-View-Template (MVT)** architecture. Below is an overview of the key backend functionalities:

### 1. **Database Models (PostgreSQL)**
- The application uses a **PostgreSQL** database to store product data, user information, and order details.  
- Key models include:
  - `Category`: Defines product categories (Gin, Vodka, Whiskey, Wine).
  - `Product`: Stores details such as `sku`, `name`, `description`, `price`, `alcohol_percentage`, `volume_ml`, `rating`, and `image`.
  - `Order`: Tracks user purchases with related items and payment details.
  - `UserProfile`: Stores user data and order history.

### 2. **Authentication & Authorization**
- Django’s built-in authentication system is used for **user registration, login, logout**, and **password reset**.  
- Admin users have access to manage products, orders, and users via the **Django Admin Panel**.  
- CSRF and session management ensure security.

### 3. **Product Management**
- Products are dynamically retrieved and displayed based on categories.
- Sorting and filtering logic allows users to refine their searches.
- Each product has a detailed view, including ratings and reviews.

### 4. **Shopping Cart & Checkout**
- Users can **add, update, and remove items** from their shopping cart.
- Cart items are stored using Django sessions.
- Secure **Stripe payment integration** processes transactions.
- Once an order is placed, users receive a **confirmation email**.

### 5. **Order Processing & Webhooks**
- Orders are saved in the database upon successful payment.
- Stripe **webhooks** handle payment confirmation and updates order status.
- Users can view past orders in their profile.

### 6. **Admin Management**
- Admin users can **add, update, and delete** products through Django Admin.
- Order status can be managed (e.g., processing, shipped, delivered).
- Custom admin filters improve data management.

### 7. **Error Handling & Security**
- Custom error pages (404, 500) provide a better user experience.
- Form validation prevents incorrect inputs.
- Data encryption ensures sensitive information is protected.

### 8. **Performance Optimizations**
- Cached queries improve database performance.
- Images are stored efficiently using **Cloudinary** (or similar services).
- Asynchronous tasks (via Celery, if used) handle background processing.

The backend ensures a **secure, scalable, and high-performance** experience for users, while also providing **robust admin tools** for product and order management.

## User Experience: First-Time User

As a first-time user of **Sip Out Loud**, the experience is designed to be **intuitive, engaging, and seamless**. From browsing collections to completing a purchase, users can navigate effortlessly.

### 1. **Landing on the Homepage**
- Users are greeted with a **visually appealing homepage**, featuring high-quality images of premium spirits.
- A **clear navigation bar** allows quick access to categories like **Gin, Vodka, Whiskey, and Wine**.
- A **hero section** invites users to explore the collection with a **"See Collection"** button.

### 2. **Browsing Products**
- Users can view a **well-organized product catalog** with filters and sorting options.
- Each product page provides **detailed information**, including:
  - Alcohol percentage.
  - Volume (ml).
  - Ratings & reviews.
  - Pricing.
  - High-resolution images.

### 3. **User Registration & Authentication**
- First-time users can create an account using a **simple sign-up form**.
- **Social authentication** (Google, Facebook, etc.) is available for quick access.
- Upon registration, users receive a **welcome email**.

### 4. **Adding Items to the Cart**
- Users can add products to their bag using a **visually appealing "Add to Bag" button**.
- A **cart summary** is available at all times in the navigation bar.
- Users can **increase or decrease quantities** or **remove items** before checkout.

### 5. **Checkout & Payment**
- A guided **checkout process** ensures ease of use.
- Secure **Stripe payment integration** allows users to pay with their preferred method.
- Users receive an **order confirmation email** with purchase details.

### 6. **Post-Purchase Experience**
- Users can track their orders from their **profile dashboard**.
- A **thank-you page** with personalized recommendations enhances engagement.
- Registered users can **leave product reviews** and provide feedback.

### 7. **Mobile-Friendly Experience**
- The site is **fully responsive**, ensuring a smooth experience on **smartphones and tablets**.
- The navigation and buttons are optimized for **touch interaction**.

### 8. **Help & Support**
- A dedicated **FAQ page** answers common questions.
- A **contact form** allows users to reach out for inquiries or support.

This **first-time user journey** ensures that newcomers feel **welcomed, informed, and confident** while navigating and purchasing from **Sip Out Loud**. 🍷🥃


### As a Returning User:
1. **Report Generation:**

  -Generate booking summaries and reports for administrative purposes.

2. **Admin Panel:**
  - Generate booking summaries and reports for administrative purposes.

## Accessibility
- Color Contrast: The system ensures proper color contrast for readability, especially for users with visual impairments.
-  Keyboard Navigation: All functionality can be accessed via keyboard for users with mobility challenges.
- Screen Reader Compatibility: All critical content is accessible via screen readers to ensure inclusivity for users with disabilities.
- Error Messages: Detailed error messages are provided to guide users in correcting any issues with their input.

## Future Features
- Payment Gateway Integration: Allow users to pay for bookings directly through the system.
- Multi-Room Booking: Enable guests to book multiple rooms in one transaction.
- Email Notifications: Automatically send booking confirmations and updates to users.
- Mobile Application: Develop a mobile version of the platform for on-the-go booking.
- Admin Dashboard Enhancements: Add graphs and detailed statistics for room occupancy and revenue tracking.

## Testing
### User story Testing
- Login: Testing valid and invalid login attempts.
- Booking Process: Confirming that total costs are calculated correctly and that bookings are saved.
- Admin Access: Ensuring that admin can view and modify bookings without issues.

### Feature Testing
- Room Selection: Ensured that the system correctly filters rooms by availability and displays relevant details.

[CI Python Linter](https://pep8ci.herokuapp.com/#)

![python validation](assets/images/readme/python_validation.png)

## Deployment
### Heroku

1. Sign into [Heroku](https://dashboard.heroku.com/apps)
2. On the right side click **New** and select **Create new app**
3. Create a new Heroku app with a unique name. Heroku will generate a random name if you don't specify one and select your region.
4. Click **Create app**
5. Close to the top select **Settings**, click on *Reveal Config Vars**
  - On **Key** and **Value** input fields enter PORT and Paste everything copied from the **creds.json** folder in your gitpod workspace(respectively).
6. Click **add** to create another set of KEY and VALUE.
  - In the input fields add KEY: PORT, VALUE: 8000
7. At the bottom, click **Add buildpack**, from the options select **python** and **nodejs** + **add buildpack** after selecting each.
8. Close to the top where you clicked **Settings** this time click **Deploy**, click **connect to github**.
  - search for the name of the repository you want to deploy and click **connect**
9. Click **deploy branch**

## Technologies
- Github for the source code.
- VsCode for creating the website.
- Django: Web framework for backend logic and server-side functionality.
- Code Institute's Gitpod Template
- Heroku for deployment
- Code institute learnings
- Techsini to create a mockup of the website
- Unsplash for images
- PostgreSQL: Database for storing user and booking data.
- HTML/CSS/JavaScript: Frontend design and interactivity.
- amazon aws
- stripe

## Code
- [Code Institute](https://learn.codeinstitute.net/dashboard)
- Tutorial videos- Programming with Mosh [YouTube](https://www.youtube.com/@programmingwithmosh)

## Credits for images
** All images came from [Unsplash](https://unsplash.com/)
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

## Acknowledgement
- I would like to thank my Mentor Mr Precious for his guidance and advice.

- A big thanks to Slack Community for for always being someone willing to answer my questions.

- A big thank you to the Code Institute team for their constant support and resources that made this project possible.