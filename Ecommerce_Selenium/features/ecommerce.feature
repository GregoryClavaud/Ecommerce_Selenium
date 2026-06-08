Feature: Ecommerce Selenium

    @TC1
    Scenario: Test case 1 : Register User
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        Then New User Signup! est visible
        When Je mets le username et l'email
        | username | email            |
        | gbob     | gbob34@gmail.com |
        And Je clique sur le bouton Signup
        Then ENTER ACCOUNT INFORMATION est visible
        When Je mets les informations d'inscription
        | password | jourAnniversaire | moisAnniversaire | anneeAnniversaire | firstname | lastname | address        | country | state      | city  | zipcode | phone      |
        | 1234     | 10               | February         | 1994              | Bob       | David    | 3 rue des pain | Canada  | Val d'oise | Cergy | 95000   | 0123654789 |
        And Je clique sur le bouton Create ACCOUNT
        Then ACCOUNT CREATED! est visible
        When Je clique sur le bouton Continue pour finaliser l'inscription
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible
        And Je clique sur le bouton Continue pour finaliser la suppression

    @TC2
    Scenario: Test Case 2: Login User with correct email and password
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        Then Login to your account est visible
        When Je mets un email et un mot de passe correct
        | email                 | password |
        | stevea@gmail.com      | 1234     |
        And Je clique sur le bouton Login
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible

    @TC3
    Scenario: Test Case 3: Login User with incorrect email and password
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        Then Login to your account est visible
        When Je mets un email et un mot de passe incorrect
        | email                 | password   |
        | jean@gmail.com        | azerty     |
        And Je clique sur le bouton Login
        Then Le message Your email or password is incorrect! est visible

    @TC4
    Scenario: Test Case 4: Logout User
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        Then Login to your account est visible
        When Je mets un email et un mot de passe correct
        | email                 | password |
        | stevea@gmail.com      | 1234     |
        And Je clique sur le bouton Login
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Logout
        Then Je suis sur la page "https://automationexercise.com/login"
    
    @TC5
    Scenario: Test Case 5: Register User with existing email
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        Then New User Signup! est visible
        When Je mets le username et l'email d'un compte existant
        | username   | email             |
        | Asteve     | stevea@gmail.com  |
        And Je clique sur le bouton Signup
        Then Le message Email Address already exist! est visible
    
    @TC6
    Scenario: Test Case 6: Contact Us Form
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Contact US
        Then GET IN TOUCH est visible
        When Je mets mes informations à transmettre
        | name     | email             | subject               | message                     |
        | Steve    | stevea@gmail.com  | Problème de connexion | J'arrive pas à me connecter |
        And J'upload un fichier
        And Je clique sur le bouton Submit
        And Sur le bouton OK sur la fenêtre qui vient d'apparaître
        Then Le message Success! Your details have been submitted successfully est visible
        When Je clique sur le bouton Home
        Then Je suis sur la page "https://automationexercise.com/"

    @TC7
    Scenario: Test Case 7: Verify Test Cases Page
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Test Cases
        Then Je suis sur la page "https://automationexercise.com/test_cases"

    @TC8
    Scenario: Test Case 8: Verify All Products and product detail page
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Products
        Then Je suis sur la page "https://automationexercise.com/products"
        And La liste des produits est visible
        When Je clique sur View Product du premier produits
        Then Je suis sur la page "https://automationexercise.com/product_details/1"
        And Je vérifie que les détails du produit sont visibles
        | name         | category     | price   | availability | condition | brand |
        | Blue Top     | Women > Tops | Rs. 500 | In Stock     | New       | Polo  |

    @TC9
    Scenario: Test Case 9: Search Product
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Products
        Then Je suis sur la page "https://automationexercise.com/products"
        When Je rentre le nom du produit recherché
        | search product |
        | Tshirt         |
        And Je clique sur le bouton Search
        Then SEARCHED PRODUCTS est visible
        And La liste des produits est visible
    
    @TC10
    Scenario: Test Case 10: Verify Subscription in home page
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je scroll en bas de page
        Then SUBSCRIPTION est visible
        When Je rentre un email
        | email            |
        | stevea@gmail.com |
        And Je clique sur la flèche à coté
        Then You have been successfully subscribed! est visible

    @TC11 
    Scenario: Test Case 11: Verify Subscription in Cart page
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Cart
        And Je scroll en bas de page
        Then SUBSCRIPTION est visible
        When Je rentre un email
        | email            |
        | stevea@gmail.com |
        And Je clique sur la flèche à coté
        Then You have been successfully subscribed! est visible

    @TC12
    Scenario: Test Case 12: Add Products in Cart
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Products
        And Je clique sur le bouton Add to cart du premier produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Add to cart du second produit
        And Je clique sur le bouton View Cart
        Then Je verifie mon panier
        | id | name       | price   | quantity | total price |
        | 1  | Blue Top   | Rs. 500 | 1        | Rs. 500     |
        | 2  | Men Tshirt | Rs. 400 | 1        | Rs. 400     |

    @TC13 
    Scenario: Test Case 13: Verify Product quantity in Cart
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Products
        And Je clique sur View Product du premier produits
        Then Je vérifie que les détails du produit sont visibles
        | name         | category     | price   | availability | condition | brand |
        | Blue Top     | Women > Tops | Rs. 500 | In Stock     | New       | Polo  |
        When J'augmente la quantité à 4
        And Je clique sur le bouton Add to cart
        And Je clique sur le bouton View Cart
        Then Je verifie mon panier contient la bonne quantité est de 4
    
    @TC14
    Scenario: Test Case 14: Place Order: Register while Checkout
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Add to cart du premier produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Add to cart du second produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Cart
        Then Je suis sur la page "https://automationexercise.com/view_cart"
        When Je clique sur le bouton Proceed to checkout
        And Je clique sur Register/Login de l'alerte qui vient d'apparaître
        And Je mets le username et l'email
        | username | email            |
        | gbob     | gbob34@gmail.com |
        And Je clique sur le bouton Signup
        And Je mets les informations d'inscription
        | password | jourAnniversaire | moisAnniversaire | anneeAnniversaire | firstname | lastname | address        | country | state      | city  | zipcode | phone      |
        | 1234     | 10               | February         | 1994              | Bob       | David    | 3 rue des pain | Canada  | Val d'oise | Cergy | 95000   | 0123654789 |
        And Je clique sur le bouton Create ACCOUNT
        Then ACCOUNT CREATED! est visible
        When Je clique sur le bouton Continue pour finaliser l'inscription
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Cart
        And Je clique sur le bouton Proceed to checkout
        Then Je vérifie que l'adresse et les produits sont les bons
        | name       | price   | quantity | total price |
        | Blue Top   | Rs. 500 | 1        | Rs. 500     |
        | Men Tshirt | Rs. 400 | 1        | Rs. 400     |
        And Je mets une description
        | description |
        | blabla      |
        When Je clique sur le bouton Place order
        And Je rentre les informations de paiements
        | name | number    | cvc | expiry mounth | expiry year |
        | Bob  | 1234 5422 | 253 | 02            | 2027        |
        And Je clique sur le bouton Pay and confirm
        Then Le message Your order has been placed successfully! est visible
        When Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible
        And Je clique sur le bouton Continue pour finaliser la suppression

    @TC15
    Scenario: Test Case 15: Place Order: Register before Checkout
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        And Je mets le username et l'email
        | username | email            |
        | gbob     | gbob34@gmail.com |
        And Je clique sur le bouton Signup
        And Je mets les informations d'inscription
        | password | jourAnniversaire | moisAnniversaire | anneeAnniversaire | firstname | lastname | address        | country | state      | city  | zipcode | phone      |
        | 1234     | 10               | February         | 1994              | Bob       | David    | 3 rue des pain | Canada  | Val d'oise | Cergy | 95000   | 0123654789 |
        And Je clique sur le bouton Create ACCOUNT
        Then ACCOUNT CREATED! est visible
        When Je clique sur le bouton Continue pour finaliser l'inscription
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Add to cart du premier produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Add to cart du second produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Cart
        Then Je suis sur la page "https://automationexercise.com/view_cart"
        When Je clique sur le bouton Proceed to checkout
        Then Je vérifie que l'adresse et les produits sont les bons
        | name       | price   | quantity | total price |
        | Blue Top   | Rs. 500 | 1        | Rs. 500     |
        | Men Tshirt | Rs. 400 | 1        | Rs. 400     |
        And Je mets une description
        | description |
        | blabla      |
        When Je clique sur le bouton Place order
        And Je rentre les informations de paiements
        | name | number    | cvc | expiry mounth | expiry year |
        | Bob  | 1234 5422 | 253 | 02            | 2027        |
        And Je clique sur le bouton Pay and confirm
        Then Le message Your order has been placed successfully! est visible
        When Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible
        And Je clique sur le bouton Continue pour finaliser la suppression

    @TC16
    Scenario: Test Case 16: Place Order: Login before Checkout
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        And Je mets un email et un mot de passe correct
        | email                 | password |
        | gbob34@gmail.com      | 1234     |
        And Je clique sur le bouton Login
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Add to cart du premier produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Add to cart du second produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Cart
        Then Je suis sur la page "https://automationexercise.com/view_cart"
        When Je clique sur le bouton Proceed to checkout
        Then Je vérifie que l'adresse et les produits sont les bons
        | name       | price   | quantity | total price |
        | Blue Top   | Rs. 500 | 1        | Rs. 500     |
        | Men Tshirt | Rs. 400 | 1        | Rs. 400     |
        And Je mets une description
        | description |
        | blabla      |
        When Je clique sur le bouton Place order
        And Je rentre les informations de paiements
        | name | number    | cvc | expiry mounth | expiry year |
        | Bob  | 1234 5422 | 253 | 02            | 2027        |
        And Je clique sur le bouton Pay and confirm
        Then Le message Your order has been placed successfully! est visible
        When Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible
        And Je clique sur le bouton Continue pour finaliser la suppression

    @TC17
    Scenario: Test Case 17: Remove Products From Cart
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Add to cart du premier produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Add to cart du second produit
        And Je clique sur le bouton View Cart
        Then Je suis sur la page "https://automationexercise.com/view_cart"
        When Je clique sur la croix pour vider mon panier
        Then Mon panier est vide

    @TC18
    Scenario: Test Case 18: View Category Products
        Given Je suis le site "https://automationexercise.com/"
        Then Les catégories sont visibles sur la side bar à gauche
        When Je clique sur la catégorie Women
        And Je clique sur la sous catégorie Tops
        Then Je suis sur la page "https://automationexercise.com/category_products/2"
        And Le texte WOMEN - TOPS PRODUCTS est visible
        When Je clique sur la catégorie Men
        And Je clique sur la sous catégorie Tshirts
        Then Je suis sur la page "https://automationexercise.com/category_products/3"

    @TC19
    Scenario: Test Case 19: View & Cart Brand Products
        Given Je suis le site "https://automationexercise.com/"
        When Je clique sur le bouton Products
        Then Les marques sont visibles sur la side bar à gauche
        When Je clique sur la marque Polo
        Then Je suis sur la page "https://automationexercise.com/brand_products/Polo"
        And La liste des produits est visible
        When Je clique sur la marque Babyhug
        Then Je suis sur la page "https://automationexercise.com/brand_products/Babyhug"
        And La liste des produits est visible

    @TC20
    Scenario: Test Case 20: Search Products and Verify Cart After Login
        Given Je suis le site "https://automationexercise.com/"
        When Je clique sur le bouton Products
        Then Je suis sur la page "https://automationexercise.com/products"
        When Je rentre le nom du produit recherché
        | search product |
        | Tshirt         |
        And Je clique sur le bouton Search
        Then SEARCHED PRODUCTS est visible
        And La liste des produits est visible
        When J'ajoute le produit Men Tshirt
        And Sur le bouton Continue Shopping
        And J'ajoute le produit Pure Cotton V-Neck T-Shirt
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Cart
        Then Je verifie mon panier
        | id | name                       | price    | quantity | total price |
        | 2  | Men Tshirt                 | Rs. 400  | 1        | Rs. 400     |
        | 28 | Pure Cotton V-Neck T-Shirt | Rs. 1299 | 1        | Rs. 1299    |
        When Je clique sur le bouton Signup/Login
        And Je mets un email et un mot de passe correct
        | email                 | password |
        | stevea@gmail.com      | 1234     |
        And Je clique sur le bouton Cart
        Then Je verifie mon panier
        | id | name                       | price    | quantity | total price |
        | 2  | Men Tshirt                 | Rs. 400  | 1        | Rs. 400     |
        | 28 | Pure Cotton V-Neck T-Shirt | Rs. 1299 | 1        | Rs. 1299    |

    @TC21
    Scenario: Test Case 21: Add review on product
        Given Je suis le site "https://automationexercise.com/"
        When Je clique sur le bouton Products
        Then Je suis sur la page "https://automationexercise.com/products"
        When Je clique sur View Product du premier produits
        Then Write Your Review est visible
        When Je rentre le nom du client, l'email et une Review
        | name | email            | review     |
        | Bob  | gbob34@gmail.com | good stuff |
        And Je valide la review en cliquant sur le bouton Submit
        Then Thank you for your review est visible
    
    @TC22
    Scenario: Test Case 22: Add to cart from Recommended items
        Given Je suis le site "https://automationexercise.com/"
        When Je scroll en bas de page
        Then RECOMMENDED ITEMS est visible
        When J'ajoute le produit Stylish Dress dans le panier
        And Je clique sur le bouton View Cart
        Then Je verifie mon panier
        | id | name          | price     | quantity | total price |
        | 4  | Stylish Dress | Rs. 1500  | 1        | Rs. 1500    |

    @TC23
    Scenario: Test Case 23: Verify address details in checkout page
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je clique sur le bouton Signup/Login
        When Je mets le username et l'email
        | username | email            |
        | gbob     | gbob34@gmail.com |
        And Je clique sur le bouton Signup
        When Je mets les informations d'inscription
        | password | jourAnniversaire | moisAnniversaire | anneeAnniversaire | firstname | lastname | address        | country | state      | city  | zipcode | phone      |
        | 1234     | 10               | February         | 1994              | Bob       | David    | 3 rue des pain | Canada  | Val d'oise | Cergy | 95000   | 0123654789 |
        And Je clique sur le bouton Create ACCOUNT
        Then ACCOUNT CREATED! est visible
        When Je clique sur le bouton Continue pour finaliser l'inscription
        When J'ajoute le produit Sleeveless Dress dans le panier
        And Sur le bouton Continue Shopping
        And J'ajoute le produit Winter Top dans le panier
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Cart
        Then Je verifie mon panier
        | id | name             | price     | quantity | total price |
        | 3  | Sleeveless Dress | Rs. 1000  | 1        | Rs. 1000    |
        | 5  | Winter Top       | Rs. 600   | 1        | Rs. 600     |
        When Je clique sur le bouton Proceed to checkout
        Then Je vérifie que l'adresse de livraison est la même que celle enregistrée
        And Je vérifie que l'adresse de paiement est la même que celle enregistrée
        When Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible
        And Je clique sur le bouton Continue pour finaliser la suppression

    @TC24
    Scenario: Test Case 24: Download Invoice after purchase order
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
         When Je clique sur le bouton Add to cart du premier produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Add to cart du second produit
        And Sur le bouton Continue Shopping
        And Je clique sur le bouton Cart
        Then Je suis sur la page "https://automationexercise.com/view_cart"
        When Je clique sur le bouton Proceed to checkout
        And Je clique sur Register/Login de l'alerte qui vient d'apparaître
        And Je mets le username et l'email
        | username | email            |
        | gbob     | gbob34@gmail.com |
        And Je clique sur le bouton Signup
        And Je mets les informations d'inscription
        | password | jourAnniversaire | moisAnniversaire | anneeAnniversaire | firstname | lastname | address        | country | state      | city  | zipcode | phone      |
        | 1234     | 10               | February         | 1994              | Bob       | David    | 3 rue des pain | Canada  | Val d'oise | Cergy | 95000   | 0123654789 |
        And Je clique sur le bouton Create ACCOUNT
        Then ACCOUNT CREATED! est visible
        When Je clique sur le bouton Continue pour finaliser l'inscription
        Then Logged in as username est visible sur la page d'accueil
        When Je clique sur le bouton Cart
        And Je clique sur le bouton Proceed to checkout
        Then Je vérifie que l'adresse et les produits sont les bons
        | name       | price   | quantity | total price |
        | Blue Top   | Rs. 500 | 1        | Rs. 500     |
        | Men Tshirt | Rs. 400 | 1        | Rs. 400     |
        And Je mets une description
        | description |
        | blabla      |
        When Je clique sur le bouton Place order
        And Je rentre les informations de paiements
        | name | number    | cvc | expiry mounth | expiry year |
        | Bob  | 1234 5422 | 253 | 02            | 2027        |
        And Je clique sur le bouton Pay and confirm
        Then Le message Your order has been placed successfully! est visible
        When Je clique sur le Download Invoice
        Then Je vérifie que le fichier est téléchargé
        When Je clique sur le bouton Continue pour poursuivre ma navigation
        And Je clique sur le bouton Delete Account
        Then ACCOUNT DELETED! est visible
        And Je clique sur le bouton Continue pour finaliser la suppression
        
    @TC25
    Scenario: Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je scroll en bas de page
        Then SUBSCRIPTION est visible
        When Je clique sur la flèche située en bas à droite pour remonter
        Then Le texte Full-Fledged practice website for Automation Engineers est visible

    @TC26
    Scenario: Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
        Given Je suis le site "https://automationexercise.com/"
        Then La page d'accueil est visible
        When Je scroll en bas de page
        Then SUBSCRIPTION est visible
        When Je scroll en haut de page
        Then Le texte Full-Fledged practice website for Automation Engineers est visible