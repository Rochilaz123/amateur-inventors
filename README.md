# Amateur Inventors Forum

This website provides a forum for amateur inventors to share their ideas and engage in discussions with other inventors like themselves. Users can create posts detailing their inventive concepts, and other users can offer feedback and suggestions.

Additionally, allowing users to edit and delete their previous posts gives them full control over their content, enabling them to update their ideas based on feedback received or remove outdated posts as needed. This feature fosters a sense of ownership and responsibility among users, encouraging them to actively participate in the platform.

Overall, this website serves as a supportive community for amateur inventors to showcase their ideas, receive valuable input from their peers, and collectively contribute to the growth and development of innovative solutions.

<img src="readme-images/responsive-mockup.png" alt="Responsive Mockup" width="75%">


## Features

### Feature name

 - Navbar - Allows for easy navigation of the website. O the landing page directly under the navbar is a button urging users to join the community. This informs users what the purpose of the website is, and allows for a nice user experience as the button takes a user directly to the signup page.

	![navbar image](readme-images/navbar.png)

- Home page - The home page displays all ideas all users have posted. The user understands intuitively to click on the titles of idea posts, which takes them to a detailed view of the post

	![home page image](readme-images/home-page.png)


- Sign in / Sign up pages - The sign in and sign up pages are very easy to use, and the user can easily navigate between the pages.

![sign in image](readme-images/sign-in.png) 

- Verification Messages - The user sees verification messages upon Sign in, Sign out, leaving comments or ideas and editing or deleting comments or ideas.

![verification message image](readme-images/sign-in-message.png) 

- Idea Detail Page - The user sees a detailed veiw of a post on clicking the title. They can see any comments underneath, and then have an option to leave a comment if logged in.

![idea detail image](readme-images/idea-detail.png) 


## UX

### Site Goals

- The goal of Amateur Inventors is to provide a forum for aspiring inventors to voice their idea's and initiate discussions or provide feedback on other user's ideas. Users should be able to navigate around the site intuitively and easily. Users should also be able to update or delete any ideas or comments they have posted previously when logged in.

### User Stories

As a user:
- I can create an account, and log in.
- When logged in I can post ideas so that I can get feedback from other users.
- When logged in, I can post comments to give other users feedback and take part in discussions.
- When logged in, I can edit or delete ideas I have posted previously so that I can manage the content I share.
- When logged in, I can edit or delete comments I have previously posted so that i can manage my commments.
- I can click on a post to open a detailed view.
- I can view all ideas posted on my homepage so that i can decide which ones to look at.

### Wireframes



### Database Structure

| |Idea| |
|-----------|----------|----------|
||Title|Char Field|
||Slug|SLug Field|
|ForeignKey|Author|User Model|
|           | Purpose| Text|
|           | Mockup image| Cloudinary Field|
|           | Created On| DateTime|
|           | Details| Text|
|           | Issues| Text|
|           | Progress| Integer (choices)|
|           | Updated On| DateTime|

- Cloudinary field - I didn't use this, as I didn't want too many fields, however I left it here in case I do want to add it in at a later stage.
- Progress - I left this out as I felt it was too many fields for a user to fill out.
- Updated on -  I would possibly like to add at a later stage that an idea that was updated shows the updated date as well as the date it was posted originally.

| |Comment| |
|-----------|----------|----------|
|ForeignKey|Idea|Idea Model|
|ForeignKey|Author|User Model|
|           | Body| Text|
|           | created On| DateTime


## Testing

### Validator Testing

- HTML
	- All my code passed when run through the official [W3](https://validator.w3.org/nu/) validator. 
		- Sign up page has some errors caused by the the django allauth package.

- CSS
	- No errors returned from official [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Famateur-inventor-bd0a01aede11.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) CSS Validator.

- Python
	- No errors found with [Python](https://pep8ci.herokuapp.com/) validator.
		- In settings.py file, there are some lines that are too long, but they cannot be shortened.

### Unfixed Bugs

 - The form for the user to share an idea wasn't linked properly to Cloudinary, so the images weren't showing. I ultimately decided not to fix that bug, and to take the image option off the form, as I wanted to minimise the number of fields on the form. Additionally, most inventors at this stage won't have a mockup of the invention, so it didn't have much use.

 
 ### Testing user stories

 **Expectation:**
 As a visitor I want to understand the main purpose of the site.

 **Result:**
 As a visitor I understand this is a forum for inventors to share ideas and give feedback.

 **Expectation:**
 As a visitor, I want to be able to navigate around the site easily.

 **Result:**
 As a visitor, the site is very easy to use, and I can navigate around intuitively.

**Expectation:**
As a user, I want to be able to add, update and delete ideas and comments easily.

**Result:**
Adding and making changes to my comments and post is very easy and quick.


###  Manual Testing

|**Feature**|**Expect**|**Action**|**Result**|
|-----------|----------|----------|----------|
|Nav links| They direct the user to the correct page.| Clicked on each nav link on every page.| All nav links led to the correct pages.|



## Deployment

1. Create an account and login to Heroku.
2. Click create an app.
3. Choose a name for your app, making sure it's available.
4. 


## Citation of Sources

- The header and nav bar were partly taken from my [I Think Therefore I Blog ](https://github.com/Rochilaz123/django-blog) Project.
- The comment model and delete modal were mostly taken from [I Think Therefore I blog ](https://github.com/Rochilaz123/django-blog)Project.
- The icons in the header and footer were taken from [Font Awesome](https://fontawesome.com/search?m=free&o=r).

## Future Features

- In the future i would like to implement a feature for each user to create a profile for themselves, and you can click on the author's name to see their profile and a list of all their ideas.