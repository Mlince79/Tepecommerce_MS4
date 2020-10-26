# Tepe - e-commerce

<img src="https://raw.githubusercontent.com/Mlince79/Tepecommerce_MS4/master/site/documentation/static/img/laptop-tablet-phone-pc.jpg" style="margin: 0;">

Tepe is Marcela's Ruiz Barba Illustrator artist first e-commerce website. She has an Instagram account and a Behance profile where she is always very active in updating new content.
With this page, she will be able to offer her followers the possibility to buy some of her illustrations. 
The site includes a page for her biography where people will be able to know more about her and a contact area for those who do not know her throw her social media channels.  

## UX

  * [Empathize](#Empathize)
  * [Define](#Define)
  * [Ideate](#Ideate)
  * [Prototype](#Prototype)
  * [Test](#Test)

### Empathize

Marcela and I are friends since we were in high school. We both took similar paths and spent several years working in advertising. 
She knew how she wants to present her work, so she gave me a draft which I used as a reference. 

<img src="https://raw.githubusercontent.com/Mlince79/Tepecommerce_MS4/master/site/documentation/static/img/draft.jpg" style="margin: 0;">

### Define

For this course, we decided to try to sell some of her illustrations within Europe. She will be printing a limited edition of each of her illustrations.

Users that will be buying her work are her followers and people looking for unique pieces made by her.

### Ideate

The website will allow her to update the new illustrations that she printed, and she will be able to categorize them as new. 
Based on her sales, she will be providing a rating to her pieces. 
The idea is to print more of the illustrations that customers like more and removed the ones that are not selling. 
The money earned from the prints will be the investment to produce more articles with her design.  
Users at this moment will not need to login, but there is a plan to add the login in the future. 

### Test 

The website has been tested with different users asking them to purchase an illustration. After those test some changes where made. 

## Existing Features
* Easy navigation
    - MY SHOP: easy access to the illustrations that are on sale.
    - ABOUT ME: information about Marcela's career. 
    - CONTACT ME: a way to send a direct email to Marcela's account.
* Trendy, intuitive design and user experience
Marcela's web design try to offer the user the feeling of visiting an online gallery. 
* Relevant, authoritative website content
Marcela has a very particular style that makes her site stand out from the others. She has worked towards a very original way to create her pieces. 
* Product visuals and descriptions
The detail of the product will show a description of her technique and the materials she used. 
* Social media as an extension of the business website
Instagram and Behance account will be present on each page.
* Shop
    - Product detail area will allow users to add items to their shopping bag.
    - Shopping bag, where users can add or remove items.
    - Checkout provides by stripe, where users can make their purchase.

<details>
    <summary>Click to see - User Stories Table</summary>

&nbsp;

User story ID | As a | Want to be able to... | So that I can...
--------------|---------|------------------------|-----------------
|             ||        **Viewing and Navegation**            ||
1 - | Shopper | View a list of illustrations | Select some to purchase
2 - | Shopper | View individual product details | Identify the price, description, product rating, illustration image
3 - | Shopper | Easily view the total of my purchase at any time | See how much I want to spend
|             || **Purchasing and Checkout** ||
4 - | Shopper | Easily select the quantity of a product when purchasing it. | Ensure I do not accidentally select the wrong product or quantity
5 - | Shopper | View items in my bag to be bought	| Identify the total cost of my articles and all items I will receive
6 - | Shopper | Adjust the number of individual items in my bag | Easily make changes to my purchase before checkout
7 - | Shopper | Easily enter my payment information | Check out quickly and with no hassles
8 - | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase 
9 - | Shopper | View an order confirmation after checkout | Verify that I haven't created any mistakes
10 - | Shopper | Receive an email confirmation after checking out | Keep the proof of what I've purchased for my records
|             || **Admin and Store Management** ||           |
11 - | Store Owner | Add an illustration | Add new illustrations in my web-shop
12 - | Store Owner | Edit/Update an illustration | Change image, prices and description
13 - | Store Owner | Delete an illustration | Remove illustrations that are sold out
</details>

### Features Left to Implement
<details>
    <summary>Click to see - User Stories to be implement Table</summary>

&nbsp;
User story ID | As a | Want to be able to... | So that I can...
--------------|---------|------------------------|-----------------
|                 || **Registration and User Accounts**	||		       |
1 | Site User | Easily register for an account | Have a personal account and be able to view my profile
2 | Site User | Easily login and logout | Access my personal information 
3 | Site User | Easily recover my password in case i forget it | Recover access to my account
4 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful 
5 | Site User | Have a personalized user profile | View my order history and order confirmations, and save my payment information
</details>

## Technologies Used
See requirements.txt
HTML5, CSS, Bootstrap.

## Testing
<details>
    <summary>Click to see user test</summary>

***Base Html***
- Display logo image.
- Display menu and active links after hover and after a click.
Display social media, Instagram and Behance and confirm active hover and working links opening a separate page. 

***Home***
- Display home image.

***My Shop***
- Display illustrations images. 
- Display button to sort illustrations by Price Low-High, Most Popular and New Illustrations.
- Confirm the functionality of the sort illustrations button.
- Confirm the display overlay is working on each image and showing the complete and correct information.

***My Shop/detail product***
- Display image illustration correctly.
- Display all the information about the piece correctly: name, price, size, rating, description.
- Display quantity button and be sure that customers can only allow buying 2 of each image. 
- Confirm that buttons Keep Shopping and Add to the bag are working. 
- Confirm those toast messages appears when adding a new item and when adding more items. 
- Confirm checkout outline border appears after adding the first item in the shopping bag. 
- Confirm checkout button is displayed and working correctly and showing the correct amount. 

***Bag***
- Shopping bag will display all the illustrations added to the bag. 
- Show: title, size, price quantity and subtotal of each image. 
- Show the correct total order amount to be pay, delivery cost and total, including delivery cost.
- Keep shopping and secure checkout button working. 

***Checkout***
- Checkout form displays correctly.
- Order summary shows the total amount of items. 
- Item includes name, size, quantity and subtotal: order total, delivery and total, including delivery cost. 
- The form has all the required fields. And show with a (*) the ones mandatory.
- Details: Full name and Email Address.
- Delivery: Phone number, Street Address 1 and 2, Town or City, Country, State or Locality Postal Code
- Country - Display all the nations. 
- Payment 
- Complete the order and adjust the bag button shows correctly and are working. 
- The message that shows the amount of money that will be a charge is displayed correctly and in red. 

***Checkout success***
- Order information is displayed. 
- A notification that an email has been sent is shown as well. 
- Toast message is displayed.
- Link to go-to products is displayed and working. 

***About***
- Display Marcelas illustration image.
- Display text.

***Contact***
- Display illustration image.
- Display form to contact. 
- Verification fields are active.
- Submit button working. 

***For the owner of the website***
- Will have access to products/add/ 
- Available login. A toast message will be shown after a successful login. 
- Access direct to Product Management, where the owner will be able to add new products by filling out the form. 
- Buttons of Cancel, Add Product, Sign Out will be active. 
- Cancel = Will redirect owner to the products section.
- Add Product = Will add a new product. 
- Sign Out = Owner will be able to logout. 
- Products section. The owner will be able to see her account active. On click, a dropdown will be displayed to have access to Product Management and logout. 
- The owner can edit or delete illustrations in the products detail page. 
- Sign out page, the owner will be able to logout or to go back to product management. After signing out, the owner will get a toast message and redirect to the homepage. 


</details>
[![Build Status](https://travis-ci.org/Mlince79/Tepecommerce_MS4.svg?branch=master)](https://travis-ci.org/Mlince79/Tepecommerce_MS4)

I tested the website user experience in different devices. 

# Errors: 
I have limited the number of shops to only two illustrations. As there is no inventory test implemented, the user can add more items to the shopping bag. 

## Deployment

<details>
    <summary>Click to see - Deployment Steps </summary>

### Local Development
* I used the gitpod-full-template from CODE INSTITUTE.
* Created my repository in Github. 
* I then opened my Gitpod to create my workspace there. 
    - I installed django 
    - And created my project 
* Created my .gitingore file and added the following:
    - env.py
    - *.sqlite3
    - *.pyc
    - __pychache__
* Create a env.py file to have my SECRET_KEY
* Did changes in settings.py
    * DEVELOPMENT=True
* Run `python3 manage.py runserver`
* I ran the initial migration and created a superuser to log into the admin. 
* Did the initial commit to Github.


### Stripe Payment in Local Development
* Set up a Stipe account
* Add js stripe code block
* The following keys should be add to env.py and Config Vars in Heroku 
    * STRIPE_PUBLIC_KEY=(From the test API key
    * STRIPE_SECRET_KEY=(From the test API key)
    * STRIPE_WH_SECRET=(From the endpoint made for Heroku)
* I made test to confirm that the pyment has succed. 


### Setting Up Email Google
* 2-step verification needs to be set, to create an app password specific to our Django app to allow to authenticate and use gmail account.
* Settings.py changes
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'boutiqueado@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')



### Deploy to Heroku
* Create a new app in Heroku
* In the Heroku website create a PostgreSQL
* Include it in env.py and include it in config.vars as DATABASE_URL=(Heroku database URI)
* Install dj_database_url, and psycopg2, gunicorn
* Settings.py

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default' : dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

DEBUG = development

if os.environ.get('DEVELOPMENT'):
    development = True
else:
    development = False


ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME'), 'localhost']

* Create Procfile 
* Add Stripe -> Developers -> Webhooks endpoint
* Set your other config vars
    * DATABASE_URL
    * EMAIL_HOST_USER
    * EMAIL_HOST_PASSWORD
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
* Conect App to GitHub


</details>

[Back To Top](#table-of-contents)
&nbsp;

## Credits

### Content
- The code of this project was created based on the boutiqueado [CODE INSTITUTE](https://github.com/ckz8780/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218)

### Media
- The design and illustrations are the owner (Marcela Ruiz Barba) materials
### Acknowledgements

- I received inspiration for this project from  [CODE INSTITUTE](https://github.com/ckz8780/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218)






